#!/usr/bin/env fish
# Install the pinned LLM CLI with the Python selected by pyenv.

set -l llm_version 0.35

if not type -q pyenv
    echo 'pyenv is required to select the existing Python interpreter.' >&2
    exit 1
end

if not type -q uv
    echo 'uv is required to install LLM as a tool.' >&2
    exit 1
end

set -l python_path (pyenv which python3)
if test $status -ne 0; or not test -x "$python_path"
    echo 'The pyenv-selected python3 executable is unavailable.' >&2
    exit 1
end

uv tool install --python "$python_path" "llm==$llm_version"
or exit 1

fish "$PWD/local/ai-tools/llm/configure.fish"
