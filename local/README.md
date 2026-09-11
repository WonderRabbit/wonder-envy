# 로컬 개발 환경 적용 결과

## Fish·Catppuccin·lsd 후속 적용 (2026-09-11)

macOS 로그인 셸·Terminal·Ghostty·Herdr의 기본값을 Fish로 변경했다. nvm·SDKMAN은 Bass로 Fish와 연동하며 Node·Python·Java·uv 통합 검증을 통과했다. lsd 1.2.0을 설치하고 지원 CLI에 Catppuccin Mocha를 적용했다. 자세한 [사용법·테마·복구](../menual/fish-and-themes.md), [계획 16](../.omo/plans/mac-mini-migration/16-fish-catppuccin-lsd.md), [체크리스트](INSTALL-CHECKLIST.md)를 참고한다.

## 추가 설치 반영 (2026-09-11)

최신 상태는 [설치 체크리스트](INSTALL-CHECKLIST.md), 사용법은 [menual](../menual/README.md)을 기준으로 한다. LazyVim·tree-sitter-cli·Worktrunk·Atuin·mise·Hurl·lnav·difftastic을 설치했다. 아래 기본 환경 기록 중 최소 Neovim 구성은 이제 LazyVim으로 대체되었다.

Neovim 원본은 `local/nvim/`, 실제 설정은 `~/.config/nvim`이다. `apply-config.py`는 전체 Neovim 덮어쓰기를 하지 않고, 선택한 colorscheme 플러그인 설정과 셸·도구·테마 파일을 관리한다. 새 설정은 Atuin, mise Fish activation 차단, Worktrunk Fish autoload·completion이다.

LazyVim 전환 백업은 `~/.local/state/wonder-envy/backups/lazyvim-20260911-130603/`에 있다. Fish의 mise 자동 activation과 중첩 로그인 Zsh의 Java 경로 순서 문제를 수정했다. GitHub SSH 인증 계정의 noreply identity를 저장소 로컬 설정으로 추가했으며 전역 identity는 바꾸지 않았다.


적용일: 2026-09-11. 대상은 macOS 26.6.2 / Apple Silicon, 홈은 `/Users/sophi`, 저장소는 `/Users/sophi/Workspace/Projects/wonder-envy`다. `.omo/plans/mac-mini-migration.md`와 07·11·12·13의 확정 사항을 우선 적용했다. 과거 조사 문서의 설치 금지 문구는 조사 당시 범위로 보존하고, 이번 사용자의 실제 설정 요청에 따라 설치했다.

공통 개발 환경의 설치와 설정은 완료했다. 모든 이전 데이터와 선택적 SDK까지 복원한 상태는 아니다. 아래 잔여 항목을 완료해야 전체 장치 이전이 끝난다.

## 설치 및 연결

| 영역 | 실제 상태 |
| --- | --- |
| 기반 | 기존 Apple Command Line Tools·Homebrew 사용, Homebrew 메타데이터 갱신 |
| Node | 공식 nvm 0.40.7, Node 26.8.2, npm 11.19.1, 기본 별칭 `node` |
| Python | Homebrew pyenv, CPython 3.14.7을 소스 빌드하고 전역 기본값으로 선택 |
| Python 환경 | 독립 uv 0.12.13, `only-system`·`python-downloads = "never"` 적용 |
| Java | SDKMAN 5.23.0, Temurin `26.0.2-tem` 설치 및 기본값 지정 |
| Bash | SDKMAN 설치자가 Bash 4 이상을 요구하여 Homebrew Bash 5.3.15 추가 |
| 터미널 | 기존 Ghostty 1.3.1·Herdr 0.9.0 사용, JetBrainsMono Nerd Font 설치 |
| 셸 | Fish 4.9.3, Oh My Posh 31.2.1; 로그인 셸은 Fish로 변경 |
| 편집 및 Git | Neovim 0.12.5, 기존 Yazi 26.9.1·lazygit 0.65.0, gh 2.100.0으로 갱신 |
| Python CLI | pyenv Python을 지정해 uv tool로 Poetry 2.4.3, IPython 9.17.1, Pygments 2.21.0 설치 |
| AI CLI | nvm npm의 Codex 0.154.0·OpenCode 1.18.30, 네이티브 stable Claude Code 2.1.236 |
| OMO | `npx lazycodex-ai install --no-tui --no-codex-autonomous`, 플러그인 4.19.4·12개 역할 파일·관리 CLI 설치 |
| OMC | Claude 공식 marketplace 명령으로 `oh-my-claudecode@omc` 5.3.0 설치·활성화 |
| Herdr 연결 | Codex v8, Claude v9, OpenCode v11 integration 설치 및 `current` 확인 |
| 앱 | Aside 1.0.910.1, VS Code 1.137.0, Antigravity CLI 1.2.0 설치 |
| Aside CLI | 브라우저와 별도로 공식 설치자 사용, CLI 1.26.906.1630 설치 |
| Orca·Paseo | 기존 Orca 1.4.192·Paseo 0.7.2 유지, 앱 번들 CLI를 `~/.local/bin`에 연결 |
| Docker | 공식 Docker Desktop 4.90.0 DMG 설치, Docker CLI 29.7.2·Compose 5.5.1·Buildx 0.36.1 연결 |

Homebrew 공통 설치 목록은 [Brewfile](Brewfile)에 있다. eza·fd·fzf·stow·tree·zoxide·jq·sevenzip·Poppler·resvg와 Python 빌드 의존성도 포함한다. tmux·Alacritty·Gemini CLI·옛 Hermes Node 링크는 설치하지 않았다.

기존 Orca·Paseo 앱은 이 작업에서 업데이트하거나 별도 daemon을 추가하지 않았다. OMO의 현재 플러그인 설정에서 Context7은 활성, Codegraph·git_bash MCP는 비활성이며 설치자 선택을 유지했다. 설치된 MCP의 로컬 파일 경로 존재는 확인했지만 서버 연결이나 OMO QA를 실행한 것은 아니다.

## 사용 방법

새 터미널은 Fish와 Oh My Posh를 사용한다. Node·Java·Python 작업을 Fish에서 직접 실행한다. Herdr의 새 pane도 로그인 Fish로 시작한다.

```sh
cd ~/Workspace/Projects/wonder-envy
herdr
```

| 명령 | 동작 |
| --- | --- |
| `dev` | 새 로그인 Fish 시작; 일반 개발에는 전환 불필요 |
| `y` | Yazi 실행 후 선택한 디렉터리로 부모 셸 이동 |
| `nvim` 또는 `vim` | Neovim 실행 |
| `lg` | lazygit 실행 |
| Neovim `Space`, `g`, `g` | LazyVim에서 프로젝트 lazygit 열기 |
| `ll` | lsd로 숨김 파일을 포함한 상세 목록 |
| `nvm use` / `sdk env` | 해당 프로젝트의 버전 선언을 명시적으로 적용 |

Orca/Paseo에서 선택한 실제 저장소·worktree 경로를 Herdr에서도 사용한다. 앱이 만든 worktree는 해당 앱에서 관리한다. 새 GUI 프로세스가 이미 실행 중인 앱의 PATH를 갱신하지는 않으므로, CLI를 찾지 못하는 앱은 재시작하거나 Fish에서 실행한다. nvm·SDKMAN은 Bash 환경 변경을 Fish로 전달하는 함수를 사용한다.

새 Python 환경은 실제 pyenv 인터프리터를 지정한다.

```sh
uv venv --python (pyenv which python)
# uv.lock이 있는 기존 프로젝트에서:
uv sync --locked
```

기존 프로젝트의 `.nvmrc`, `.python-version`, `.sdkmanrc`, 잠금 파일은 변경하지 않았다.

## 적용한 파일과 백업

| 템플릿 | 실제 적용 위치 |
| --- | --- |
| `config/zshrc` | `~/.zshrc` |
| `config/config.fish` | `~/.config/fish/config.fish` |
| `config/uv.toml` | `~/.config/uv/uv.toml` |
| `config/herdr.toml` | `~/.config/herdr/config.toml` |
| `config/yazi.toml` | `~/.config/yazi/yazi.toml` |
| `config/ghostty` | `~/.config/ghostty/config` |
| `config/init.lua` | 과거 최소 설정 보관본; 현재 적용 제외 |

기존 `~/.zprofile`의 Homebrew 초기화는 유지했다. Git 전역 `core.editor`는 `nvim`으로 설정했다. 사용자 이름·이메일은 추측하지 않았다.

[apply-config.py](apply-config.py)는 현재 매핑된 셸·도구 템플릿을 적용한다. 동일한 파일은 건너뛰고, 다른 기존 파일은 사용자 홈의 비공개 백업 디렉터리에 보관한 후 교체한다. 설정을 이후 직접 수정했다면 재실행 전에 템플릿과 병합해야 한다.

```sh
python3 local/apply-config.py
brew bundle check --file=local/Brewfile --no-upgrade
```

백업 위치는 `~/.local/state/wonder-envy/backups/`다. 각 시각별 `manifest.json`에 새로 만든 파일과 기존 파일 여부를 구분했다. 초기 적용은 `20260911-111256-853833`, 최종 Zsh 보완은 `20260911-111554-738462`에 기록되어 있다. AI 설정은 `ai-20260911-111325`에 별도로 보관했다. 인증 파일을 저장소로 복사하지 않았다.

복구할 때 기존 파일은 원하는 시점의 사본으로 복원하고, 이번 작업에서 새로 만든 파일은 manifest를 확인한 후 제거한다. 패키지·앱·플러그인 설치는 이 파일 백업만으로 제거되지 않는다.

## Docker 설치 예외

Homebrew cask는 `/usr/local/bin`과 `/usr/local/cli-plugins`에 링크를 만들면서 관리자 암호를 요구해 롤백됐다. 동일한 공식 DMG를 읽기 전용으로 마운트해 `/Applications/Docker.app`에 복사하고 마운트를 해제했다. Docker는 Homebrew 관리 목록에 넣지 않았다.

CLI와 credential helper는 `~/.local/bin`, Compose·Buildx는 `~/.docker/cli-plugins`에서 앱 번들의 실행 파일을 가리킨다. 추후 업데이트는 Docker 앱의 업데이트 기능 또는 공식 DMG를 사용한다. 최초 앱 실행과 VM 구성·권한 안내는 사용자 화면에서 완료해야 한다. Docker daemon·컨테이너는 시작하지 않았다.

## 검증 결과

- `brew bundle check --file=local/Brewfile --no-upgrade`: 통과.
- Zsh 구문 검사 및 실제 PTY 로그인 셸 초기화: 오류 없이 통과. tty가 없는 셸에서는 fzf 키 바인딩 초기화를 생략하도록 보완했다.
- Fish 구문·대화형 초기화, `EDITOR=nvim`, `y` 함수·프롬프트 존재: 통과.
- Ghostty `+validate-config`: 통과.
- Neovim headless 시작 및 lazygit 단축키 등록: 통과. lazygit TUI 조작 전체를 검증한 것은 아니다.
- TOML 설정 파싱, AI hook JSON 파싱: 통과.
- pyenv Python으로 임시 uv 가상환경 생성, SSL·SQLite·bz2·lzma·ctypes·zlib import: 통과. tkinter 8.6 import도 확인했다.
- Node·Python·Java 경로가 각각 nvm·pyenv·SDKMAN 설치본임을 확인했다.
- 주요 CLI 버전 조회, Docker·Compose·Buildx 버전 조회: 통과.
- Herdr의 세 integration은 `current` 상태다. 설정 적용 스크립트 재실행은 변경 0건이었다.
- OMO 설치 전후 Codex의 모델·reasoning effort·approval policy·sandbox mode가 동일함을 확인했다.
- npm이 알린 comment-checker postinstall 제한은 배포본에 arm64 바이너리가 이미 포함되어 있어 기능 파일 누락이 아님을 확인했다. 패키지의 설치 스크립트로 이를 확인했으며 검사 기능은 실행하지 않았다.
- `git diff --check`: 통과. 앱 간 전체 TUI·MCP·모델 호출, OMO doctor·QA는 실행하지 않았다.

설치 로그·다운로드는 Git에서 제외한 `.local-setup/`에 있다. 이 디렉터리에는 로컬 인증 상태 조회 결과가 포함될 수 있으므로 공유하지 않는다.

## 남은 사용자·원본 자료 의존 항목

1. **로그인:** Codex는 로그인 상태다. Claude는 `claude auth login`, GitHub CLI는 `gh auth login`이 필요하다. OpenCode·Antigravity·Aside 계정 연결은 사용 시 해당 도구의 로그인 흐름을 따른다.
2. **Git identity:** 전역 이름·이메일은 미설정이며, 이 저장소에는 인증된 GitHub 계정의 noreply identity를 설정했다.
3. **기존 dotfiles:** 이전 Mac의 `~/dotfiles`와 Neovim 원본이 없다. 현재 Neovim은 새 LazyVim 구성이며 과거 사용자 LSP·플러그인·테마 전체를 복원한 상태가 아니다.
4. **사용자 자료:** SSH/GPG/age/mkcert 키, 모델, Docker volume/DB, Obsidian 자료, 대화·메모리, 미커밋 worktree는 원본 자료가 필요하다. 현재 SSH 자료는 변경하지 않았다.
5. **앱 최초 실행:** Docker 초기 설정, 필요한 앱 권한, OMO/OMC의 다음 세션 안내 및 hook 검토를 완료한다. 원격 pairing·daemon 중복 실행은 추가하지 않았다.
6. **프로젝트별 선택 설치:** Android·Flutter·Xcode 전체 SDK, Ruby/CocoaPods/Jekyll, Rust toolchain, Gradle·Spring·JHipster, 미디어 도구, 로컬 모델은 실제 프로젝트 요구와 자료를 기준으로 별도 설치한다. 과거 관측된 203개 Formula를 일괄 재현하지 않았다.

## 확인한 공식 설치 근거

- 런타임: [nvm](https://github.com/nvm-sh/nvm), [pyenv 빌드 환경](https://github.com/pyenv/pyenv/wiki), [uv 설치](https://docs.astral.sh/uv/getting-started/installation/), [SDKMAN](https://sdkman.io/install/).
- 셸·도구 설정: [Herdr](https://herdr.dev/docs/configuration/), [Yazi](https://yazi-rs.github.io/docs/configuration/yazi/), [Ghostty](https://ghostty.org/docs/config/reference), [Oh My Posh](https://ohmyposh.dev/docs/installation/prompt).
- AI 도구: [Codex CLI](https://learn.chatgpt.com/docs/codex/cli), [Claude Code](https://code.claude.com/docs/en/setup), [OpenCode](https://opencode.ai/docs/), [LazyCodex](https://github.com/code-yeongyu/lazycodex), [OMC](https://github.com/Yeachan-Heo/oh-my-claudecode).
- 앱 배포: Homebrew의 설치 시점 공식 cask 메타데이터와 [Aside 공식 CLI 설치자](https://releases.aside.com/install.sh)를 사용했다.
