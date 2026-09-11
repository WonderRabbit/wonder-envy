# 런타임·Python 도구·AI CLI

기본 Fish에서 nvm·pyenv·SDKMAN을 바로 사용한다. 아래 버전 변경 명령은 프로젝트 요구가 있을 때 실행한다. 인증값을 명령 예시나 공유 파일에 직접 기록하지 않는다.

| 도구 | 사용 방법 | 공식 참고 |
| --- | --- | --- |
| Homebrew | `brew list --versions`, `brew info <이름>`; 명세 점검 `brew bundle check --file=local/Brewfile` | [공식 문서](https://docs.brew.sh/) |
| Zsh | `zsh -il`; 설정 `~/.zshrc`, 로그인 초기화 `~/.zprofile` | [공식 매뉴얼](https://zsh.sourceforge.io/Doc/) |
| nvm | `nvm ls`, 프로젝트에서 `nvm use`, 기본 복귀 `nvm use default` | [공식 저장소](https://github.com/nvm-sh/nvm) |
| Node.js | `node script.js`, `node --version` | [공식 문서](https://nodejs.org/docs/latest/api/) |
| npm / npx | 기존 잠금 기반 설치 `npm ci`, 명세의 명령 `npm run <이름>`; npx는 패키지를 내려받아 실행할 수 있음 | [npm 문서](https://docs.npmjs.com/) |
| pyenv / CPython | `pyenv versions`, `pyenv which python`, `python script.py` | [pyenv](https://github.com/pyenv/pyenv), [Python](https://docs.python.org/3/) |
| uv / uvx | `uv venv --python (pyenv which python)`, 기존 uv 프로젝트 `uv sync --locked`, `uv run <명령>`, `uv tool list` | [공식 가이드](https://docs.astral.sh/uv/) |
| SDKMAN / Java | `sdk current java`, `java -version`; 프로젝트 `.sdkmanrc` 적용 `sdk env` | [SDKMAN](https://sdkman.io/usage/), [Temurin](https://adoptium.net/temurin/) |
| Poetry | 기존 Poetry 프로젝트에서 `poetry install`, `poetry run python`; uv 전역 도구로 설치됨 | [공식 문서](https://python-poetry.org/docs/) |
| IPython | `ipython`; 프로젝트 패키지가 필요하면 해당 프로젝트 환경에서 실행 | [공식 문서](https://ipython.readthedocs.io/en/stable/) |
| Pygments | `pygmentize -l python file.py`로 코드 강조 출력 | [공식 문서](https://pygments.org/docs/) |
| Codex | Fish에서 `codex`, 버전 `codex --version`, 인증 확인 `codex login status` | [공식 CLI 문서](https://learn.chatgpt.com/docs/codex/cli) |
| Claude Code | `claude`, 최초 인증 `claude auth login`, 플러그인 확인 `claude plugin list` | [공식 문서](https://code.claude.com/docs/en/overview) |
| OpenCode | Fish에서 `opencode`; 앱 내 `/connect`로 공급자 연결 | [공식 문서](https://opencode.ai/docs/) |
| Antigravity CLI | `agy --help`; 현재 cask가 `agy` 명령 제공 | [공식 제품 안내](https://antigravity.google/product/antigravity-cli) |
| OMO / LazyCodex | Codex 재시작 후 플러그인 안내 확인; 설치 갱신은 공식 `npx lazycodex-ai` 경로, 관리 CLI는 `~/.local/bin/omo*` | [공식 저장소](https://github.com/code-yeongyu/lazycodex) |
| OMC | Claude의 `oh-my-claudecode@omc` 플러그인으로 사용; `claude plugin list`로 활성 상태 확인 | [공식 저장소](https://github.com/Yeachan-Heo/oh-my-claudecode) |
| Aside CLI | `aside --help`; 브라우저 앱 설치·로그인과 CLI는 별도 | [공식 사이트](https://aside.com/), [공식 설치자](https://releases.aside.com/install.sh) |
| Orca CLI | `orca --help`, `orca status`; 앱 관리 작업의 상태·명령 안내 확인 | [공식 문서](https://www.onorca.dev/docs) |
| Paseo CLI | `paseo --help`; 앱 번들 CLI 사용, 기존 앱과 별도 daemon을 같은 홈에서 중복 시작하지 않음 | [공식 문서](https://paseo.sh/docs) |
| Docker CLI / Compose / Buildx | `docker --version`, `docker compose version`, `docker buildx version`; 실제 컨테이너는 Docker Desktop 초기 실행 후 사용 | [Docker](https://docs.docker.com/), [Compose](https://docs.docker.com/compose/), [Buildx](https://docs.docker.com/build/) |

`uvx`는 필요시 도구를 내려받아 실행한다. nvm의 전역 npm 도구는 Node 버전마다 분리되므로 버전 변경 후 필요한 CLI를 다시 설치해야 한다. 현재 uv는 Python을 별도로 다운로드하지 않도록 구성했다.

Docker credential helper는 CLI가 로그인 자격 증명을 저장·조회할 때 사용하는 보조 실행 파일이다. 직접 토큰을 출력하는 명령을 매뉴얼에 포함하지 않는다. Docker 앱은 수동 DMG 설치이며 사용자 CLI 링크를 사용한다.

현재 기본 셸과 nvm·SDKMAN 연동은 [Fish 상세 문서](fish-and-themes.md)를 따른다.
