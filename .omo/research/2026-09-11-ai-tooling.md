# 현재 개발 환경에 연결할 AI 도구 조사

조사일: 2026-09-11, Asia/Seoul. 공식 저장소 README·릴리스 API·제품 문서를 읽었다. **설치·MCP 등록·모델 다운로드·유료 호출은 실행하지 않았다.** 아래 우선순위와 기대 효과는 현재 환경에 대한 판단이며 실측 성능 순위가 아니다.

## 현재 환경과 판단 기준

[설치 체크리스트](../../local/INSTALL-CHECKLIST.md)에 따르면 Fish, Node 26.8.2, Python 3.14.7, uv, Java/SDKMAN, LazyVim, Herdr, Worktrunk, Codex·Claude Code·OpenCode, OMO·OMC, Orca·Paseo가 준비되어 있다. Obsidian `~/Volt`와 Tasks·QuickAdd도 구성됐다. Context7은 기존 구성에 있으므로 신규 설치 후보에서 제외한다. 기존 체크리스트는 이 조사에서 재검증한 설치 결과가 아니다.

이번에 읽은 장치 메모리는 **32 GiB**다. 새 AI 실행기보다 문서 검색, 편집기 연결, 반복 평가처럼 현재 도구가 담당하지 않는 기능을 우선한다. 로컬 모델은 메모리·문맥 길이·동시 실행에 따라 실제 속도를 확인해야 한다.

## 후보 비교

버전은 조사 시 GitHub `releases/latest` 응답이며 날짜는 **UTC 게시일**이다. README의 개발 브랜치 설명과 해당 릴리스의 구현이 완전히 같다고 보장하지 않는다. 설치 시 선택한 태그의 명세를 다시 확인한다. 공개 API 확인 결과는 [JSON](2026-09-11-ai-tooling-sources.json)에 보관했다.

| 후보 | 확인된 릴리스 | 현재 환경에서 추가되는 기능 | 판단 |
| --- | --- | --- | --- |
| [QMD](https://github.com/tobi/qmd) | [v2.8.3 · 08-16](https://github.com/tobi/qmd/releases/tag/v2.8.3) | Volt·매뉴얼의 로컬 검색 결과를 CLI/MCP로 AI에 제공 | 우선 검토 |
| [Repomix](https://github.com/yamadashy/repomix) | [v1.18.0 · 08-08](https://github.com/yamadashy/repomix/releases/tag/v1.18.0) | 선택한 저장소 파일을 AI 입력용 문맥으로 묶기 | 우선 검토 |
| [Sidekick.nvim](https://github.com/folke/sidekick.nvim) | [v2.3.0 · 03-20](https://github.com/folke/sidekick.nvim/releases/tag/v2.3.0) | Neovim 선택 영역·파일 문맥을 기존 AI CLI로 전달 | 우선 검토 |
| [LLM](https://github.com/simonw/llm) | [0.35 · 09-07](https://github.com/simonw/llm/releases/tag/0.35) | Fish 파이프에서 모델 호출·요약·구조화 출력 | 반복 자동화 시 |
| [Serena](https://github.com/oraios/serena) | [v1.7.0 · 08-09](https://github.com/oraios/serena/releases/tag/v1.7.0) | LSP 기반 심볼 탐색·참조·편집 도구를 MCP로 제공 | 큰 코드 저장소에서 |
| [Promptfoo](https://github.com/promptfoo/promptfoo) | [0.123.0 · 09-10](https://github.com/promptfoo/promptfoo/releases/tag/0.123.0) | 프롬프트·모델·RAG 출력의 반복 평가 | AI 기능 개발 시 |
| [MCPorter](https://github.com/openclaw/mcporter) | [v0.13.10 · 09-05](https://github.com/openclaw/mcporter/releases/tag/v0.13.10) | MCP 도구를 셸·스크립트에서 직접 호출 | MCP 자동화 필요 시 |
| [Ollama](https://github.com/ollama/ollama) | [v0.34.0 · 09-05](https://github.com/ollama/ollama/releases/tag/v0.34.0) | 로컬 모델 실행 서버 | 로컬 처리 수요 확인 후 |
| [agent-browser](https://github.com/vercel-labs/agent-browser) | [v0.37.1 · 09-08](https://github.com/vercel-labs/agent-browser/releases/tag/v0.37.1) | 셸에서 재현 가능한 브라우저 자동화 | 기존 브라우저 도구와 비교 후 |
| [Spec Kit](https://github.com/github/spec-kit) | [v1.0.6 · 09-10](https://github.com/github/spec-kit/releases/tag/v1.0.6) | 명세 중심 개발 절차·산출물 | OMO·기존 계획과 겹쳐 보류 |

## 1. QMD — Volt와 프로젝트 문서를 AI가 검색하도록 연결

QMD는 BM25 키워드 검색, 벡터 검색, 로컬 모델 재순위화를 조합하며 JSON 출력과 MCP를 지원한다. `mdq`는 Markdown을 질의·가공하는 기존 도구이고, `qmd`는 여러 문서에서 관련 내용을 검색하는 별도 도구다. [공식 설명](https://github.com/tobi/qmd)

현재 Node는 태그 v2.8.3의 `>=22` 조건을 충족하고 Homebrew SQLite도 설치되어 있다. 공식 quick start는 npm과 Bun을 대안으로 제시하므로 **현재 Node 경로를 우선**한다. Ollama를 추가하지 않아도 QMD 자체의 node-llama-cpp 경로로 로컬 모델을 사용한다. 문서에 제시된 기본 모델 파일은 합계 약 2GB이며 런타임 메모리와 인덱스 공간은 별도다. [패키지 조건](https://github.com/tobi/qmd/blob/v2.8.3/package.json), [요구 사항](https://github.com/tobi/qmd#requirements)

도입 시 처음에는 공개 가능한 `menual/`만 색인하고, 한국어 질의 10개로 ripgrep·Obsidian 검색 대비 찾는 문서의 정확도와 소요 시간을 비교한다. 이후 `~/Volt`의 필요한 폴더만 확장한다. 검색이 로컬이어도 검색 결과를 클라우드 AI에 전달하면 그 내용은 해당 공급자로 전송된다.

아래는 설치 후의 Fish 예시이며 이번 조사에서는 실행하지 않았다.

```fish
qmd collection add ./menual --name envy-manual
qmd search 'Fish Java 설정' -c envy-manual --json
# 모델 다운로드·임베딩 생성을 수반하는 다음 단계
qmd embed
qmd query '터미널에서 자바 버전은 어떻게 바꾸는가'
```

## 2. Repomix — 필요한 코드만 문맥으로 전달

Repomix는 저장소를 XML 등의 AI 입력 파일로 묶고 토큰 수 계산과 Secretlint 기반 검사를 제공한다. 여러 파일을 수동으로 복사하는 작업을 줄인다. 전체 저장소를 읽을 수 있는 현재 에이전트 안에서는 매번 사용할 필요가 없고, 외부 대화에 코드 설명을 전달하거나 제한된 범위를 리뷰받을 때 가치가 크다. [공식 사용법](https://github.com/yamadashy/repomix)

태그 v1.18.0은 Node `>=22`를 요구한다. 기존 nvm의 npm 경로 또는 버전을 고정한 일회성 실행을 사용하고 별도 Node 관리자를 추가하지 않는 것이 맞다. [패키지 조건](https://github.com/yamadashy/repomix/blob/v1.18.0/package.json)

파일 포함 범위를 명시하고 `.local-setup/`, 키·인증 파일, 사용자 보관함을 출력에 넣지 않는다. 자동 검사는 누락 가능성이 있어 묶음 자체를 확인해야 한다. 시범 기준은 같은 질문에 필요한 파일 누락 여부·토큰 수·답변 근거를 수동 파일 선택 방식과 비교하는 것이다. 최초 시험은 이 저장소의 공개 문서나 작은 테스트 프로젝트면 충분하다.

## 3. Sidekick.nvim — 현재 AI CLI를 LazyVim 안에서 사용

AI CLI 터미널을 Neovim에 연결하고 파일·선택 영역을 프롬프트 문맥으로 전달한다. 새로운 AI 공급자를 반드시 추가하는 도구는 아니다. Neovim `>=0.11.2`를 요구하므로 현재 기록된 0.12.5는 조건을 충족한다. [공식 저장소](https://github.com/folke/sidekick.nvim)

공식 FAQ는 CLI 기능이 Copilot 구독 없이 동작한다고 구분한다. 현재 환경에서는 **NES를 끄고 CLI 기능부터 사용**하는 구성이 맞다. 지속 세션의 mux 백엔드는 tmux·Zellij이므로 `mux.enabled=false`를 유지한다. Herdr가 해당 백엔드라고 가정하지 않는다. [공식 FAQ](https://github.com/folke/sidekick.nvim#-faq)

이렇게 하면 Herdr는 작업 공간·pane, Worktrunk는 Git 작업 분리, Sidekick은 편집기 문맥 전달을 담당한다. 시범에서는 선택한 함수만 전달되는지, 기존 LazyVim 키와 충돌하지 않는지, 에디터 종료 시 CLI 세션의 수명이 기대와 맞는지 확인한다. API 사용량이나 기존 서비스 요금은 사용하는 AI CLI의 정책을 따른다.

## 4. LLM — Fish 파이프를 위한 작은 모델 호출기

`llm`은 여러 공급자와 로컬 모델 플러그인을 지원하는 CLI다. 대화형 코딩 에이전트와 별도로, 정해진 파일 요약·JSON 추출·반복 프롬프트 같은 짧은 파이프 작업에 적합하다. 기존 uv tool 관리 방식과 연결할 수 있으며 0.35의 Python 조건은 `>=3.10`이다. [공식 저장소](https://github.com/simonw/llm), [Python 조건](https://github.com/simonw/llm/blob/0.35/pyproject.toml)

예를 들어 공개 샘플 로그를 lnav로 좁힌 다음 LLM으로 요약하고 결과를 jq로 처리할 수 있다. 셸 명령 자동 실행보다 구조화된 결과 생성부터 시험하는 것이 현재 구성에 잘 맞는다. 프롬프트·응답은 기본적으로 SQLite에 기록되므로 도입 시 `llm logs off` 또는 호출별 `--no-log` 정책을 정한다. [로그 문서](https://llm.datasette.io/en/stable/logging.html)

클라우드 API는 공급자 계정·키와 요금이 필요하다. 기존 코딩 CLI의 로그인만으로 모든 LLM 공급자 연결이 자동 해결된다고 가정하지 않는다. 이번 조사에서는 모델 선택·API 호출을 하지 않았다.

## 5. Serena — 큰 코드베이스에서 심볼 단위 작업

Serena는 언어 서버 등의 백엔드로 심볼·참조를 검색하고 편집하는 MCP 도구 모음이다. 파일명·문자열을 찾는 rg나 코드 구조를 찾는 ast-grep을 보완한다. 다만 현재 제공된 OMO의 LSP 기능과 겹칠 수 있으므로, 사용 중인 클라이언트에서 부족한 기능이 확인될 때 도입한다. 문서 중심인 wonder-envy 자체에는 우선순위가 낮다. [공식 설명](https://github.com/oraios/serena)

최신 README는 `uv tool install -p 3.13 serena-agent`를 안내하지만, v1.7.0의 Python 범위는 `>=3.11,<3.15`다. 따라서 현재 Python 3.14.7은 선언상 범위에 들어간다. 의존성과 대상 언어 LSP의 실제 호환성은 미검증이며, 필요할 때만 pyenv로 3.13을 병행하고 기존 기본값은 유지한다. uv의 자동 Python 다운로드 금지 설정을 임의로 해제하지 않는다. [태그 명세](https://github.com/oraios/serena/blob/v1.7.0/pyproject.toml)

한 개의 실제 코드 프로젝트에서 대표 심볼 5개의 정의·참조를 기존 도구와 비교하고 수정 기능은 분리된 worktree에서 평가한다. 공급자 과금은 연결한 AI 모델에 달려 있다.

## 6. Promptfoo — 프롬프트 변경도 반복 평가

Promptfoo는 프롬프트·모델·RAG·에이전트 출력의 평가를 CLI와 설정 파일로 반복한다. Hurl이 HTTP 응답을 확인한다면 Promptfoo는 AI 응답의 기준을 확인한다. 현재 환경 관리 저장소보다 실제 AI 기능을 만드는 프로젝트에 설치하는 편이 적합하다. [공식 저장소](https://github.com/promptfoo/promptfoo)

현재 문서는 Node `>=22.22.0`, 권장 Node 24 LTS를 명시한다. Node 26.8.2는 최소 조건을 충족하지만 권장 버전과 같지는 않으므로 첫 평가를 실행해 확인한다. 글로벌 도구 추가보다 프로젝트 개발 의존성과 잠금 파일에 버전을 고정하는 방식을 추천한다. [런타임 지원](https://www.promptfoo.dev/docs/installation/)

공개 샘플 10개와 JSON 필수 필드·금지 응답·정답 근거 등 3개 기준으로 시작한다. 평가 실행기가 로컬이어도 외부 모델·채점 모델을 사용하면 입력 전송과 호출 비용이 발생한다. 실측 전에는 모델 교체가 더 좋거나 저렴하다고 결론 내리지 않는다.

## 조건부 후보와 중복 검토

- **MCPorter**: MCP 도구를 CLI·스크립트로 부를 필요가 있을 때 유용하다. 기존 AI 클라이언트 안에서만 MCP를 쓴다면 필수는 아니다. npm 경로의 Node 조건은 24 이상으로 현재 버전이 충족한다. 예전 `steipete/mcporter` 링크는 현재 `openclaw/mcporter`로 연결된다. 전체 클라이언트 설정 자동 수집보다 필요한 서버 한 개를 명시적으로 연결해 시작한다. [공식 문서](https://github.com/openclaw/mcporter)
- **Ollama**: 모델을 로컬에 두고 LLM CLI 등과 연결할 때 후보가 된다. 32GiB에서는 작은 양자화 모델부터 단일 동시 요청으로 처리량·한국어 정확도·메모리 압박을 측정하는 접근을 추천한다. 이는 하드웨어에 대한 시험 제안이며 특정 모델의 적합성 보장은 아니다. 컨텍스트 증가도 메모리를 더 요구한다. QMD 때문에 의무적으로 설치할 필요는 없다. 모델별 라이선스와 Ollama 자체 라이선스는 구분한다. [공식 저장소](https://github.com/ollama/ollama), [메모리·실행 FAQ](https://docs.ollama.com/faq)
- **agent-browser**: CI나 셸에서 같은 브라우저 작업을 반복할 목적이면 검토한다. 최신 README는 네이티브 Rust 바이너리와 Chrome 사용을 안내한다. 기존 Codex 브라우저·Chrome 도구와 Aside가 있으므로 단순 브라우징만을 위해 추가할 가치는 낮다. 새 브라우저 다운로드·로그인 상태 관리 부담도 비교한다. [공식 저장소](https://github.com/vercel-labs/agent-browser)
- **Spec Kit·Superpowers**: 명세·계획·구현 절차를 보강하지만 현재 `.omo/plans`, OMO·OMC와 겹친다. 같은 저장소에 여러 계획·검토 지침을 동시에 적용하면 우선순위와 산출물이 중복될 수 있어 현재 추천 묶음에서는 제외한다. [Spec Kit](https://github.github.io/spec-kit/), [Superpowers](https://github.com/obra/superpowers)
- **Goose·Docker Agent**: 추가 에이전트 실행기 후보지만 이미 여러 CLI와 Orca·Paseo·Herdr가 있다. 현재 빈 기능을 채우는 이점이 명확하지 않아 상세 도입 평가를 보류한다. Docker 기반 실험은 체크리스트에 남은 Docker 최초 실행도 선행해야 한다. [Goose](https://github.com/aaif-goose/goose), [Docker Agent](https://github.com/docker/docker-agent)

## 제안하는 시범 순서

1. **QMD + Repomix**: 문서를 찾고 필요한 코드만 전달하는 흐름부터 확인한다. QMD는 한국어 검색 정확도를 반드시 비교한다.
2. **Sidekick CLI 기능**: 기존 AI CLI를 편집기에 연결한다. NES·mux를 끈 최소 구성으로 시작한다.
3. **LLM 또는 Promptfoo**: 반복 문서 처리면 LLM, AI 제품의 회귀 평가면 Promptfoo를 선택한다.
4. **Serena·Ollama·MCPorter**: 실제 코드 규모, 로컬 추론 필요, MCP 자동화 필요가 확인된 뒤 추가한다.

시범에서 통과한 도구만 설치 계획·체크리스트와 `menual/`에 편입한다. 이번 리서치는 설치 완료 상태를 바꾸지 않으며 현재 Fish·런타임·MCP 설정도 변경하지 않았다.
