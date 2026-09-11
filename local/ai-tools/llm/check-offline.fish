#!/usr/bin/env fish
# Run a no-provider-network fixture check. Acquiring its temporary PyPI package may need package network access.

if not type -q llm; or not type -q jq; or not type -q rg
    echo 'llm, jq, and rg must be available.' >&2
    exit 1
end

if not llm logs status | string match -q '*Logging is OFF*'
    echo 'LLM prompt/response logging is not disabled.' >&2
    exit 1
end

set -l existing_echo (llm plugins | jq -r '.[] | select(.name == "llm-echo") | .name')
if test -n "$existing_echo"
    echo 'Refusing to alter an existing llm-echo installation.' >&2
    exit 2
end

set -l fixture_dir (mktemp -d -t llm-offline)
if test $status -ne 0; or test -z "$fixture_dir"; or not test -d "$fixture_dir"
    echo 'Could not create the temporary LLM fixture directory.' >&2
    exit 1
end

set -g llm_fixture_dir "$fixture_dir"
set -g llm_fixture_plugin_added false

function cleanup_llm_fixture --on-event fish_exit
    if test "$llm_fixture_plugin_added" = true
        llm uninstall -y llm-echo >/dev/null 2>&1
    end
    if test -n "$llm_fixture_dir"; and test -d "$llm_fixture_dir"
        command rm -rf "$llm_fixture_dir"
    end
end

llm install 'llm-echo==0.3a3'
or exit 1
set -g llm_fixture_plugin_added true

printf '%s' 'fixture-input-llm-offline' | llm -m echo > "$llm_fixture_dir/response.json"
or exit 1

jq -e '.prompt == "fixture-input-llm-offline" and .system == "" and .attachments == [] and .stream == true and .previous == []' "$llm_fixture_dir/response.json" >/dev/null
or exit 1

llm logs status > "$llm_fixture_dir/log-status.txt"
rg -qx 'Logging is OFF' "$llm_fixture_dir/log-status.txt"
or exit 1

llm uninstall -y llm-echo
or exit 1
set -g llm_fixture_plugin_added false

if llm -m echo 'fixture-input-llm-offline' > "$llm_fixture_dir/removed-plugin.stdout" 2> "$llm_fixture_dir/removed-plugin.stderr"
    echo 'The temporary echo model remained available after uninstall.' >&2
    exit 1
end

rg -q 'Unknown model: echo' "$llm_fixture_dir/removed-plugin.stderr"
or exit 1

llm plugins | jq -e 'all(.[]; .name != "llm-echo")' >/dev/null
or exit 1

echo 'Offline echo fixture passed; no cloud model, API key, or prompt log was used.'
