# Promptfoo 설치와 운영

Promptfoo는 같은 입력을 여러 프롬프트나 모델에 반복하고 결과를 assertion으로 평가하는 CLI다. 프롬프트 변경의 회귀, RAG 응답 형식, 금지 문구, 구조화 출력 같은 기준을 코드와 함께 보관할 때 쓴다.

## 다른 도구와의 역할 차이

- Hurl은 HTTP 요청과 응답 상태, 헤더, 본문을 재현 가능하게 검사한다.
- 일반 테스트 러너는 순수 함수와 애플리케이션 동작을 검사한다.
- Promptfoo는 모델/프롬프트/테스트 입력 조합을 표로 실행하고 LLM 출력용 assertion과 점수를 모은다.

모델 호출 자체를 제공하는 도구는 아니다. 공급자를 OpenAI, Anthropic 등으로 설정하면 별도 계정, API 키, 요금이 필요하다. 이번 검증은 입력을 그대로 돌려주는 로컬 `echo` 공급자만 사용해 키와 비용이 없다.

## 설치 상태와 출처

- 설치 버전: 0.123.0
- Node 조건: 22.22.0 이상. 공식 권장 런타임과 다를 수 있지만 이 Mac의 Node 26.8.2에서 실제 평가를 확인했다.
- 실행 파일: `~/.nvm/versions/node/v26.8.2/bin/promptfoo`
- 별칭 실행 파일: 같은 패키지의 `pf`
- 공식 설치 문서: <https://www.promptfoo.dev/docs/installation/>
- 설정 문서: <https://www.promptfoo.dev/docs/configuration/guide/>
- 고정 설치 명세: `local/ai-tools/node/package.json`, `package-lock.json`

```fish
fish local/ai-tools/node/install.fish
promptfoo --version
```

## 개인 정보와 네트워크 기본값

Promptfoo는 기본적으로 명령과 assertion 종류 등의 사용량 telemetry를 수집하고 npm 업데이트를 확인한다. 이 환경은 Fish universal 변수로 다음 값을 설정한다.

```fish
set -Ux PROMPTFOO_DISABLE_TELEMETRY 1
set -Ux PROMPTFOO_DISABLE_UPDATE 1
set -Ux PROMPTFOO_DISABLE_REMOTE_GENERATION true
set -Ux PROMPTFOO_DISABLE_SHARING 1
```

이 변수는 새 Fish 세션에도 적용된다. remote generation 제한은 red-team 계열의 지원 경로를 막지만 네트워크 방화벽은 아니다. 설정에 외부 공급자를 직접 적으면 해당 공급자 호출은 실행된다. `--share`를 사용하지 않고 테스트 데이터에 비밀을 넣지 않는다.

universal 변수 상태는 값을 노출할 비밀이 아니므로 다음처럼 확인한다.

```fish
set -q PROMPTFOO_DISABLE_TELEMETRY; and test "$PROMPTFOO_DISABLE_TELEMETRY" = 1; and echo telemetry-disabled
set -q PROMPTFOO_DISABLE_SHARING; and test "$PROMPTFOO_DISABLE_SHARING" = 1; and echo sharing-disabled
```

## 로컬 fixture 빠른 시작

성공 fixture는 `local/ai-tools/node/examples/promptfoo/promptfooconfig.yaml`이다. `echo` 공급자는 변수 치환이 끝난 프롬프트를 그대로 출력한다. API 키, 모델 다운로드, 유료 채점기가 없다.

```fish
promptfoo eval \
    -c local/ai-tools/node/examples/promptfoo/promptfooconfig.yaml \
    --no-cache \
    --no-share \
    --no-progress-bar \
    --output .local-setup/ai-tooling/node/promptfoo-pass.json
```

성공 fixture는 QMD와 Repomix 역할 문자열이 치환됐는지 `contains`와 `equals`로 검사한다. echo 출력이 좋은 LLM 답변이라는 뜻이 아니다. 설정 파싱, 변수 치환, 공급자 실행, assertion, 결과 저장의 로컬 경로만 검증한다.

실패 보고와 종료 코드는 별도 fixture로 확인한다.

```fish
promptfoo eval \
    -c local/ai-tools/node/examples/promptfoo/expected-failure.yaml \
    --no-cache \
    --no-share \
    --no-progress-bar \
    --output .local-setup/ai-tooling/node/promptfoo-expected-failure.json
echo $status
```

이 fixture는 출력에 없는 문구를 요구하므로 정확히 종료 코드 100, `successes=0`, `failures=1`, `errors=0`이어야 한다. 단순히 0이 아닌지만 보면 설정 파싱이나 런타임 오류를 의도한 assertion 실패로 잘못 판단할 수 있다. CI에서는 성공 fixture의 종료 코드 0과 의도 실패 fixture의 정확한 종료 코드·통계를 모두 확인한다.

## 설정 파일 구조

기본 설정 파일 이름은 `promptfooconfig.yaml`이다.

```yaml
description: 공개 문자열을 사용하는 무과금 로컬 평가 예제
prompts:
  - "도구={{tool}}; 역할={{role}}"
providers:
  - id: echo
tests:
  - vars:
      tool: QMD
      role: 여러 Markdown 문서 검색
    assert:
      - type: contains
        value: "도구=QMD"
```

`prompts × providers × tests` 조합이 평가 행이 된다. 테스트 수와 공급자 수를 늘리면 호출 수와 비용도 곱으로 늘어난다. 외부 모델을 추가하기 전에 echo나 저장된 출력으로 assertion을 먼저 검증한다.

`equals`, `contains`, `is-json` 같은 결정적 assertion은 별도 채점 모델이 필요 없다. `llm-rubric`, `similar`, 모델 채점 계열은 채점 공급자와 비용이 필요할 수 있다. 자동 품질 평가를 추가할 때 생성 모델과 채점 모델의 호출을 각각 계산한다.

## 현실적인 사용 예

RAG 응답이 JSON이어야 한다면 먼저 저장된 공개 출력으로 형식을 고정한다.

```yaml
prompts:
  - '{{logged_output}}'
providers:
  - echo
tests:
  - vars:
      logged_output: '{"answer":"설정 완료","sources":["manual.md"]}'
    assert:
      - type: is-json
      - type: contains-json
        value:
          answer: 설정 완료
```

실제 서비스 호출을 평가할 때는 테스트 계정과 공개 fixture를 사용하고, 사용자 대화나 운영 로그를 그대로 커밋하지 않는다. 외부 공급자를 추가하는 예시는 다음과 같지만 이번 설치에서는 실행하거나 키를 저장하지 않았다.

```yaml
providers:
  - id: openai:chat:MODEL_NAME
prompts:
  - "{{question}}"
tests:
  - vars:
      question: 공개 테스트 질문
    assert:
      - type: contains
        value: 기대하는 핵심어
```

이 경우 공급자 공식 문서에 따라 API 키를 셸 환경이나 안전한 비밀 저장소에서 주입한다. YAML, Git, `.local-setup/` 증거에 키를 쓰지 않는다. 코딩 CLI 로그인과 모델 API 키는 자동으로 공유된다고 가정하지 않는다.

## 결과, 캐시, 로그 위치

명시한 `--output` JSON은 `.local-setup/ai-tooling/node/`에 둔다. Promptfoo는 기본적으로 홈 아래 `~/.promptfoo/`에 데이터베이스, 캐시, 로그를 만들 수 있다. 에러와 디버그 로그는 `~/.promptfoo/logs/`에서 찾거나 CLI로 조회한다.

```fish
promptfoo logs --list
```

이번 재현 명령은 `--no-cache`, `--no-share`, 명시적인 로컬 출력 경로를 사용한다. `--no-write`는 결과 저장 자체를 막으므로 검증 증거를 남길 때는 사용하지 않는다. 브라우저 UI나 watch 모드는 장시간 프로세스를 남길 수 있어 이번 설치 검증에서 시작하지 않았다.

## AI/개발 흐름에 연결하기

권장 흐름은 다음과 같다.

1. 공개 fixture와 결정적 assertion을 먼저 만든다.
2. echo 또는 이미 생성된 출력으로 평가 정의 자체가 성공/실패를 구분하는지 확인한다.
3. 실제 공급자를 한 개만 추가하고 예상 호출 수와 비용을 계산한다.
4. 결과 JSON을 비교하고 프롬프트 변경의 회귀를 리뷰한다.
5. CI에서는 `promptfoo eval`의 종료 코드를 테스트 실패로 연결한다.

QMD 검색 결과를 평가하려면 별도 스크립트나 HTTP 공급자로 실제 검색 출력을 Promptfoo에 넘길 수 있다. Repomix 결과를 모델 입력으로 쓸 때는 묶음 파일의 공개 범위 검토가 먼저다. 이번 설정은 두 도구를 자동 연결하지 않는다.

Promptfoo는 MCP 서버 등록이 필요한 도구가 아니다. 평가할 MCP 에이전트가 있다면 Promptfoo의 MCP/agent 평가 문서를 따라 별도 provider를 구성해야 하며, 이번 범위에서는 전역 AI 클라이언트 설정을 건드리지 않았다.

## 업데이트, 제거, 복구

```fish
npm view promptfoo version engines --json
npm install --global --save-exact promptfoo@원하는_버전
promptfoo --version
```

0.x 버전의 minor 변경도 호환성 변경으로 취급한다. 업그레이드 뒤 성공 fixture와 의도 실패 fixture를 모두 다시 실행하고 출력 JSON 스키마를 확인한다. 고정 버전은 `package.json`과 잠금 파일에 함께 반영한다.

CLI 제거:

```fish
npm uninstall --global promptfoo
```

설치 스크립트는 기존 universal 값과 export 상태를 덮어쓰기 전에 `.local-setup/ai-tooling/node/promptfoo-env-restore.fish`에 복구 명령을 처음 한 번 기록한다. 설치 전 사용자 설정을 보존하려면 먼저 내용을 검토한 다음 이 파일을 source한다. 기록된 값이 있으면 원래 값과 export 상태를 복원하고, 설치 전 값이 없었으면 해당 변수만 지운다.

```fish
cat .local-setup/ai-tooling/node/promptfoo-env-restore.fish
source .local-setup/ai-tooling/node/promptfoo-env-restore.fish
```

설치 전 값이 없었고 기존 설정을 복원할 필요 없이 이 네 설정을 의도적으로 제거하려는 경우에만 직접 지운다.

```fish
set -eU PROMPTFOO_DISABLE_TELEMETRY
set -eU PROMPTFOO_DISABLE_UPDATE
set -eU PROMPTFOO_DISABLE_REMOTE_GENERATION
set -eU PROMPTFOO_DISABLE_SHARING
```

`~/.promptfoo/` 데이터와 `.local-setup/ai-tooling/node/promptfoo-*` 결과는 npm 제거 후에도 남는다. 완전 삭제가 필요할 때만 내용을 확인하고 별도로 휴지통으로 옮긴다. 이전 버전으로 롤백하려면 고정 버전을 다시 설치한다.

## 문제 해결

- `Unsupported engine`: `node --version`이 22.22.0 이상인지 확인하고 nvm 경로가 Fish에서 활성화됐는지 확인한다.
- `command not found`: `command -v promptfoo`, `npm config get prefix`를 비교한다. 새 셸에서 nvm 초기화가 되었는지 확인한다.
- API 키 오류: echo fixture에는 키가 필요 없다. 외부 provider를 설정한 경우 그 공급자의 키와 모델 접근 권한을 별도로 확인한다.
- 예상치 못한 과금: provider와 model-graded assertion을 확인한다. 테스트 행 수 × prompt 수 × provider 수와 채점 호출을 센다.
- 결과가 공유됨: 명령에 `--no-share`를 사용하고 `PROMPTFOO_DISABLE_SHARING=1`을 확인한다.
- 로그가 필요함: `promptfoo logs --list` 또는 `~/.promptfoo/logs/`를 확인한다. 로그를 이 저장소에 커밋하지 않는다.
- `ExperimentalWarning: DecompressInterceptor`: Node 26에서 출력되는 런타임 경고로 이번 echo 평가의 성공/실패 판단과 분리해 기록했다. 실제 평가 종료 코드와 결과 JSON을 확인한다.
- 설치 중 optional native package script 경고: echo fixture에 필요하지 않은 Playwright, ONNX, Sharp 등의 선택 기능이 포함될 수 있다. 해당 기능이 필요할 때만 공식 설치 요구 사항을 검토하고 스크립트 허용 범위를 넓힌다.

## 이번 검증 범위

실제로 0.123.0 CLI를 Node 26.8.2에서 실행했다. 로컬 echo 성공 fixture의 테스트 케이스 2개가 통과해 `successes=2`, `failures=0`, `errors=0`을 기록했고, 의도 실패 assertion은 종료 코드 100과 `successes=0`, `failures=1`, `errors=0`을 기록했다. 여기서 2는 assertion 개수가 아니라 평가된 테스트 케이스 수다. telemetry, 업데이트 확인, 원격 생성, 공유를 끈 환경에서 실행했다. 원본 증거는 `.local-setup/ai-tooling/node/`에 둔다.

유료 또는 외부 모델 품질, 모델 채점 assertion, 브라우저 UI, watch 모드, red-team 원격 기능, MCP/agent provider 연동은 확인하지 않았다.
