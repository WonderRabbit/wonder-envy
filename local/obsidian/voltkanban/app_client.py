"""Obsidian CLI transport with app-side compare-and-swap writes."""

from __future__ import annotations

import json
import subprocess
from dataclasses import dataclass
from pathlib import PurePosixPath
from typing import ClassVar

from pydantic import BaseModel, ConfigDict, ValidationError

from .board import BoardError


class Reply(BaseModel):
    model_config: ClassVar[ConfigDict] = ConfigDict(frozen=True, strict=True)
    ok: bool
    content: str = ""
    error: str = ""


def board_path(raw: str) -> str:
    path = PurePosixPath(raw)
    if (
        path.is_absolute()
        or ".." in path.parts
        or "\\" in raw
        or not raw.endswith(".md")
        or any(part.startswith(".") for part in path.parts)
        or any(c in raw for c in "\r\n\x00")
    ):
        raise BoardError("board must be a relative Markdown path inside the vault")
    return str(path)


@dataclass(frozen=True, slots=True)
class Change:
    path: str
    before: str | None
    after: str


@dataclass(frozen=True, slots=True)
class Client:
    vault: str
    executable: str

    def evaluate(self, code: str) -> Reply:
        try:
            output = subprocess.run(
                [self.executable, f"vault={self.vault}", "eval", f"code={code}"],
                capture_output=True,
                text=True,
                timeout=30,
                check=False,
            )
        except (OSError, subprocess.TimeoutExpired) as exc:
            raise BoardError(f"Obsidian CLI unavailable: {exc}") from exc
        _, marker, payload = output.stdout.partition("=> ")
        if output.returncode != 0 or not marker:
            raise BoardError(
                f"Obsidian command failed: {(output.stderr or output.stdout).strip()}"
            )
        try:
            reply = Reply.model_validate_json(payload.strip())
        except ValidationError as exc:
            raise BoardError(
                "invalid Obsidian CLI response; no retry was attempted"
            ) from exc
        if not reply.ok:
            raise BoardError(reply.error)
        return reply

    def read(self, path: str) -> str:
        quoted = json.dumps(board_path(path))
        code = f"""(async()=>{{try{{
            const file=app.vault.getAbstractFileByPath({quoted});
            if(!file || file.extension!=="md") throw new Error("board not found");
            return JSON.stringify({{ok:true,content:await app.vault.read(file)}});
        }}catch(e){{return JSON.stringify({{ok:false,error:String(e)}})}}}})()"""
        return self.evaluate(code).content

    def write(self, change: Change) -> None:
        data = json.dumps(
            {
                "path": board_path(change.path),
                "before": change.before,
                "after": change.after,
            }
        )
        code = """(async()=>{try{
            const p=PAYLOAD;
            if(p.before===null){
                if(app.vault.getAbstractFileByPath(p.path)) throw new Error("board already exists");
                const parts=p.path.split('/'); parts.pop();
                let folder='';
                for(const part of parts){
                    folder=folder ? folder+'/'+part : part;
                    if(!app.vault.getAbstractFileByPath(folder)) await app.vault.createFolder(folder);
                }
                await app.vault.create(p.path,p.after);
            }else{
                const file=app.vault.getAbstractFileByPath(p.path);
                if(!file || file.extension!=="md") throw new Error("board not found");
                await app.vault.process(file,current=>{
                    if(current!==p.before) throw new Error("CONFLICT: board changed; read again before retrying");
                    return p.after;
                });
            }
            return JSON.stringify({ok:true});
        }catch(e){return JSON.stringify({ok:false,error:String(e)})}})()""".replace(
            "PAYLOAD", data
        )
        _ = self.evaluate(code)
