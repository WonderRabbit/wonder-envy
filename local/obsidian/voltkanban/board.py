"""Lossless single-line Kanban ticket operations; no file I/O."""

from __future__ import annotations

import re
from dataclasses import dataclass
from enum import StrEnum
from typing import Final, Literal, NewType, override

TicketId = NewType("TicketId", str)


class Status(StrEnum):
    BACKLOG = "backlog"
    TODO = "todo"
    DOING = "doing"
    REVIEW = "review"
    DONE = "done"
    CANCELLED = "cancelled"


SYMBOLS: Final = dict(zip(Status, ("B", " ", "/", "R", "x", "-"), strict=True))
CARD: Final = re.compile(r"^- \[(.)\] (.+?)(?: \^([A-Za-z0-9-]+))?$")
IDENTIFIER: Final = re.compile(r"[A-Za-z0-9]+(?:-[A-Za-z0-9]+)*")


@dataclass(slots=True)
class BoardError(Exception):
    reason: str

    @override
    def __str__(self) -> str:
        return self.reason


@dataclass(frozen=True, slots=True)
class Card:
    id: TicketId | None
    title: str
    status: Status
    symbol: str
    line: int


def new_board() -> str:
    return (
        "---\nkanban-plugin: board\n---\n\n"
        + "".join(f"## {status.value}\n\n" for status in Status)
        + '%% kanban:settings\n```\n{"kanban-plugin":"board"}\n```\n%%\n'
    )


def parse_board(source: str) -> tuple[Card, ...]:
    """Reject unsupported structure instead of silently dropping user content."""
    if "\r" in source:
        raise BoardError("Use LF line endings before managing this board")
    lines = source.splitlines(keepends=True)
    if not lines or lines[0].strip() != "---":
        raise BoardError("not a Kanban board: missing frontmatter")
    try:
        front_end = next(i for i in range(1, len(lines)) if lines[i].strip() == "---")
    except StopIteration as exc:
        raise BoardError("unclosed frontmatter") from exc
    if not re.search(r"^kanban-plugin:\s*board\s*$", "".join(lines[:front_end]), re.M):
        raise BoardError("not a Kanban board")
    result: list[Card] = []
    seen: set[TicketId] = set()
    lanes: list[Status] = []
    lane: Status | None = None
    for index in range(front_end + 1, len(lines)):
        line = lines[index].rstrip("\n")
        if line.startswith("%% kanban:settings"):
            break
        if line.startswith("## "):
            try:
                lane = Status(line[3:].strip())
            except ValueError as exc:
                raise BoardError(
                    "unsupported column; use the six standard columns"
                ) from exc
            lanes.append(lane)
            continue
        if not line.strip() or line == "**Complete**":
            continue
        found = CARD.fullmatch(line)
        if found is None or lane is None:
            raise BoardError(
                f"unsupported board content at line {index + 1}; use single-line cards"
            )
        raw_id = found[3]
        ticket_id = TicketId(raw_id) if raw_id else None
        if ticket_id is not None:
            if ticket_id in seen:
                raise BoardError(f"duplicate ticket id: {ticket_id}")
            seen.add(ticket_id)
        result.append(Card(ticket_id, found[2], lane, found[1], index))
    if len(lanes) != len(Status) or set(lanes) != set(Status):
        raise BoardError("board must contain each of the six standard columns once")
    return tuple(result)


def ticket(cards: tuple[Card, ...], identifier: str) -> Card:
    for card in cards:
        if card.id == identifier:
            return card
    raise BoardError(f"ticket not found: {identifier}")


def clean_title(title: str) -> str:
    if (
        not title.strip()
        or any(c in title for c in "\r\n\x00")
        or re.search(r"\^[A-Za-z0-9-]+", title)
    ):
        raise BoardError("title must be one nonempty line without a block ID")
    stripped = title.strip()
    return (
        stripped
        if re.search(r"(?<!\S)#task(?![\w/-])", stripped)
        else stripped + " #task"
    )


def insert_line(source: str, status: Status, line: str) -> str:
    lines = source.splitlines(keepends=True)
    index = next(
        i for i, text in enumerate(lines) if text.strip() == f"## {status.value}"
    )
    lines.insert(index + 1, "\n" + line + "\n")
    return "".join(lines)


def create_card(source: str, title: str, identifier: str) -> str:
    cards = parse_board(source)
    if not IDENTIFIER.fullmatch(identifier):
        raise BoardError(
            "ticket id must contain only letters, digits and single hyphens"
        )
    if any(card.id == identifier for card in cards):
        raise BoardError(f"duplicate ticket id: {identifier}")
    return insert_line(source, Status.TODO, f"- [ ] {clean_title(title)} ^{identifier}")


def move_card(source: str, identifier: str, status: Status) -> str:
    card = ticket(parse_board(source), identifier)
    lines = source.splitlines(keepends=True)
    line = lines.pop(card.line).rstrip("\n")
    line = f"- [{SYMBOLS[status]}] " + line[6:]
    return insert_line("".join(lines), status, line)


def edit_card(source: str, identifier: str, title: str) -> str:
    card = ticket(parse_board(source), identifier)
    lines = source.splitlines(keepends=True)
    lines[card.line] = f"- [{card.symbol}] {clean_title(title)} ^{card.id}\n"
    return "".join(lines)


def sync_board(source: str, direction: Literal["columns", "tasks"]) -> str:
    """Explicitly resolve UI drift; unnamed/unmanaged cards are left untouched."""
    result = source
    reverse = {symbol: status for status, symbol in SYMBOLS.items()}
    for card in parse_board(source):
        if card.id is None:
            continue
        status = card.status
        if direction == "tasks":
            if card.symbol not in reverse:
                raise BoardError(f"unknown task status symbol: {card.symbol}")
            status = reverse[card.symbol]
        if card.status != status or card.symbol != SYMBOLS[status]:
            result = move_card(result, card.id, status)
    return result
