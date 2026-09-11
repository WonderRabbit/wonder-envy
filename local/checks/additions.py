#!/usr/bin/env python3
"""Local-only installation checks; no credentials or production services required."""
from pathlib import Path
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
import json
import os
import subprocess
import tempfile
import threading

def run(args, cwd=None, expected=0, env=None):
    p = subprocess.run(args, cwd=cwd, env=env, text=True, capture_output=True)
    if p.returncode != expected:
        raise RuntimeError(f"{args[0]} exit {p.returncode}: {p.stderr[-1500:]}")
    return p.stdout

results = {}
with tempfile.TemporaryDirectory(prefix="wonder-envy-check-") as tmp:
    root = Path(tmp)
    repo = root / "repo"
    repo.mkdir()
    run(["git", "init", "-b", "main"], repo)
    (repo / "sample.txt").write_text("base\n")
    run(["git", "add", "sample.txt"], repo)
    run(["git", "-c", "user.name=Installation Check", "-c", "user.email=check@example.invalid", "commit", "-m", "Local fixture"], repo)
    for shell, command in [("zsh", "eval \"$(wt config shell init zsh)\"; wt switch --create setup/a"),
                           ("fish", "wt config shell init fish | source; wt switch --create setup/b")]:
        run([shell, "-c", command], repo)
    worktrees = run(["git", "worktree", "list", "--porcelain"], repo)
    paths = [Path(line[9:]) for line in worktrees.splitlines() if line.startswith("worktree ")]
    others = [p for p in paths if p.resolve() != repo.resolve()]
    assert len(others) == 2
    (others[0] / "sample.txt").write_text("changed only in A\n")
    assert (others[1] / "sample.txt").read_text() == "base\n"
    assert not run(["git", "status", "--porcelain"], others[1]).strip()
    (others[0] / "sample.txt").write_text("base\n")
    for branch in ["setup/a", "setup/b"]:
        run(["wt", "remove", "--no-delete-branch", "--foreground", branch], repo)
        run(["git", "show-ref", "--verify", "refs/heads/" + branch], repo)
    results["worktrunk"] = "Zsh/Fish switch; independent files/status; branch-preserving cleanup passed"

    (repo / "mise.toml").write_text('[tasks.env-paths]\nrun = "command -v node; command -v python; command -v java"\n')
    run(["mise", "trust", str(repo / "mise.toml")], repo)
    try:
        paths = run(["fish", "-lc", "mise run env-paths"], repo)
        assert "/.nvm/" in paths and "/.pyenv/" in paths and "/.sdkman/" in paths, paths
    finally:
        run(["mise", "untrust", str(repo / "mise.toml")], repo)
    results["mise"] = "Fish task preserves nvm/pyenv/SDKMAN paths"

    class Handler(BaseHTTPRequestHandler):
        def do_GET(self):
            self.send_response(200 if self.path == "/health" else 404)
            self.end_headers()
            self.wfile.write(b"ok")
        def log_message(self, *args):
            pass
    server = ThreadingHTTPServer(("127.0.0.1", 0), Handler)
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    try:
        url = f"http://127.0.0.1:{server.server_port}"
        for endpoint, expected in [("health", 0), ("missing", 4)]:
            spec = root / (endpoint + ".hurl")
            spec.write_text(f"GET {url}/{endpoint}\nHTTP 200\n")
            run(["hurl", "--test", str(spec)], expected=expected)
    finally:
        server.shutdown()
        server.server_close()
        thread.join()
    results["hurl"] = "Loopback 200 success and deliberate 404 assertion failure passed; server stopped"

    log = root / "access.log"
    log.write_text('127.0.0.1 - - [11/Sep/2026:13:00:00 +0900] "GET /health HTTP/1.1" 200 2\n'
                   '127.0.0.1 - - [11/Sep/2026:13:00:01 +0900] "GET /missing HTTP/1.1" 404 0\n')
    out = run(["lnav", "-n", str(log), "-c", ";SELECT count(*) AS event_count FROM access_log"])
    assert "2" in out, out
    results["lnav"] = "Access-log recognition and SQL row count passed"

    (repo / "example.js").write_text("const value = 1;\n")
    run(["git", "add", "example.js"], repo)
    run(["git", "-c", "user.name=Installation Check", "-c", "user.email=check@example.invalid", "commit", "-m", "Code fixture"], repo)
    (repo / "example.js").write_text("const value=2;\n")
    assert run(["git", "-c", "diff.external=difft", "diff"], repo).strip()
    assert "diff --git" in run(["git", "diff"], repo)
    results["difftastic"] = "JavaScript one-off external diff and unchanged default Git diff passed"

print(json.dumps(results, ensure_ascii=False, indent=2))
