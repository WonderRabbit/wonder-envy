# QMD 설치와 운영

QMD는 여러 Markdown 파일을 로컬에서 색인하고 키워드, 의미, 혼합 검색으로 찾는 도구다. 이 환경에서는 `wonder-envy` 저장소의 공개 문서인 `menual/**/*.md`만 색인한다. `~/Volt`, 홈 디렉터리 전체, `.local-setup/`, 인증 자료는 색인하지 않는다.

## 어떤 때 쓰는가

- `rg`는 파일 내용에서 정확한 문자열이나 정규식을 가장 빠르게 찾는다. 이름을 아는 설정, 에러 문자열, 코드 패턴에는 먼저 `rg`를 쓴다.
- `mdq`는 이미 선택한 Markdown 문서의 구조를 질의하고 변환한다.
- QMD는 어느 문서에 답이 있는지 모를 때 여러 문서에서 관련 구절을 찾는다. 정확한 단어가 없는 한국어 질문도 벡터 검색으로 연결할 수 있다.

따라서 `rg "JAVA_HOME" menual`처럼 표기가 확실하면 `rg`, "터미널에서 자바 버전을 바꾸려면?"처럼 개념으로 찾으면 QMD가 알맞다. QMD 검색 결과의 문서 본문을 다시 `mdq`로 좁혀도 된다.

## 설치 상태와 출처

- 설치 버전: `@tobilu/qmd` 2.8.3
- Node 조건: 22 이상. 이 Mac에서는 nvm의 Node 26.8.2를 사용한다.
- 실행 파일: `~/.nvm/versions/node/v26.8.2/bin/qmd`
- 공식 저장소: <https://github.com/tobi/qmd>
- npm 패키지: <https://www.npmjs.com/package/@tobilu/qmd>
- 고정 설치 명세: `local/ai-tools/node/package.json`, `package-lock.json`

새 Node나 Bun은 설치하지 않았다. 다음 명령은 QMD, Repomix, Promptfoo를 고정 버전으로 차례대로 설치한다.

```fish
fish local/ai-tools/node/install.fish
```

수동으로 QMD만 복구할 때는 다음처럼 실행한다.

```fish
npm install --global --save-exact @tobilu/qmd@2.8.3
qmd --version
qmd doctor
```

## 실제 설정과 저장 위치

QMD 2.8.3의 기본 전역 설정은 `~/.config/qmd/index.yml`, SQLite 색인은 `~/.cache/qmd/index.sqlite`, 모델은 `~/.cache/qmd/models/`에 저장된다. 현재 설정의 재현 예시는 `local/ai-tools/node/config/qmd-index.example.yml`에 있다. 예시의 절대 경로 자리표시자를 실제 저장소 경로로 바꾸고 기존 설정이 있으면 덮어쓰지 말고 병합한다.

현재 컬렉션의 핵심 설정은 다음과 같다.

```yaml
collections:
  wonder-envy-menual:
    path: /absolute/path/to/wonder-envy/menual
    pattern: "**/*.md"
    ignore:
      - "**/.env*"
      - "**/*credentials*"
      - "**/*secret*"
      - "**/*token*"
      - "**/*.pem"
      - "**/*.key"
      - "**/id_rsa*"
      - "**/private/**"
      - "**/*.bak"
    includeByDefault: false
```

`menual/`만 경로로 지정하는 것이 첫 번째 경계이고, 민감한 이름과 키 파일을 제외하는 것이 두 번째 경계다. `includeByDefault: false` 때문에 범위를 적지 않은 QMD 질의에는 이 컬렉션이 들어가지 않는다. 모든 예제에 `-c wonder-envy-menual`을 붙이는 이유다.

기본 모델 세 개를 명시해 버전 변경 때 모델 선택이 조용히 바뀌지 않도록 했다.

- 임베딩: `embeddinggemma-300M-Q8_0.gguf`
- 질의 확장: `qmd-query-expansion-1.7B-q4_k_m.gguf`
- 재순위: `Qwen3-Reranker-0.6B-Q8_0.gguf`

모두 로컬 GGUF 모델이며 API 키가 필요 없다. 최초 다운로드와 모델 갱신에는 Hugging Face 네트워크가 필요하고 수 GB의 디스크 공간을 쓴다. 검색할 문서 본문과 임베딩은 이 Mac에 남는다.

## 처음 설정하기

기존 `~/.config/qmd/index.yml`이 없을 때 저장소 루트에서 다음 순서로 시작한다.

```fish
qmd collection add menual --name wonder-envy-menual --mask "**/*.md"
qmd collection exclude wonder-envy-menual
qmd context add qmd://wonder-envy-menual/ "wonder-envy의 공개 한국어 설치 및 운영 매뉴얼"
```

그 다음 `local/ai-tools/node/config/qmd-index.example.yml`의 `ignore`와 `models` 항목을 실제 설정에 병합한다. 설정 파일을 직접 바꾼 뒤에는 반드시 다시 색인한다.

```fish
qmd update -c wonder-envy-menual
qmd pull --progress
qmd embed -c wonder-envy-menual --max-docs-per-batch 32 --max-batch-mb 32
qmd status
```

컬렉션 경로나 이름이 이미 다른 대상을 가리키면 자동으로 지우지 말고 `qmd collection show wonder-envy-menual`로 확인한 뒤 병합한다.

## Fish 빠른 시작

정확한 단어를 찾는 BM25 검색은 모델을 로드하지 않아 빠르다.

```fish
qmd search "Fish" -c wonder-envy-menual
qmd search '"JAVA_HOME"' -c wonder-envy-menual --format files
```

의미가 비슷한 문서를 찾을 때는 임베딩 모델을 쓰는 벡터 검색을 실행한다.

```fish
qmd vsearch "Fish에서 SDKMAN Java 경로를 보존하는 방법" \
    -c wonder-envy-menual --format json
```

BM25와 벡터 후보를 함께 합치고 재순위하려면 구조화된 혼합 질의를 쓴다. Fish에서는 `printf`의 여러 줄 출력을 `string collect`로 한 인자에 보존하는 방식이 인용 오류를 줄인다.

```fish
set -l query (printf '%s\n' \
    "intent: Fish에서 SDKMAN Java 경로 보존 방법 찾기" \
    "lex: SDKMAN JAVA_HOME" \
    "vec: Fish에서 SDKMAN Java 경로를 보존하는 방법" | string collect)
qmd query "$query" -c wonder-envy-menual --format json
```

`qmd query "질문"`의 한 줄 형식은 질의 확장 모델까지 사용한다. 이 컬렉션은 기본 검색에서 제외했으므로 여기에도 범위를 붙인다.

```fish
qmd query "Homebrew 패키지를 확인하는 순서" -c wonder-envy-menual
```

결과가 가리키는 문서를 읽을 때는 URI나 짧은 문서 ID를 사용한다.

```fish
qmd get qmd://wonder-envy-menual/fish-and-themes.md
qmd get '#문서ID'
qmd ls wonder-envy-menual
```

## 일상 운영

문서를 추가하거나 수정한 뒤에는 해당 컬렉션만 갱신한다.

```fish
qmd update -c wonder-envy-menual
qmd embed -c wonder-envy-menual
```

색인 상태와 모델 문제는 다음 명령으로 확인한다.

```fish
qmd status
qmd doctor
du -sh ~/.cache/qmd ~/.cache/qmd/models
```

벡터 검색이 느릴 때는 키워드 검색으로 시작하거나 혼합 검색에서 재순위를 생략할 수 있다.

```fish
qmd query "설치 확인" -c wonder-envy-menual --no-rerank
```

## AI와 MCP 연결 예시

QMD 2.8.3은 stdio MCP 서버를 제공한다. 이번 설치에서는 Codex, Claude Code, OpenCode 등의 전역 설정에 등록하지 않았다. 클라이언트 설정에 다음과 같은 항목을 사용하되, 실제 클라이언트의 문법을 먼저 확인한다.

```json
{
  "mcpServers": {
    "wonder-envy-qmd": {
      "command": "/Users/USER/.nvm/versions/node/v26.8.2/bin/qmd",
      "args": ["mcp"]
    }
  }
}
```

에이전트에게는 MCP `query` 도구의 `collections` 배열을 `['wonder-envy-menual']`로 제한하라고 명시한다. 단수 `collection` 필드는 2.8.3의 MCP 명세가 아니다. 로컬에서 찾은 문서 본문을 클라우드 모델 프롬프트에 붙이면 그 시점에 해당 공급자로 내용이 전송되므로, 검색이 로컬이라는 사실과 모델 전송은 구분해야 한다.

MCP를 장시간 서비스로 띄울 필요는 없다. 클라이언트가 필요할 때 stdio 프로세스를 시작하고 종료하게 둔다.

## 업데이트, 제거, 복구

업데이트 전에는 공식 변경 기록과 Node 조건을 확인하고 고정 버전과 잠금 파일을 함께 바꾼다.

```fish
npm view @tobilu/qmd version engines --json
npm install --global --save-exact @tobilu/qmd@원하는_버전
qmd doctor
qmd update -c wonder-envy-menual
qmd embed -c wonder-envy-menual
```

설정만 되돌리려면 먼저 `~/.config/qmd/index.yml`을 복사해 둔 뒤 컬렉션 항목을 제거한다. CLI로 제거하면 그 컬렉션 연결이 사라진다.

```fish
qmd collection remove wonder-envy-menual
```

프로그램 제거와 로컬 데이터 제거는 별개다.

```fish
npm uninstall --global @tobilu/qmd
```

`~/.config/qmd/`와 `~/.cache/qmd/`에는 설정, 색인, 모델이 남는다. 완전 삭제가 필요할 때만 내용을 확인하고 별도로 휴지통으로 옮긴다. npm 제거만으로 데이터가 지워지지 않으므로 재설치 롤백에 유리하다.

## 문제 해결

- `no collections configured`: 컬렉션이 없거나 다른 `--index`를 보고 있다. `qmd collection list`와 `qmd status`를 확인한다.
- `Path is not in any indexed collection`: 컨텍스트 경로는 `wonder-envy-menual:/`가 아니라 `qmd://wonder-envy-menual/` 형식이다.
- `missing 3/3 models`: `qmd pull --progress`를 실행한다. 중간에 끊겼다면 같은 명령으로 이어받는다.
- `need embedding`: `qmd embed -c wonder-envy-menual`을 실행한다. 임베딩 모델을 바꿨다면 `-f`로 해당 컬렉션 벡터를 다시 만든다.
- Metal 관련 비정상 종료: 먼저 `qmd doctor`를 확인한다. 일회성 CPU 검증은 `QMD_FORCE_CPU=1 qmd doctor` 또는 검색의 `--no-gpu`를 쓴다.
- 검색 결과가 없음: 이 컬렉션은 기본 검색에서 제외되어 있다. `-c wonder-envy-menual`을 붙였는지 확인한다.
- 새 문서가 없음: `ignore`에 걸렸는지, 확장자가 `.md`인지 확인하고 `qmd update -c wonder-envy-menual`을 실행한다.
- 모델은 정상인데 한국어 결과가 약함: 먼저 BM25와 벡터 결과를 각각 비교한다. 임베딩 모델을 바꾸면 기존 벡터와 호환되지 않으므로 설정 변경 뒤 강제 재임베딩이 필요하다.

## 이번 검증 범위

실제로 확인한 항목은 2.8.3 실행, SQLite와 sqlite-vec 로딩, Apple Metal 장치 감지, 공개 `menual/**/*.md` 컬렉션, 민감 이름 제외 규칙, 기본 검색 제외, 로컬 모델 다운로드, BM25 검색, 한국어 벡터 검색, 한국어 혼합 검색이다. 명령별 원본은 `.local-setup/ai-tooling/node/`, 공유 가능한 요약은 `local/ai-tools/node/results.json`에 둔다.

실제 MCP 클라이언트 전역 등록, `~/Volt` 색인, 장시간 벤치마크, 다른 임베딩 모델의 한국어 품질 비교는 수행하지 않았다.
