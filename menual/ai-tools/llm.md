# LLM CLI

Simon Willison의 `llm`은 프롬프트를 표준 입력·파일·파이프라인에 연결하는 범용 모델 CLI다. Codex·Claude Code 같은 코딩 에이전트는 저장소를 읽고 도구를 호출해 여러 단계를 수행하지만, LLM은 한 번의 입력을 선택한 모델에 보내고 결과를 다음 명령에 넘기는 데 맞는다. 짧은 요약, 텍스트 변환, 구조화된 추출에는 LLM을 쓰고 여러 파일의 변경·검증에는 코딩 에이전트를 쓴다.

## 이 Mac의 설치 상태

- `0.35`로 고정했다. 공식 PyPI 기록은 이 버전을 최신 안정 릴리스로 표시하며 Python 3.10 이상, Python 3.14 호환 분류를 제공한다.
- 설치는 pyenv의 기존 CPython 3.14.7을 명시한 uv tool이다. 새 Python 런타임이나 다른 런타임 관리자는 설치하지 않았다.
- 실행 파일은 `~/.local/bin/llm`, 도구 환경은 `~/.local/share/uv/tools/llm/` 아래다. 깨끗한 Fish에서도 이 실행 파일을 찾는 것을 확인했다.
- 기본 프롬프트·응답 SQLite 로그를 껐다. macOS 사용자 데이터 경로는 `~/Library/Application Support/io.datasette.llm/`, 로그 DB는 `logs.db`, 끔 설정은 `logs-off`다. 로그를 꺼도 빈 DB가 생성될 수 있으며, 이는 프롬프트나 응답이 기록됐다는 뜻이 아니다.

API 키를 읽거나 저장하지 않았고 클라우드·유료 모델도 호출하지 않았다. 기본 모델이 목록에 보여도 인증과 비용 승인 전에는 실행하지 않는다.

## 설치와 재설치

저장소 루트에서 다음 Fish 명령을 실행한다. `(pyenv which python3)`가 이미 설치된 interpreter의 절대 경로를 전달하므로 uv가 관리 Python을 내려받지 않는다.

```fish
uv tool install --python (pyenv which python3) 'llm==0.35'
llm logs off
llm --version
llm logs status
```

동일한 과정을 스크립트로 실행하려면 다음을 사용한다.

```fish
fish local/ai-tools/llm/install.fish
```

설정만 다시 적용할 때는 `fish local/ai-tools/llm/configure.fish`를 쓴다. 이 명령은 `llm logs off`만 변경하며 기본 모델, 키, 플러그인을 설정하지 않는다.

## Fish 첫 실행과 공급자 선택

먼저 설치 상태와 지원 모델 목록을 본다.

```fish
llm --version
llm models
llm logs status
```

실제 추론은 공급자 인증을 마친 뒤에만 실행한다. API는 호출량·모델별 과금과 별도 API 키가 필요한 인터페이스다. ChatGPT·Claude 등의 웹 구독은 보통 해당 UI 사용권이며 API 크레딧이나 키를 자동으로 제공하지 않는다. 조직 계약과 공급자 정책을 확인한 뒤 필요한 한 공급자의 공식 안내로 키를 준비한다.

키는 셸 기록, 저장소, 예제 파일에 넣지 않는다. 공급자별 키 명령이나 OS 비밀 저장소 사용법은 공급자 문서와 조직 정책에 맞춰 별도로 수행한다. 이 저장소의 설치 스크립트는 키를 받거나 복사하지 않는다.

인증과 비용 승인이 끝난 뒤에는 모델을 명시해 호출한다. 기본 모델을 우연히 호출하지 않도록 일상 명령에도 `-m`을 붙인다.

```fish
set model_id 'REPLACE_WITH_APPROVED_MODEL_ID'
printf '%s\n' '회의 메모' | llm -m "$model_id" '세 문장으로 요약해 주세요' --no-log
llm -m "$model_id" '이 오류 메시지의 원인 후보를 세 개 제시해 주세요' --no-log
```

`--no-log`는 현재 로그가 꺼진 상태에서도 개별 명령의 의도를 명확히 한다. 특정 대화를 보관해야 할 때만 `--log`를 붙이고 민감한 내용은 보내지 않는다.

## 로컬 모델과 클라우드 모델

클라우드 모델은 네트워크와 공급자 계정이 필요하며 입력이 해당 공급자로 전송된다. 모델 ID·가격·보존 정책·리전은 실행 전 공급자 문서에서 확인한다. 로컬 모델은 별도 실행기와 다운로드한 모델 파일이 필요하지만 추론 트래픽을 외부 API로 보내지 않는 구성이 가능하다. LLM은 모델 플러그인으로 로컬 실행기를 연결할 수 있으나, 이번 설치에는 로컬 모델 실행기·모델 파일·플러그인을 추가하지 않았다.

새 공급자나 로컬 실행기를 연결하면 먼저 `llm models`로 모델 ID를 확인하고, 비민감한 한 줄 입력에 `--no-log`를 붙여 비용·네트워크·출력 형식을 확인한다. 플러그인은 Python 코드를 도구 환경에 설치하므로 출처·버전·권한을 검토한 경우에만 설치한다. 템플릿의 `functions:`나 도구 호출은 임의 명령 실행으로 이어질 수 있어 기본 예제에 넣지 않는다.

## 파이프라인: jq, Hurl, lnav

LLM은 표준 입력을 프롬프트에 합친다. 다음은 모델 인증이 준비된 뒤의 사용 예다. 각 블록의 `model_id`에 실제 승인 모델 ID를 넣는다.

```fish
set model_id 'REPLACE_WITH_APPROVED_MODEL_ID'

# JSON에서 필요한 필드만 추려 모델로 전달한다.
jq '{service, error, timestamp}' incident.json | \
  llm -m "$model_id" '원인 가설과 다음 점검을 한국어로 정리해 주세요' --no-log

# Hurl은 파일별 결과 JSON을 출력한다. 임시 파일에 먼저 저장해 민감한 값을 검토한다.
hurl --test --json checks/health.hurl > /tmp/hurl-result.json
jq . /tmp/hurl-result.json | \
  llm -m "$model_id" '실패 패턴만 요약해 주세요' --no-log

# lnav에서 먼저 범위를 좁힌 결과만 전달한다.
lnav -n app.log -c ';SELECT log_time, log_body FROM all_logs LIMIT 50' > /tmp/llm-log-sample.txt
llm -m "$model_id" '반복되는 오류만 분류해 주세요' --no-log < /tmp/llm-log-sample.txt
```

`jq`로 필드를 최소화하고, Hurl 보고서와 로그에는 인증 헤더·쿠키·개인정보가 없는지 먼저 확인한다. `/tmp` 샘플은 작업 후 삭제한다.

## 구조화된 출력과 템플릿

`local/ai-tools/llm/examples/incident-schema.json`은 제목·1~5 심각도·요약을 요구하는 JSON Schema다. JSON Schema를 지원하는 모델을 연결한 뒤에는 다음처럼 사용한다.

```fish
set model_id 'REPLACE_WITH_APPROVED_MODEL_ID'
llm -m "$model_id" \
  --schema local/ai-tools/llm/examples/incident-schema.json \
  '다음 사건을 분류해 주세요: 데이터베이스 연결이 5분간 실패했습니다.' \
  --no-log
```

간단한 스키마는 `llm schemas dsl 'title, severity int, summary'`로 JSON Schema로 펼쳐 볼 수 있다. 스키마 지원 여부는 모델·플러그인마다 다르므로 `llm -m "$model_id" --options`와 공급자 문서를 확인한다. 이 Mac에서는 DSL 변환만 검증했고 실제 모델의 구조화 출력은 호출하지 않았다.

재사용 프롬프트는 `llm templates edit summarize`로 만들거나 `llm templates path`에 YAML 파일을 둔다.

```yaml
system: 한국어로 간결하게 요약합니다.
prompt: '다음 내용을 요약합니다: $input'
```

실행은 `cat notes.txt | llm -t summarize -m "$model_id" --no-log`다. URL 템플릿·`functions:`·도구가 포함된 템플릿은 코드를 실행하거나 신뢰할 수 없는 지시를 가져올 수 있으므로 검토 없이 사용하지 않는다.

## 로그, 오류, 업데이트와 복구

현재 상태는 `llm logs status`, 경로는 `llm logs path`로 확인한다. 기본 로그를 다시 켜려면 `llm logs on`, 즉시 다시 끄려면 `llm logs off`다. 이미 남은 로그를 공유·삭제하기 전에는 조직 보존 정책을 확인한다.

`Error: 'Unknown model: ...'`은 모델이나 플러그인이 설치되지 않았다는 뜻이다. `llm models`로 ID를 확인한다. 인증 오류는 키가 없거나 권한이 부족한 경우가 많다. 네트워크 오류는 VPN·프록시·공급자 상태를 확인하며 키나 전체 환경 출력을 이슈에 붙이지 않는다. 스키마 오류는 모델 지원 여부와 JSON Schema 유효성을 나눠 확인한다.

업데이트는 먼저 변경 사항을 읽고 동일 interpreter를 지정한다.

```fish
set reviewed_version '0.35'
uv tool install --python (pyenv which python3) "llm==$reviewed_version"
llm --version
llm logs off
```

0.35로 되돌릴 때는 `reviewed_version`을 `0.35`로 두고 로그 상태를 다시 확인한다. 완전히 제거하려면 `uv tool uninstall llm`을 실행한다. 사용자 템플릿·키·로그 데이터는 이 명령과 별개일 수 있으므로 제거 전 `llm templates path`, `llm logs path`를 확인하고 필요한 자료만 안전한 위치에 백업한다. API 키를 저장했다면 조직 절차로 폐기·회전한다.

## 검증 범위

실제로 통과한 항목은 다음과 같다.

- 깨끗한 Fish에서 `llm --version`이 0.35를 출력하고 `~/.local/bin/llm`을 찾는다.
- `llm logs off` 뒤 `llm logs status`가 `Logging is OFF`를 출력한다.
- 일시적으로만 설치한 `llm-echo==0.3a3`에 합성 문자열을 pipe로 전달해 echo JSON의 입력·시스템·첨부·스트림 필드를 검증했다. echo 호출 자체는 공급자나 모델 네트워크를 사용하지 않는다. 처음 검사할 때의 PyPI 패키지 획득은 네트워크가 필요할 수 있다. 이후 플러그인을 제거했고 기본 모델을 변경하지 않았다.
- 제거된 `echo` 모델 호출은 비영 종료와 `Unknown model: echo` 오류를 냈다.
- `llm schemas dsl`은 예제 DSL을 JSON Schema로 변환했다.

이 검증은 실제 언어 모델 추론이나 모델 품질 평가는 아니다. 공급자 키, 과금, API 응답, 로컬 모델 실행, 공급자별 스키마 강제는 의도적으로 미검증이다. 공개 요약은 `local/ai-tools/llm/results.json`, 비공개 실행 증거는 `.local-setup/ai-tooling/llm/evidence/`에 있다.

## 참고

- [LLM 0.35 PyPI 릴리스](https://pypi.org/project/llm/0.35/)
- [LLM 공식 사용·로그 문서](https://llm.datasette.io/en/stable/usage.html)
- [LLM 템플릿 문서](https://llm.datasette.io/en/stable/templates.html)
- [LLM 스키마 문서](https://llm.datasette.io/en/stable/schemas.html)
