#!/bin/sh
set -eu

source_dir=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
runtime_dir="$HOME/.local/share/wonder-envy/obsidian"
skill_dir="$HOME/.claude/skills/volt-kanban"
backup_dir="$HOME/.local/state/wonder-envy/backups/kanban-tools/$(date +%Y%m%dT%H%M%S)-$$"

copy_file() {
    source_file=$1
    target_file=$2
    if [ -f "$target_file" ] && cmp -s "$source_file" "$target_file"; then
        return
    fi
    if [ -e "$target_file" ]; then
        mkdir -p "$backup_dir$(dirname "$target_file")"
        cp -p "$target_file" "$backup_dir$target_file"
    fi
    mkdir -p "$(dirname "$target_file")"
    cp "$source_file" "$target_file"
}

for file in voltkanban/__init__.py voltkanban/board.py voltkanban/app_client.py volt_kanban.py volt_kanban.py.lock; do
    copy_file "$source_dir/$file" "$runtime_dir/$file"
done
copy_file "$source_dir/skill/SKILL.md" "$skill_dir/SKILL.md"
copy_file "$source_dir/skill/references/commands.md" "$skill_dir/references/commands.md"
copy_file "$source_dir/commands/kanban.md" "$HOME/.claude/commands/kanban.md"
copy_file "$source_dir/commands/kanban.md" "$HOME/.config/opencode/commands/kanban.md"
copy_file "$source_dir/volt-kanban" "$HOME/.local/bin/volt-kanban"
chmod +x "$HOME/.local/bin/volt-kanban"
printf '%s\n' 'Installed volt-kanban CLI, shared skill and /kanban commands.'
