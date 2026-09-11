"""Opt-in integration against a temporary board in the running Obsidian app."""

from __future__ import annotations

import json
import os
import sys
from pathlib import Path
from uuid import uuid4

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from voltkanban.app_client import Change, Client, board_path
from voltkanban.board import (
    BoardError,
    Status,
    create_card,
    move_card,
    new_board,
    parse_board,
)


@pytest.mark.parametrize(
    "path", ["/tmp/board.md", "../board.md", ".obsidian/config.md", "board.txt"]
)
def test_board_path_rejects_outside_or_config_targets(path: str) -> None:
    with pytest.raises(BoardError):
        board_path(path)


@pytest.mark.skipif(
    os.environ.get("VOLT_KANBAN_LIVE") != "1", reason="opt-in live vault test"
)
def test_real_app_preserves_concurrent_edit_and_literal_input() -> None:
    client = Client("Volt", "/opt/homebrew/bin/obsidian")
    path = "90-System/__kanban-qa-" + uuid4().hex + ".md"
    original = new_board()
    client.write(Change(path, None, original))
    try:
        first = create_card(original, "한글 $(literal) `data`", "QA-1")
        client.write(Change(path, original, first))
        stale = create_card(original, "stale", "QA-2")
        with pytest.raises(BoardError, match="CONFLICT"):
            client.write(Change(path, original, stale))
        current = client.read(path)
        assert len(parse_board(current)) == 1
        assert "한글 $(literal) `data`" in current
        moved = move_card(current, "QA-1", Status.DONE)
        client.write(Change(path, current, moved))
        assert parse_board(client.read(path))[0].status == Status.DONE
        with pytest.raises(BoardError, match="already exists"):
            client.write(Change(path, None, original))
    finally:
        code = "(async()=>{const f=app.vault.getAbstractFileByPath(PATH);if(f)await app.vault.delete(f);return JSON.stringify({ok:true})})()".replace(
            "PATH", json.dumps(path)
        )
        client.evaluate(code)
