# CLI reference

Run the executable directly; no provider-specific API or credentials are needed.

```sh
~/.local/bin/volt-kanban list
~/.local/bin/volt-kanban create '설정 화면 개선 [[설계 노트]]'
~/.local/bin/volt-kanban create '분류 사전 검토' --id OBS-003
~/.local/bin/volt-kanban show OBS-003
~/.local/bin/volt-kanban move OBS-003 doing
~/.local/bin/volt-kanban edit OBS-003 '분류 사전 검토 #topic/obsidian'
~/.local/bin/volt-kanban done OBS-003
~/.local/bin/volt-kanban sync --from columns
~/.local/bin/volt-kanban sync --from tasks
~/.local/bin/volt-kanban --board '10-Projects/NEW/NEW Kanban.md' init
```

Global `--vault` and `--board` options go before the subcommand. Environment equivalents: `OBSIDIAN_VAULT`, `VOLT_KANBAN_BOARD`; `OBSIDIAN_CLI` overrides the Obsidian executable path.

| Column | Tasks checkbox | Meaning |
| --- | --- | --- |
| backlog | `[B]` | Not selected for execution |
| todo | `[ ]` | Ready |
| doing | `[/]` | In progress |
| review | `[R]` | Review |
| done | `[x]` | Finished |
| cancelled | `[-]` | Cancelled |

Each managed card has `#task` and a stable block ID, e.g. `^OBS-003`. List/show output is JSON with `id`, `title`, `status` (column), `symbol` (checkbox), and zero-based `line` (diagnostic only; never use line as identity). Unmanaged GUI-created cards without IDs are listed with `id: null`; sync ignores them. Add a unique block ID in Obsidian before managing such a card by CLI.

Titles are single-line Markdown. Details belong in linked notes. The helper adds no due dates or completion dates and does not execute recurring-task rules; use Tasks for recurring tasks. A Tasks GUI transition may add completion metadata; CLI operations preserve existing title metadata. Status is authoritative for CLI-managed cards.

If another process changed the board after read, the write fails with `CONFLICT` instead of overwriting that edit. App unavailable, missing ticket, duplicate ID, invalid path, and unsupported layout also return nonzero. There is no delete command; use cancelled for routine withdrawal.
