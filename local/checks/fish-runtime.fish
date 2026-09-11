# Run in a clean login Fish: see menual/fish-and-themes.md.
function require --argument-names result
    if test "$result" -ne 0
        echo "FAIL: $argv[2..]" >&2
        exit 1
    end
end
set -l fixture $argv[1]
if not test -d "$fixture"
    echo 'Pass an existing temporary fixture directory.' >&2
    exit 2
end
functions -q nvm sdk wt
require $status 'Fish manager functions'
functions -q __mise_env_eval
if test $status -eq 0
    echo 'mise runtime activation must stay disabled' >&2
    exit 1
end
test "$SHELL" = /opt/homebrew/bin/fish
require $status 'SHELL'
string match -q "$HOME/.pyenv/shims/python" (command -s python)
require $status 'pyenv shims first'
nvm use --silent default
require $status 'nvm use'
nvm exec --silent default node -e 'if (process.version !== "v26.8.2") process.exit(1); console.log("NODE_OK")'
require $status 'nvm argument forwarding and Node execution'
pyenv shell 3.14.7
require $status 'pyenv shell'
python -c 'import sys; assert sys.version_info[:3] == (3,14,7); print("PYTHON_OK")'
require $status 'Python execution'
sdk use java 26.0.2-tem >/dev/null
require $status 'sdk use'
set -l selected_java "$JAVA_HOME"
sdk current java >/dev/null
require $status 'sdk current'
test "$JAVA_HOME" = "$selected_java"
require $status 'SDKMAN selection survives subsequent calls'
printf '%s\n' 'class Main { public static void main(String[] args) { System.out.println("JAVA_OK"); } }' > "$fixture/Main.java"
java "$fixture/Main.java"
require $status 'Java source execution'
uv venv --no-managed-python --python (pyenv which python) "$fixture/.venv"
require $status 'uv venv'
source "$fixture/.venv/bin/activate.fish"
python -c 'import sys; assert sys.prefix != sys.base_prefix; print("UV_FISH_VENV_OK")'
require $status 'Fish venv activation'
deactivate
string match -q "$HOME/.pyenv/shims/python" (command -s python)
require $status 'deactivate restores pyenv'
npm --version
require $status 'npm'
lsd --color always --icon always -lah "$fixture" >/dev/null
require $status 'lsd config loading'
printf 'FISH_RUNTIME_OK\n'
