fish_add_path /opt/homebrew/bin /opt/homebrew/sbin "$HOME/.local/bin"
set -gx EDITOR nvim
set -gx VISUAL nvim
set -gx PYENV_ROOT "$HOME/.pyenv"

if status is-interactive
    pyenv init - fish | source
    zoxide init fish | source
    fzf --fish | source
    atuin init fish --disable-up-arrow --disable-ai | source
    alias lg lazygit
    alias vim nvim
    alias ll 'eza -lah --git'
    alias dev 'zsh -il'
    oh-my-posh init fish | source
end

# nvm and SDKMAN are initialized in the Zsh development shell: run dev.
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
