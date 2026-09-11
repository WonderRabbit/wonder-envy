#!/usr/bin/env python3
"""Apply reviewed templates; preserve differing existing files in a private backup."""
from pathlib import Path
import datetime
import json
import shutil

root = Path(__file__).resolve().parent
user_home = Path.home()
stamp = datetime.datetime.now().strftime("%Y%m%d-%H%M%S-%f")
backup = user_home / ".local/state/wonder-envy/backups" / stamp
mapping = {
    "zshrc": ".zshrc",
    "config.fish": ".config/fish/config.fish",
    "uv.toml": ".config/uv/uv.toml",
    "herdr.toml": ".config/herdr/config.toml",
    "yazi.toml": ".config/yazi/yazi.toml",
    "ghostty": ".config/ghostty/config",
    "atuin.toml": ".config/atuin/config.toml",
    "mise-activate.fish": ".config/fish/conf.d/mise-activate.fish",
    "wt.fish": ".config/fish/functions/wt.fish",
    "wt-completions.fish": ".config/fish/completions/wt.fish",
}
manifest = []
for source, relative in mapping.items():
    target = user_home / relative
    data = (root / "config" / source).read_bytes()
    if target.exists() and target.read_bytes() == data:
        continue
    backup.mkdir(parents=True, exist_ok=True, mode=0o700)
    existed = target.exists() or target.is_symlink()
    if existed:
        saved = backup / relative
        saved.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(target, saved, follow_symlinks=False)
        if target.is_symlink():
            target.unlink()
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_bytes(data)
    manifest.append({"path": relative, "existed": existed})
if manifest:
    (backup / "manifest.json").write_text(json.dumps(manifest, indent=2) + "\n")
    print(f"Applied {len(manifest)} files; backup/manifest: {backup}")
else:
    print("Configuration already matches; no changes.")
