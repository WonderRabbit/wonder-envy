"""Behavior tests for the shared Kanban Markdown contract."""

import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from voltkanban.board import (
    BoardError,
    Status,
    create_card,
    edit_card,
    move_card,
    new_board,
    parse_board,
    sync_board,
)


def test_create_preserves_unicode_and_literal_shell_text() -> None:
    source = new_board()
    result = create_card(source, "한글 $(touch /tmp/no) `literal`", "OBS-002")
    card = parse_board(result)[0]
    assert (card.id, card.title, card.status) == (
        "OBS-002",
        "한글 $(touch /tmp/no) `literal` #task",
        Status.TODO,
    )


def test_move_updates_column_and_checkbox() -> None:
    source = create_card(new_board(), "First", "OBS-002")
    result = move_card(source, "OBS-002", Status.DOING)
    card = parse_board(result)[0]
    assert (card.status, card.symbol) == (Status.DOING, "/")


def test_move_preserves_other_card_and_settings() -> None:
    source = create_card(create_card(new_board(), "First", "A-1"), "Second", "A-2")
    result = move_card(source, "A-1", Status.DONE)
    assert "- [ ] Second #task ^A-2" in result
    assert (
        result.split("%% kanban:settings")[1] == source.split("%% kanban:settings")[1]
    )


def test_duplicate_id_rejected() -> None:
    source = create_card(new_board(), "First", "A-1")
    with pytest.raises(BoardError, match="duplicate"):
        create_card(source, "Again", "A-1")


def test_missing_ticket_rejected() -> None:
    with pytest.raises(BoardError, match="not found"):
        move_card(new_board(), "MISSING", Status.DONE)


@pytest.mark.parametrize("title", ["line\nbreak", "bad ^another-id", ""])
def test_invalid_title_rejected(title: str) -> None:
    with pytest.raises(BoardError):
        create_card(new_board(), title, "A-1")


def test_sync_from_tasks_handles_ui_checkbox_change() -> None:
    source = create_card(new_board(), "First", "A-1").replace(
        "- [ ] First", "- [x] First"
    )
    result = sync_board(source, "tasks")
    assert parse_board(result)[0].status == Status.DONE


def test_sync_from_columns_handles_ui_drag() -> None:
    source = move_card(
        create_card(new_board(), "First", "A-1"), "A-1", Status.DOING
    ).replace("- [/] First", "- [ ] First")
    result = sync_board(source, "columns")
    assert parse_board(result)[0].symbol == "/"


def test_edit_keeps_id_and_status() -> None:
    source = move_card(create_card(new_board(), "First", "A-1"), "A-1", Status.REVIEW)
    card = parse_board(edit_card(source, "A-1", "다시 검토"))[0]
    assert (card.id, card.status, card.title) == (
        "A-1",
        Status.REVIEW,
        "다시 검토 #task",
    )


def test_refuse_unknown_or_multiline_board_without_rewriting() -> None:
    source = create_card(new_board(), "First", "A-1").replace(
        "First #task", "First\n  nested details #task"
    )
    with pytest.raises(BoardError):
        parse_board(source)


def test_board_error_supports_exception_traceback_assignment() -> None:
    error = BoardError("missing ticket")
    error.__traceback__ = None
    assert str(error) == "missing ticket"


def test_native_kanban_settings_are_json_inside_plain_fence() -> None:
    import json

    settings = new_board().split("%% kanban:settings\n", 1)[1]
    payload = settings.replace("```", "").split("%%", 1)[0].strip()
    assert json.loads(payload) == {"kanban-plugin": "board"}
