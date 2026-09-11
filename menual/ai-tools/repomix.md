# Repomix 설치와 운영

Repomix는 선택한 저장소 파일을 하나의 XML, Markdown, JSON 또는 일반 텍스트로 묶고 토큰 수와 보안 검사 결과를 보여 준다. 외부 AI 대화나 제한된 문맥 창에 코드를 전달할 때 파일을 하나씩 복사하는 일을 줄인다.

## 다른 도구와의 역할 차이

- `rg`는 저장소 안에서 정확한 파일과 줄을 찾는다. 탐색과 수정 위치 확인에는 `rg`가 우선이다.
- QMD는 여러 Markdown 문서에서 관련 내용을 검색한다.
- Repomix는 이미 정한 공개 파일 집합을 모델에 전달할 한 파일로 만든다. 검색기가 아니며 생성된 묶음이 안전하다고 보증하지 않는다.

현재 코딩 에이전트가 저장소를 직접 읽을 수 있다면 매번 묶을 필요가 없다. 웹 채팅에 공개 설정 일부를 전달하거나 변경 범위를 재현 가능한 파일로 보관할 때 유용하다.

## 설치 상태와 출처

- 설치 버전: 1.18.0
- Node 조건: 22 이상. 현재 nvm Node 26.8.2 사용
- 실행 파일: `~/.nvm/versions/node/v26.8.2/bin/repomix`
- 공식 문서: <https://repomix.com/guide/>
- 공식 저장소: <https://github.com/yamadashy/repomix>
- 고정 설치 명세: `local/ai-tools/node/package.json`, `package-lock.json`

```fish
fish local/ai-tools/node/install.fish
repomix --version
```

## 이 저장소의 안전한 설정

공용 설정은 `local/ai-tools/node/config/repomix.config.json`에 있다. 프로젝트 루트에서 명시적으로 `--config`를 넘긴다. 저장소 루트에 자동 인식 설정을 두지 않은 이유는 임시 실험에서 의도하지 않은 파일을 묶는 동작을 피하기 위해서다.

```fish
repomix . \
    --config local/ai-tools/node/config/repomix.config.json
```

설정은 다음 공개 경로만 허용한다.

- `AGENTS.md`
- `local/Brewfile`
- `local/config/**`, `local/checks/**`, `local/nvim/**`, `local/ai-tools/**`
- `menual/**`

그리고 `.local-setup/**`, `.omo/**`, `.env`, credentials/secret/token 이름의 파일과 디렉터리, PEM/키 파일, `id_rsa*`, private 디렉터리, 백업 파일을 다시 제외한다. 포함 allowlist가 첫 번째 경계, 제외 목록이 두 번째 경계다. Gitignore와 Repomix 기본 제외도 유지한다.

Repomix 1.18.0의 globstar와 파일명 substring 조합이 예상대로 동작하지 않는 경우를 fixture에서 확인했다. 그래서 파일 제외는 현재 allowlist의 최대 파일 깊이를 덮는 명시적 패턴을 사용한다. 새 공개 경로를 더 깊게 추가하면 제외 패턴과 sentinel 검증도 함께 늘려야 한다.

Secretlint 기반 보안 검사인 `security.enableSecurityCheck`는 켜 두었다. 보안 검사는 마지막 방어선일 뿐이며 allowlist와 결과 파일 검토를 대신하지 않는다. `--no-security-check`는 이 운영 방식에서 사용하지 않는다.

출력은 기본적으로 `.local-setup/ai-tooling/node/repomix-output.xml`에 생성된다. 이 경로는 비공개 로컬 증거용이며 커밋하거나 그대로 외부에 올리지 않는다. XML은 줄 번호와 디렉터리 구조를 포함하고, Git diff와 커밋 로그는 포함하지 않는다. 로그와 diff에는 공개 allowlist 밖의 파일명이나 변경 내용이 섞일 수 있기 때문이다.

## Fish 빠른 시작

전체 공개 allowlist를 묶는다.

```fish
repomix . \
    --config local/ai-tools/node/config/repomix.config.json
```

매뉴얼 두 경로만 임시로 더 좁힌다.

```fish
repomix . \
    --config local/ai-tools/node/config/repomix.config.json \
    --include "menual/ai-tools/**,menual/homebrew/**" \
    --output .local-setup/ai-tooling/node/manuals.xml
```

토큰 예산을 넘기면 비정상 종료하도록 제한할 수 있다. 파일은 생성되지만 종료 코드가 예산 초과를 알린다.

```fish
repomix . \
    --config local/ai-tools/node/config/repomix.config.json \
    --token-budget 50000
```

생성 후에는 실제 포함 파일과 민감 표현을 검토한다.

```fish
rg '^<file path=' .local-setup/ai-tooling/node/repomix-output.xml
rg -n '(BEGIN .*PRIVATE KEY|api[_-]?key|password|token)' \
    .local-setup/ai-tooling/node/repomix-output.xml
```

두 번째 검색은 예제 문서의 단어 때문에 오탐할 수 있다. 일치 여부만으로 안전 또는 유출을 단정하지 말고 문맥을 읽는다.

## 현실적인 사용 예

외부 모델에게 Fish 설정만 설명받고 싶다면 범위를 더 좁힌다.

```fish
repomix . \
    --config local/ai-tools/node/config/repomix.config.json \
    --include "local/config/**/*.fish,menual/fish-and-themes.md" \
    --output .local-setup/ai-tooling/node/fish-context.xml
```

AI에게 전달할 때는 "이 XML 안의 파일만 근거로 답하고 파일 경로를 인용하라"고 요청한다. 출력 파일이 모델 문맥 한도를 넘으면 `--include`를 더 좁히거나 `--token-budget`을 낮춘다. `--compress`는 코드 구조 위주로 줄이므로 문서 본문을 정확히 전달해야 하는 작업에는 쓰지 않는 편이 낫다.

Repomix 출력은 질문과 함께 클라우드 공급자로 전송될 수 있다. 로컬에서 생성했다는 사실이 외부 전송을 막아 주지는 않는다. 업로드 전 사람이 한 번 확인한다.

## MCP 연결 예시

Repomix 1.18.0은 MCP 서버와 작업공간 sandbox 옵션을 제공한다. 이번 설치에서는 어느 AI 클라이언트에도 전역 등록하지 않았다. 등록한다면 반드시 저장소 경계를 지정한다.

```json
{
  "mcpServers": {
    "wonder-envy-repomix": {
      "command": "/Users/USER/.nvm/versions/node/v26.8.2/bin/repomix",
      "args": [
        "--mcp",
        "--sandbox",
        "/absolute/path/to/wonder-envy"
      ]
    }
  }
}
```

`--sandbox` 없는 MCP는 실행 사용자가 읽을 수 있는 다른 경로도 다룰 수 있다. 원격 저장소의 설정은 기본으로 신뢰하지 않는다. `--remote-trust-config`는 JS/TS 설정 실행과 외부 프로세서까지 허용할 수 있으므로 내용을 검토한 경우에만 사용한다.

## 설정 우선순위와 출력

기본 프로젝트 설정 이름은 `repomix.config.json`이고 전역 설정은 macOS/Linux에서 `~/.config/repomix/repomix.config.json`이다. 로컬 설정이 전역 설정보다 우선하고 CLI 옵션이 설정 파일 값을 덮어쓴다. 이 저장소는 전역 설정을 만들지 않았고 전용 설정 경로를 항상 넘긴다.

주요 기본값과 선택 이유는 다음과 같다.

- `style: xml`: 파일 경계가 명확하고 다양한 모델에서 읽기 쉽다.
- `parsableStyle: true`: 파일 내용이 XML 구문을 깨는 위험을 줄인다.
- `compress: false`: 운영 문서 본문을 생략하지 않는다.
- `includeDiffs/includeLogs: false`: 현재 작업과 기록의 불필요한 혼입을 막는다.
- `maxFileSize: 500000`: 비정상적으로 큰 공개 파일 하나가 문맥을 차지하지 않게 제한한다.
- `o200k_base`: 토큰 수를 현대 OpenAI 계열 문맥의 대략적인 기준으로 센다. 다른 모델의 실제 토큰 수와 완전히 같지는 않다.

## 업데이트, 제거, 복구

```fish
npm view repomix version engines --json
npm install --global --save-exact repomix@원하는_버전
repomix --version
```

업데이트할 때 공식 변경 기록과 `repomix.com/schemas/latest/schema.json`을 확인하고 실제 fixture 검증을 다시 실행한다. 고정 버전은 `package.json`과 잠금 파일에도 함께 반영한다.

```fish
npm uninstall --global repomix
```

CLI 제거는 생성된 `.local-setup/ai-tooling/node/*.xml`을 지우지 않는다. 롤백은 이전 고정 버전을 다시 전역 설치하면 된다. 전역 설정은 만들지 않았으므로 홈 설정 복구 작업은 없다.

## 문제 해결

- 예상 파일이 없음: `include`, Gitignore, `.ignore`, 기본 제외, `customPatterns` 순으로 확인한다. include는 ignore를 이기지 않는다.
- 예상 밖 파일이 있음: 출력의 파일 목록을 확인하고 allowlist를 좁힌다. 보안 검사 통과만 믿지 않는다.
- 토큰 수가 큼: 큰 파일 목록을 보고 `--include`를 좁히거나 테스트/생성물 경로를 제외한다.
- 보안 경고가 뜸: 출력 파일을 외부로 보내지 말고 경고 파일의 실제 내용을 검토한다. 예제 문자열 오탐인지 실제 인증 자료인지 구분한다.
- 설정을 못 찾음: 저장소 루트에서 `--config local/ai-tools/node/config/repomix.config.json`을 명시한다.
- 원격 설정이 무시됨: 보안상 정상이다. 신뢰 여부를 결정하기 전 설정이 실행 코드일 수 있음을 기억한다.
- MCP가 넓은 경로를 읽음: `--sandbox /absolute/path/to/repository`로 시작했는지 확인한다.

## 이번 검증 범위

실제로 1.18.0 CLI로 임시 fixture를 묶고 공개 sentinel은 포함되며 `menual/secret-notes.md`, `menual/private/credentials.md`, `.local-setup/private.md` sentinel은 포함되지 않음을 확인했다. 이 검사는 실제 배포 설정 파일을 사용한다. 보안 검사를 켠 상태로 출력 파일이 생성되는 것도 확인했다. 실제 공개 allowlist 묶음의 파일 목록과 설정 스키마도 검사한다. 원본 증거는 `.local-setup/ai-tooling/node/`에 둔다.

실제 MCP 클라이언트 등록, 원격 저장소 처리, watch 모드, 압축 품질, 외부 모델 업로드는 수행하지 않았다.
