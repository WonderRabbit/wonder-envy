#!/usr/bin/env fish

set -l script_dir (path resolve (path dirname (status filename)))

if not command -q node; or not command -q npm
    echo "Node.js와 npm을 먼저 nvm으로 활성화하세요." >&2
    exit 1
end

node -e 'const [major, minor] = process.versions.node.split(".").map(Number); process.exit(major > 22 || (major === 22 && minor >= 22) ? 0 : 1)'
if test $status -ne 0
    echo "Node.js 22.22.0 이상이 필요합니다. 현재: "(node --version) >&2
    exit 1
end

for package in '@tobilu/qmd@2.8.3' 'repomix@1.18.0' 'promptfoo@0.123.0'
    npm install --global --save-exact $package; or exit 1
end

set -l evidence_dir (path resolve "$script_dir/../../../.local-setup/ai-tooling/node")
mkdir -p "$evidence_dir"
set -l env_backup "$evidence_dir/promptfoo-env-restore.fish"
if not test -e "$env_backup"
    begin
        echo '# 설치 전 Promptfoo Fish universal 변수 복구 명령'
        for name in PROMPTFOO_DISABLE_TELEMETRY PROMPTFOO_DISABLE_UPDATE PROMPTFOO_DISABLE_REMOTE_GENERATION PROMPTFOO_DISABLE_SHARING
            if set -qU $name
                set -l universal_show (env -u $name fish -c 'set --show $argv[1]' $name | string collect)
                set -l universal_value (env -u $name fish -c 'set variable_name $argv[1]; string escape -- $$variable_name' $name)
                if string match -q '*universal scope, exported,*' "$universal_show"
                    printf 'set -Ux %s %s\n' $name $universal_value
                else
                    printf 'set -Uu %s %s\n' $name $universal_value
                end
            else
                printf 'set -eU %s\n' $name
            end
        end
    end >"$env_backup"
end

set -Ux PROMPTFOO_DISABLE_TELEMETRY 1
set -Ux PROMPTFOO_DISABLE_UPDATE 1
set -Ux PROMPTFOO_DISABLE_REMOTE_GENERATION true
set -Ux PROMPTFOO_DISABLE_SHARING 1

echo "설치 완료:"
for command_name in qmd repomix promptfoo
    printf '  %s %s (%s)\n' $command_name ($command_name --version | string collect) (command -v $command_name)
end

echo
echo "QMD 공개 매뉴얼 색인 설정은 다음 문서를 따르세요:"
echo "  $script_dir/../../../menual/ai-tools/qmd.md"
echo "Promptfoo 환경 변수 원복 파일: $env_backup"
