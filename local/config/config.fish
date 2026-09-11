# Fish is the primary interactive and development shell.
fish_add_path /opt/homebrew/bin /opt/homebrew/sbin "$HOME/.local/bin"
set -gx EDITOR nvim
set -gx VISUAL nvim
set -gx SHELL /opt/homebrew/bin/fish
set -gx PYENV_ROOT "$HOME/.pyenv"
set -gx NVM_DIR "$HOME/.nvm"
set -gx SDKMAN_DIR "$HOME/.sdkman"

# Initialize shims for interactive shells and `fish -c` alike.
if command -q pyenv
    pyenv init - fish | source
end
# Preserve a parent's selected Node version; otherwise resolve nvm's default alias.
if set -q NVM_BIN; and test -x "$NVM_BIN/node"
    fish_add_path --path --move "$NVM_BIN"
else if test -f "$NVM_DIR/nvm.sh"
    bass 'source "$NVM_DIR/nvm.sh" --no-use; nvm use --silent default'
end
# SDKMAN management is loaded lazily by the sdk function.
if not set -q JAVA_HOME; or not test -x "$JAVA_HOME/bin/java"
    set -gx JAVA_HOME "$SDKMAN_DIR/candidates/java/current"
end
if test -x "$JAVA_HOME/bin/java"
    fish_add_path --path --move "$JAVA_HOME/bin"
end

# Keep pyenv shims before inherited interpreter paths from parent processes.
fish_add_path --path --move "$PYENV_ROOT/shims"

if status is-interactive
    fish_config theme choose catppuccin-mocha --color-theme=dark
    source "$HOME/.config/fish/fzf-catppuccin.fish"
    zoxide init fish | source
    fzf --fish | source
    atuin init fish --disable-up-arrow --disable-ai | source
    alias lg lazygit
    alias vim nvim
    alias ls lsd
    alias ll 'lsd -lah'
    alias la 'lsd -A'
    alias lt 'lsd --tree'
    alias dev 'fish -l'
    oh-my-posh init fish --config /opt/homebrew/opt/oh-my-posh/themes/catppuccin_mocha.omp.json | source
end

function y
    set -l tmp (mktemp -t yazi-cwd.XXXXXX)
    or return
    yazi $argv --cwd-file="$tmp"
    set -l result $status
    set -l cwd (cat -- "$tmp")
    if test -n "$cwd"; and test "$cwd" != "$PWD"
        builtin cd -- "$cwd"
    end
    rm -f -- "$tmp"
    return $result
end
