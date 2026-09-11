# 패키지 관리자와 전역 개발 도구 이전

관측일: 2026-09-06. 이 문서는 새 Mac mini에서 실행할 설치 순서다. 현재 Mac에서는 설치·업데이트·테스트·QA를 수행하지 않았다. 관측 버전은 기존 상태를 설명하는 기록이며 새 Mac은 최신 안정판을 우선한다. 전체 Homebrew 개별 항목은 [전체 패키지 목록](02-package-catalog.md)에 있다.

## 설치 정책과 순서

1. 새 Mac에서 Apple 개발 도구와 Homebrew를 준비한다. Homebrew 설치는 공식 안내에서 현재 설치 절차를 가져온다.
2. 아래 직접 사용 도구 중 계속 사용할 항목만 최신판으로 설치한다. 의존성 156종은 일괄 수동 설치하지 않는다.
3. Java는 SDKMAN, Node는 nvm, Python 인터프리터는 pyenv, Python 환경·패키지는 uv로 구성한 뒤 전역 도구를 재설치한다. Ruby는 기존 별도 계획을 따른다.
4. 프로젝트는 소스와 잠금 파일, 사용자 설정을 옮긴다. 기존 Cellar·node_modules·Python 가상환경·Ruby 바이너리는 새 Mac용으로 다시 만든다.

Homebrew 공식 안내 URL은 https://brew.sh/ 이며 이 조사에서는 웹을 열람하지 않았다. Apple 도구 준비 명령은 `xcode-select --install`이다. 두 명령 모두 이 조사에서는 실행하지 않았다.

## Homebrew의 직접 설치 도구

영수증 기준 직접 설치 Formula는 47종이다. 최신판 우선 목록에서는 구형 `p7zip`을 `sevenzip`으로 통합하고 `python@3.9`를 최신 `python`으로 바꾼다. 아래는 카테고리별 설치 예시다. shell·언어 관리자를 여러 개 쓸 필요가 없다면 필요한 것만 선택한다.

### 터미널과 파일 도구

```sh
brew install eza fd fish fzf lsd ripgrep stow tree yazi zoxide zsh-syntax-highlighting
brew install --cask ghostty
brew install herdr
```

1. 기본 shell을 zsh로 유지할지 fish로 사용할지 정한다.
2. 위 목록에서 사용할 도구를 설치한다.
3. shell 설정과 키 바인딩을 옮긴다. `fish` 설치만으로 로그인 shell 변경이 완료되는 것은 아니다.
4. `stow`를 쓴다면 dotfiles 원본 저장소를 새 Mac 경로에 두고 연결을 새로 만든다.

Ghostty와 Herdr는 사용자 확정 설치 대상이다. tmux는 설치하지 않으며 `.tmux.conf`·tmux 플러그인·자동 attach 설정을 복원하지 않는다. fzf 패키지가 제공하는 `fzf-tmux` 파일의 존재는 tmux 설치 요구가 아니며 일반 fzf 기능을 사용한다.

### 코드와 개발 보조

```sh
brew install ast-grep biome gh jq kotlin-language-server mdq neovim yq
brew install lazygit
```

1. 최신 도구를 설치한다.
2. Neovim 설정과 프로젝트별 formatter/linter 설정을 옮긴다.
3. `gh`·Gemini 등 계정 기반 도구는 새 Mac에서 다시 로그인한다.
4. 프로젝트의 로컬 개발 의존성 버전은 해당 프로젝트 잠금 파일을 따른다.

lazygit의 기존 관측 tap은 `jesseduffield/lazygit`이다. 새 설치는 현재 upstream README의 `brew install lazygit`으로 통일한다. Yazi·Neovim·lazygit은 [통합 작업 구성](13-workflow-orca-paseo-herdr.md)의 공통 필수 도구다.

Gemini CLI는 최신 기본 설치 목록에서 제외한다. 2026-09-06 [Homebrew 공식 API](https://formulae.brew.sh/api/formula/gemini-cli.json)는 `deprecated: true`, 사유 `unsupported`, 대체 cask `antigravity-cli`를 기록한다. 새 Mac에서 이 AI 도구를 계속 사용할 때는 [최신 공식 출처와 예외](09-official-sources.md)를 따라 대체 도구의 현재 설치 안내와 설정 이전 범위를 확인한 뒤 `brew install --cask antigravity-cli`를 사용한다. 기존 Gemini CLI 설정이 자동 호환된다고 가정하지 않는다.

### 터미널 앱 설치 예외

Alacritty는 2026-09-06 읽은 [Homebrew 공식 API](https://formulae.brew.sh/api/cask/alacritty.json)에서 `disabled: true`, 사유 `fails_gatekeeper_check`로 표시된다. `brew install --cask alacritty`를 기본 설치 절차로 실행하지 않는다. [공식 프로젝트](https://github.com/alacritty/alacritty/)의 현재 macOS 배포 안내를 따르거나 기존에 사용하는 Ghostty 같은 터미널을 먼저 설치한다. 이 문서는 Gatekeeper 우회 명령을 제시하지 않는다.

Orca는 `brew install --cask stablyai/orca/orca`처럼 tap을 명시한다. 같은 이름의 기본 cask를 선택하면 다른 제품을 설치할 수 있다.

### 네트워크와 보안

```sh
brew install age httpie mkcert sops telnet wget
```

1. 실제 쓰는 도구만 최신판으로 설치한다.
2. 일반 설정을 옮긴다.
3. age/SOPS 개인키와 mkcert 로컬 CA는 일반 설정과 별도로 안전한 경로로 이전하거나 새로 발급한다.
4. 새 Mac의 키체인·신뢰 설정은 해당 도구의 설치 안내를 따라 적용한다.

개인키 내용이나 인증 토큰은 이 문서에 포함하지 않았다. telnet은 관측 도구이며 평문 접속이 필요한 기존 작업이 있을 때만 추가한다.

### 미디어·문서·압축

```sh
brew install ffmpeg imagemagick sevenzip poppler wimlib yt-dlp
```

1. 위 도구 중 실제 작업에 필요한 도구를 설치한다.
2. 기존 변환 스크립트와 사용자 preset을 옮긴다.
3. p7zip에 의존하던 스크립트는 sevenzip이 제공하는 실행 명령 이름에 맞춰 사용한다.

### 언어와 빌드 기반

```sh
brew install ruby gradle mingw-w64 libtensorflow
brew install oven-sh/bun/bun
brew install spring-io/tap/spring-boot
```

Java는 SDKMAN, Node는 nvm을 사용한다. Python 관리 계획을 포함한 상세 단계는 [런타임 관리자 설치](11-runtime-managers.md)를 우선한다. 기존 `python@3.9`·`openjdk@21`은 기본 일괄 설치 대상이 아니다. gradle/spring-boot 등의 의존성으로 Homebrew JDK·Python·Node가 추가될 수 있지만 기본 개발 런타임 선택과 구분한다.

Python 인터프리터 관리자는 `brew install pyenv`로 준비한다. 가상환경은 uv가 관리하므로 pyenv-virtualenv를 추가하지 않는다. Ruby·Rust 관리자는 필요한 경우 `brew install rbenv rustup`으로 준비한다. Rust의 도구 체인은 Rustup 설치 안내에 따라 stable을 선택한다. 현재 `~/.cargo`는 없었고 이전할 Cargo 전역 패키지 목록은 확인되지 않았다.

## npm 전역 도구

현재 PATH의 npm은 `~/.local/bin/npm → ~/.hermes/node/bin/npm`이다. `npm list --global --depth=0 --json`은 `~/.local/lib`의 패키지 두 개만 표시했다. 별도로 `/opt/homebrew/lib/node_modules`에도 패키지가 있어 한 명령의 출력이 전체 설치 흔적을 대표하지 않는다.

아래 URL은 각 `package.json`의 homepage/repository에서 추출했다. 웹 열람 없음. 버전은 관측값이고 명령은 최신판 설치용이다.

| 도구 | 관측 버전 | 최신 설치 명령 | 공식 메타데이터 URL | 설치 근거 |
|---|---|---|---|---|
| Codex | 0.153.4 | `npm install -g @openai/codex` | https://github.com/openai/codex | `~/.local/lib/node_modules/@openai/codex/package.json` |
| Mermaid CLI | 11.16.0 | `npm install -g @mermaid-js/mermaid-cli` | https://github.com/mermaid-js/mermaid-cli | `~/.local/lib/node_modules/@mermaid-js/mermaid-cli/package.json` |
| n | 9.2.3 | 이전 제외; nvm 사용 | https://github.com/tj/n | `/opt/homebrew/lib/node_modules/n/package.json` |
| Yeoman | 5.0.0 | `npm install -g yo` | http://yeoman.io | `/opt/homebrew/lib/node_modules/yo/package.json` |
| JHipster generator | 8.5.0 | `npm install -g generator-jhipster` | https://www.jhipster.tech/ | `/opt/homebrew/lib/node_modules/generator-jhipster/package.json` |
| oh-my-claude-sisyphus | 4.14.6 | `npm install -g oh-my-claude-sisyphus` | https://github.com/Yeachan-Heo/oh-my-claudecode | `/opt/homebrew/lib/node_modules/oh-my-claude-sisyphus/package.json` |
| Z.AI coding-helper | 0.0.7 | `npm install -g @z_ai/coding-helper` | https://docs.z.ai/ | `/opt/homebrew/lib/node_modules/@z_ai/coding-helper/package.json` |
| Google Jules | 0.1.30 | `npm install -g @google/jules` | https://jules.google | `/opt/homebrew/lib/node_modules/@google/jules/package.json` |
| CodeGraph npm 배포본 | 1.0.1 | `npm install -g @colbymchenry/codegraph` | 미확인 | `/opt/homebrew/lib/node_modules/@colbymchenry/codegraph/package.json` |

1. 새 Mac에서 nvm으로 기본 Node를 설치한다. 전역 패키지는 nvm의 해당 Node 설치 경로를 사용하며 별도 npm prefix를 설정하지 않는다. 기존 Hermes 전용 Node를 통째로 복사하지 않는다.
2. 위 도구 중 계속 사용할 패키지에 대해 명령을 실행한다. `n`은 복원하지 않는다. nvm의 Node 버전마다 전역 패키지가 분리됨에 유의한다.
3. 도구별 사용자 설정을 옮기고 계정 연동을 새로 수행한다.
4. CodeGraph는 npm판 1.0.1, 독립판 v1.2.0, omo 플러그인 내장판이 함께 관측되므로 사용할 배포 경로를 먼저 정한다.

위 npm 이름은 로컬 관측 이름이다. 특히 oh-my-claude-sisyphus는 repository 이름이 oh-my-claudecode와 다르므로 새 설치 시 해당 프로젝트의 현재 설치 안내에서 이름을 정한다. 여기서는 외부 최신 이름을 확정하지 않았다.

추가 내장 패키지: `/opt/homebrew/lib/node_modules/npm` 11.16.0, `~/.hermes/node/lib/node_modules/npm` 10.9.8, 같은 Hermes 경로의 `corepack` 0.34.6. npm은 새 Node 설치에 맞춰 제공되는 버전을 사용한다. Corepack은 프로젝트가 pnpm/Yarn 관리에 필요로 할 때만 `npm install -g corepack`으로 최신판을 추가한다. 공식 메타데이터 URL은 각각 https://docs.npmjs.com/ 및 https://github.com/nodejs/corepack 이다.

## Python·pipx·uv·Poetry

로컬 영수증 `~/.local/pipx/venvs/*/pipx_metadata.json`에서 직접 도구 두 종을 확인했다.

| 도구 | 관측 버전 | 기존 경로 | 최신 설치 예시 | 공식 URL |
|---|---|---|---|---|
| uv | 0.6.14 | `~/.local/pipx/venvs/uv` | 공식 독립 설치자; 11 문서 참고 | https://docs.astral.sh/uv |
| Poetry | 2.1.1 | `~/.local/pipx/venvs/poetry` | `uv tool install poetry` | https://python-poetry.org/ |

두 URL은 각 venv 안 `lib/python3.13/site-packages/<패키지>-<버전>.dist-info/METADATA`에서 확인했다. uv는 기존 pipx 설치를 재현하지 않고 최신 독립 설치자를 사용한다. [확정 설치 계획](11-runtime-managers.md)의 pyenv·uv 역할 분담이 우선한다.

1. 최신 Python은 pyenv로 설치하고 uv는 독립 실행 파일로 준비한다.
2. Poetry가 필요한 프로젝트가 있다면 pyenv 인터프리터를 지정한 `uv tool install --python "$(pyenv which python)" poetry`로 최신 도구를 설치한다.
3. 프로젝트의 pyproject.toml과 잠금 파일을 옮기고 프로젝트 가상환경은 새 Mac에서 다시 만든다.
4. pipx는 이번 기본 설치 대상에서 제외한다. uv 설정의 `python-preference = "only-system"`, `python-downloads = "never"`와 명시적 pyenv 인터프리터 지정으로 역할을 분리한다.

`uv tool list`는 캐시 접근 권한 오류로 목록을 반환하지 못했다. 대신 `~/.local/share/uv/tools`를 읽었고 .gitignore와 .lock만 있으며 도구 환경 디렉터리는 없었다. `~/.local/bin/python3.11`은 uv 관리 Python 디렉터리로 연결되어 있다. 이것만으로 Python 3.11이 새 Mac의 필수 버전이라고 판단하지 않는다.

`bun pm ls -g`는 AccessDenied였고 기본 `~/.bun/install/global` 디렉터리는 없었다. 따라서 Bun 전역 도구가 없다고 절대 단정하지 않으며 기본 경로에 설치 목록이 확인되지 않았다고 기록한다.

## Ruby·Bundler·CocoaPods·Jekyll

`~/.rbenv/versions/3.1.4`가 있고 활성 `gem list --local`에 아래 주요 도구가 있다. 직접 설치 여부는 RubyGems 목록만으로 구분하지 않았다.

| 도구 | 관측 버전 | 최신 설치 명령 | 공식 URL |
|---|---|---|---|
| Bundler | 2.6.2 및 기본 2.3.26 | `gem install bundler` | https://bundler.io |
| CocoaPods | 1.16.2 | `gem install cocoapods` | https://github.com/CocoaPods/CocoaPods |
| Jekyll | 4.3.4 | `gem install jekyll` | https://jekyllrb.com |

공홈·버전 근거는 `~/.rbenv/versions/3.1.4/lib/ruby/gems/3.1.0/specifications/{bundler-2.6.2,cocoapods-1.16.2,jekyll-4.3.4}.gemspec`이다.

1. 새 Mac의 Ruby를 최신 안정판으로 준비한다. 프로젝트의 .ruby-version이 있는 경우 해당 프로젝트에만 명시된 버전을 추가한다.
2. 사용하는 전역 도구만 위 명령으로 설치한다.
3. Gemfile·Gemfile.lock·Podfile·Podfile.lock을 프로젝트와 함께 옮긴다.
4. 기존 gem 바이너리를 복사하지 않고 프로젝트 의존성은 각 프로젝트의 설치 절차로 다시 만든다.

기본 gem과 CocoaPods/Jekyll의 전이 의존성을 모두 전역 수동 설치하지 않는다. 관측된 주요 의존성은 activesupport 7.2.2.1, cocoapods-core 1.16.2, xcodeproj 1.27.0, jekyll-sass-converter 3.0.0, jekyll-watch 2.2.1, kramdown 2.5.1, rouge 4.5.1, sass-embedded 1.83.1이다. 이 버전들은 재현 목표가 아니다.

## 사용자 실행파일과 수동 설치 흔적

근거: `ls -la ~/.local/bin`. 아래 버전은 링크 경로에 포함된 값이며 실행해서 확인한 버전은 아니다.

| 실행파일 | 관측 연결 또는 흔적 | 이전 방법 |
|---|---|---|
| claude | `~/.local/share/claude/versions/2.1.207` | Claude Code의 현재 공식 설치 경로로 최신판을 재설치하고 사용자 설정을 옮긴다. |
| aside | `~/.aside/cli/Aside CLI.app/Contents/MacOS/aside` | Aside 앱/CLI를 새로 설치해 링크를 생성한다. |
| codegraph | `~/.codegraph/versions/v1.2.0/bin/codegraph` | 독립판을 계속 쓸 경우 해당 배포 경로에서 최신판을 설치한다. npm판·omo판과 실행 우선순위를 정한다. |
| agy | 약 143MB 독립 실행파일 | 설치 출처·버전 미확인. 관련 앱 또는 배포처를 먼저 식별한 뒤 재설치한다. |
| moai | 독립 실행파일 및 날짜 숫자 backup 4개 | 원래 배포처에서 최신판을 설치한다. backup 바이너리들은 기본 이전 대상에서 제외한다. |
| sensai | 독립 실행파일 | 설치 출처·버전 미확인. 소스 프로젝트 또는 릴리스 배포처를 먼저 식별한다. |
| hermes | 118바이트 실행 래퍼 | Hermes 본체를 설치한 뒤 새 Mac의 경로에 맞게 래퍼를 복원한다. |
| node/npm/npx | `~/.hermes/node/bin` 연결 | 새 Node 관리 방식을 정하고 PATH를 구성한다. 기존 링크만 복사하면 대상이 없다. |
| omo 및 omo-* | omo 4.19.4 캐시 하위 CLI 링크 | 플러그인을 현재 지원 설치 경로로 재설치한다. 캐시 절대경로 링크는 복사하지 않는다. |
| ulw/ulw-loop/lazycodex-executor-verify | 같은 omo 캐시 하위 CLI 링크 | omo 재설치에서 제공하는 실행 경로를 사용한다. |
| spring-create | `~/Workspace/Personal/Traning/spring-creator/spring-create` | 원본 프로젝트를 같은 상대 구조로 옮기거나 새 경로로 링크를 다시 만든다. |
| spring-creator | `~/Workspace/Personal/Traning/spring-creator2/spring-creator.sh` | 원본 프로젝트를 복원하고 새 경로로 링크를 다시 만든다. |
| poetry/uv/uvx | pipx venv 실행파일 연결 | 위 Python 도구 절의 선택한 설치 방식으로 다시 생성한다. |
| argcomplete 관련 3종/userpath | 작은 Python 실행 스크립트 | 필요 기능을 제공하는 패키지를 새 Python 환경에 설치하여 다시 생성한다. |

설치 출처를 확인하지 못한 로컬 바이너리의 공홈 URL이나 curl 설치 명령은 추측해서 만들지 않았다. 후속 조사에서 agy의 공식 설치 경로는 확인하여 [앱 CLI 문서](06-app-cli-custom.md)에 기록했다. spring-create와 spring-creator는 링크 대상 파일이 현재 없으므로 원본 확보 전 이전 보류다. sensai 등 나머지 미확인 항목은 배포처가 식별되어야 설치 명령이 확정된다.

## 읽기 근거와 범위

- Homebrew: `/opt/homebrew/Cellar/*/*/INSTALL_RECEIPT.json`, 각 버전의 `.brew/*.rb`, `/opt/homebrew/Caskroom/*/.metadata/INSTALL_RECEIPT.json`, Casks 정의, 로컬 tap.
- 전역 JavaScript: `npm list --global --depth=0 --json`와 세 개 prefix의 package.json.
- Python: pipx 영수증·패키지 METADATA·uv 도구 디렉터리.
- Ruby: 활성 환경의 `gem list --local`와 주요 도구 gemspec.
- 수동 설치: 사용자 실행파일 목록과 심볼릭 링크 대상.

Homebrew의 일반 목록 API는 bun·spring-boot를 누락하고 lazygit tap 및 sdl2 이름을 현재 정의로 표시하는 차이가 있었다. 따라서 전체 설치 수와 설치 출처는 Cellar 영수증을 우선했다. Caskroom의 docker/flutter는 디렉터리 버전과 영수증 source.version이 달라 두 관측값을 별도로 기록했다. Gemini CLI와 Alacritty의 공식 API는 추가로 열람해 위 예외에 반영했다. 전체 공식 조회 결과는 [최신 공식 출처](09-official-sources.md)를 우선하며 모든 패키지의 새 macOS 호환성을 조사한 것은 아니다.
