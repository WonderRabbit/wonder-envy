#!/usr/bin/env fish

# Reinstall the pinned helper CLIs with the existing nvm and uv runtimes.
set -l script_dir (path resolve (path dirname (status filename)))
set -l repo_root (path resolve "$script_dir/../..")

fish "$script_dir/node/install.fish"; or exit 1
fish "$script_dir/llm/install.fish"; or exit 1

# This copies the reviewed Sidekick LazyVim declaration and backs up differing files.
python3 "$repo_root/local/apply-config.py"; or exit 1
nvim --headless '+Lazy! install sidekick.nvim' +qa; or exit 1

echo 'Pinned CLI installation and Sidekick configuration completed.'
echo 'QMD collection, local model download, and indexing remain separate:'
echo '  menual/ai-tools/qmd.md#처음-설정하기'
