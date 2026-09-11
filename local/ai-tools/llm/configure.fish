#!/usr/bin/env fish
# Persist the repository policy: do not retain ordinary LLM prompts or responses.

if not type -q llm
    echo 'llm is not on PATH; run install.fish first.' >&2
    exit 1
end

llm logs off
or exit 1

llm logs status
