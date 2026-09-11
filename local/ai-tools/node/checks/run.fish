#!/usr/bin/env fish

set -l script_dir (path resolve (path dirname (status filename)))
set -l node_dir (path resolve "$script_dir/..")
set -l repo_root (path resolve "$node_dir/../../..")
set -l evidence_dir "$repo_root/.local-setup/ai-tooling/node"
mkdir -p "$evidence_dir"
set -g fixture_dir ''

function cleanup_node_ai_fixture --on-event fish_exit
    if test -n "$fixture_dir"; and test -d "$fixture_dir"
        rm -r -- "$fixture_dir"
    end
end

for command_name in qmd repomix promptfoo
    command -q $command_name; or begin
        echo "명령을 찾을 수 없습니다: $command_name" >&2
        exit 1
    end
end

qmd status >"$evidence_dir/qmd-status.log" 2>&1; or exit 1
qmd search "Fish" -c wonder-envy-menual --format json >"$evidence_dir/qmd-keyword.json" 2>"$evidence_dir/qmd-keyword.stderr"; or exit 1
jq -e 'length > 0 and all(.[]; (.file | startswith("qmd://wonder-envy-menual/"))) and any(.[]; .file | contains("fish-and-themes.md"))' "$evidence_dir/qmd-keyword.json" >/dev/null; or exit 1
qmd vsearch "Fish에서 SDKMAN Java 경로를 보존하는 방법" -c wonder-envy-menual --format json >"$evidence_dir/qmd-vector-ko.json" 2>"$evidence_dir/qmd-vector-ko.stderr"; or exit 1
jq -e 'length > 0 and all(.[]; (.file | startswith("qmd://wonder-envy-menual/"))) and .[0].file == "qmd://wonder-envy-menual/fish-and-themes.md"' "$evidence_dir/qmd-vector-ko.json" >/dev/null; or exit 1
set -l hybrid_query (printf '%s\n' "intent: Fish에서 SDKMAN Java 경로 보존 방법 찾기" "lex: SDKMAN JAVA_HOME" "vec: Fish에서 SDKMAN Java 경로를 보존하는 방법" | string collect)
qmd query "$hybrid_query" -c wonder-envy-menual --format json >"$evidence_dir/qmd-hybrid-ko.json" 2>"$evidence_dir/qmd-hybrid-ko.stderr"; or exit 1
jq -e 'length > 0 and all(.[]; (.file | startswith("qmd://wonder-envy-menual/"))) and .[0].file == "qmd://wonder-envy-menual/fish-and-themes.md"' "$evidence_dir/qmd-hybrid-ko.json" >/dev/null; or exit 1

set fixture_dir (mktemp -d); or begin
    echo "임시 Repomix fixture 디렉터리를 만들지 못했습니다." >&2
    exit 1
end
test -n "$fixture_dir"; and test -d "$fixture_dir"; or begin
    echo "mktemp가 유효한 fixture 디렉터리를 반환하지 않았습니다." >&2
    exit 1
end
mkdir -p "$fixture_dir/menual/private" "$fixture_dir/.local-setup"; or exit 1
printf '%s\n' PUBLIC_SENTINEL_REPOMIX >"$fixture_dir/menual/guide.md"; or exit 1
printf '%s\n' EXCLUDED_SENTINEL_CREDENTIALS >"$fixture_dir/menual/private/credentials.md"; or exit 1
printf '%s\n' EXCLUDED_SENTINEL_SECRET_FILENAME >"$fixture_dir/menual/secret-notes.md"; or exit 1
printf '%s\n' EXCLUDED_SENTINEL_LOCAL_SETUP >"$fixture_dir/.local-setup/private.md"; or exit 1
pushd "$fixture_dir" >/dev/null
repomix . --config "$node_dir/config/repomix.config.json" --output "$evidence_dir/repomix-fixture.xml" >"$evidence_dir/repomix-fixture.log" 2>&1
set -l repomix_status $status
popd >/dev/null
test "$repomix_status" -eq 0; or exit 1
rg -q PUBLIC_SENTINEL_REPOMIX "$evidence_dir/repomix-fixture.xml"; or exit 1
if rg -q 'EXCLUDED_SENTINEL_(CREDENTIALS|SECRET_FILENAME|LOCAL_SETUP)' "$evidence_dir/repomix-fixture.xml"
    echo "Repomix 제외 sentinel이 출력에 포함됐습니다." >&2
    exit 1
end
rm -r -- "$fixture_dir"
set fixture_dir ''

set -lx PROMPTFOO_DISABLE_TELEMETRY 1
set -lx PROMPTFOO_DISABLE_UPDATE 1
set -lx PROMPTFOO_DISABLE_REMOTE_GENERATION true
set -lx PROMPTFOO_DISABLE_SHARING 1
promptfoo eval -c "$node_dir/examples/promptfoo/promptfooconfig.yaml" --no-cache --no-share --no-progress-bar --output "$evidence_dir/promptfoo-pass.json" >"$evidence_dir/promptfoo-pass.log" 2>&1; or exit 1
jq -e '.results.stats.successes == 2 and .results.stats.failures == 0 and .results.stats.errors == 0' "$evidence_dir/promptfoo-pass.json" >/dev/null; or exit 1

promptfoo eval -c "$node_dir/examples/promptfoo/expected-failure.yaml" --no-cache --no-share --no-progress-bar --output "$evidence_dir/promptfoo-expected-failure.json" >"$evidence_dir/promptfoo-expected-failure.log" 2>&1
set -l failure_status $status
if test "$failure_status" -ne 100
    echo "Promptfoo 의도 실패 fixture의 종료 코드가 100이 아닙니다: $failure_status" >&2
    exit 1
end
jq -e '.results.stats.successes == 0 and .results.stats.failures == 1 and .results.stats.errors == 0' "$evidence_dir/promptfoo-expected-failure.json" >/dev/null; or exit 1

printf 'qmd=ok repomix=ok promptfoo_pass=ok promptfoo_expected_failure_exit=%s\n' "$failure_status"
