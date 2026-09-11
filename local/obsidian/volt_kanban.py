#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.13"
# dependencies = ["typer>=0.16,<1", "rich>=14,<15", "pydantic>=2.11,<3"]
# ///
# ─── How to run ───
# Install uv with Homebrew: brew install uv
# Run: uv run local/obsidian/volt_kanban.py --help
# ──────────────────
"""Shared Kanban ticket CLI for OpenCode and Claude Code."""

from __future__ import annotations

import json
import os
from dataclasses import asdict, dataclass
from typing import Annotated, Literal
from uuid import uuid4

import typer

from voltkanban.app_client import Change, Client, board_path
from voltkanban.board import (
    BoardError,
    Status,
    create_card,
    edit_card,
    move_card,
    new_board,
    parse_board,
    sync_board,
    ticket,
)


@dataclass(frozen=True, slots=True)
class Target:
    client: Client
    path: str


app = typer.Typer(no_args_is_help=True, pretty_exceptions_enable=False)


@app.callback()
def options(
    ctx: typer.Context,
    vault: Annotated[str, typer.Option(envvar="OBSIDIAN_VAULT")] = "Volt",
    board: Annotated[
        str, typer.Option(envvar="VOLT_KANBAN_BOARD")
    ] = "10-Projects/OBS-Obsidian/OBS Kanban.md",
) -> None:
    """Manage single-line board tickets through the running Obsidian app."""
    ctx.obj = Target(
        Client(vault, os.environ.get("OBSIDIAN_CLI", "/opt/homebrew/bin/obsidian")),
        board_path(board),
    )


def target(ctx: typer.Context) -> tuple[Client, str]:
    selected = ctx.ensure_object(Target)
    return selected.client, selected.path


@app.command()
def init(ctx: typer.Context) -> None:
    """Create a board; existing files are never overwritten."""
    client, path = target(ctx)
    client.write(Change(path, None, new_board()))
    typer.echo(json.dumps({"board": path, "created": True}))


@app.command("list")
def list_cards(ctx: typer.Context) -> None:
    """List cards, IDs, columns and checkbox symbols as JSON."""
    client, path = target(ctx)
    typer.echo(
        json.dumps(
            [asdict(card) for card in parse_board(client.read(path))],
            ensure_ascii=False,
        )
    )


@app.command()
def show(ctx: typer.Context, identifier: str) -> None:
    client, path = target(ctx)
    typer.echo(
        json.dumps(
            asdict(ticket(parse_board(client.read(path)), identifier)),
            ensure_ascii=False,
        )
    )


@app.command()
def create(
    ctx: typer.Context,
    title: str,
    identifier: Annotated[str | None, typer.Option("--id")] = None,
) -> None:
    """Create a todo card. IDs default to random kb- identifiers."""
    client, path = target(ctx)
    key = identifier or "kb-" + uuid4().hex
    source = client.read(path)
    client.write(Change(path, source, create_card(source, title, key)))
    typer.echo(json.dumps({"id": key, "status": "todo"}))


@app.command()
def move(ctx: typer.Context, identifier: str, status: Status) -> None:
    """Move a ticket and update its Tasks checkbox in one atomic write."""
    client, path = target(ctx)
    source = client.read(path)
    client.write(Change(path, source, move_card(source, identifier, status)))
    typer.echo(json.dumps({"id": identifier, "status": status.value}))


@app.command()
def done(ctx: typer.Context, identifier: str) -> None:
    """Move a ticket to done."""
    move(ctx, identifier, Status.DONE)


@app.command()
def edit(ctx: typer.Context, identifier: str, title: str) -> None:
    client, path = target(ctx)
    source = client.read(path)
    client.write(Change(path, source, edit_card(source, identifier, title)))
    typer.echo(json.dumps({"id": identifier, "updated": True}))


@app.command()
def sync(
    ctx: typer.Context,
    source_of_truth: Annotated[Literal["columns", "tasks"], typer.Option("--from")],
) -> None:
    """Reconcile after GUI edits; explicitly choose columns or Tasks symbols."""
    client, path = target(ctx)
    source = client.read(path)
    client.write(Change(path, source, sync_board(source, source_of_truth)))
    typer.echo(json.dumps({"board": path, "syncedFrom": source_of_truth}))


def main() -> None:
    try:
        app()
    except BoardError as exc:
        typer.echo(json.dumps({"error": str(exc)}, ensure_ascii=False), err=True)
        raise SystemExit(1) from exc


if __name__ == "__main__":
    main()
