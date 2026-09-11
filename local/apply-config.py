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
    "nvm.fish": ".config/fish/functions/nvm.fish",
    "sdk.fish": ".config/fish/functions/sdk.fish",
    "fzf-catppuccin.fish": ".config/fish/fzf-catppuccin.fish",
    "../vendor/lazygit-mocha.yml": "Library/Application Support/lazygit/config.yml",
    "../vendor/eza-theme.yml": ".config/eza/theme.yml",
    "lnav.json": ".config/lnav/config.json",
    "opencode-tui.json": ".config/opencode/tui.json",
    "lsd.yaml": ".config/lsd/config.yaml",
    "../vendor/lsd-colors.yaml": ".config/lsd/colors.yaml",
    "bass.fish": ".config/fish/functions/bass.fish",
    "../vendor/__bass.py": ".config/fish/functions/__bass.py",
    "../vendor/yazi-theme.toml": ".config/yazi/theme.toml",
    "../vendor/catppuccin-mocha.tmTheme": ".config/yazi/Catppuccin-mocha.tmTheme",
    "../vendor/atuin-mocha.toml": ".config/atuin/themes/catppuccin-mocha-mauve.toml",
    "../nvim/lua/plugins/colorscheme.lua": ".config/nvim/lua/plugins/colorscheme.lua",
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
