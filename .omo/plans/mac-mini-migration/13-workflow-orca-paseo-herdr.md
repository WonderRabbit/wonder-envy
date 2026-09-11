# Orca·Paseo와 Herdr 기반 개발 작업 구성

## 목표와 확정 사항

2026-09-06 사용자 의도를 반영한 작업 구성 문서다. **Orca + Herdr 또는 Paseo + Herdr**를 사용하고, 파일 탐색은 Yazi, 편집은 Neovim, Git 작업은 lazygit을 중심으로 한다. 독립 터미널 앱은 Ghostty이며 tmux는 설치·복원하지 않는다.

이 문서는 설치 계획과 사용 흐름이다. 공식 문서·기존 계획·현재 Neovim 설정 파일을 읽었으며 실제 앱·TUI·에이전트·Git 명령·테스트·OMO QA는 실행하지 않았다. 아래의 조합은 권장 운영 구성이지 제품 간 전용 연동을 실행으로 입증한 결과가 아니다.

## 1. 도구별 역할

| 도구 | 담당 역할 | 함께 사용할 대상 |
| --- | --- | --- |
| Orca | 프로젝트·worktree·에이전트 작업과 변경 내역 관리 | Herdr·Yazi·Neovim·lazygit |
| Paseo | daemon 기반 프로젝트·에이전트 관리, 필요 시 다른 장치에서 접근 | Herdr·Yazi·Neovim·lazygit |
| Ghostty | 독립 macOS 터미널 화면과 입력 | Fish·Zsh·Herdr |
| Herdr | 터미널 workspace·tab·pane, 직접 실행한 에이전트의 터미널 세션 | Yazi·Neovim·lazygit·셸 |
| Yazi | 파일·폴더 탐색, 미리보기, 편집기로 파일 열기 | Neovim |
| Neovim | 코드·문서 편집, 기존 LSP·플러그인 환경 | pyenv·uv·nvm·SDKMAN, lazygit |
| lazygit | 변경 확인, staging·commit·branch 등 Git 작업 | 현재 작업 중인 동일 저장소·worktree |
| Fish·Oh My Posh | 일상 대화형 셸·프롬프트 | Ghostty·Herdr |
| Zsh | nvm·SDKMAN의 공식 지원 셸 기반 개발 환경 | Java·Node 작업 및 에이전트 실행 |

Orca와 Paseo를 모두 설치할 수 있지만 **한 작업의 프로젝트·worktree·에이전트 관리는 어느 앱이 맡는지 구분**한다. 다른 앱의 작업 상태·세션 ID가 자동 공유된다고 가정하지 않는다.

## 2. 조합 A: Orca + Herdr

### 기본 사용 흐름

1. Orca에서 저장소 또는 작업할 worktree를 선택한다.
2. Orca가 표시하는 실제 작업 디렉터리를 기준으로 터미널을 연다.
3. 그 디렉터리에서 Herdr를 열어 파일 탐색·편집·Git용 pane을 구성한다.
4. Yazi로 파일을 탐색하고 Neovim으로 편집한다.
5. lazygit은 같은 디렉터리에서 실행해 해당 작업의 변경을 다룬다.
6. Orca의 에이전트 탭과 변경 화면에서 작업을 이어간다. 동일 파일을 사람이 편집할 때 에이전트의 동시 수정과 조율한다.

[Orca 공식 터미널 문서](https://www.onorca.dev/docs/terminal)는 터미널 탭·분할과 TUI 사용을 설명한다. Ghostty 설정 가져오기는 테마·폰트·커서 등에 관한 기능이며 Orca 터미널이 Ghostty 프로세스 그 자체라는 뜻은 아니다.

### Ghostty를 별도 사용하는 방식

Orca와 Ghostty를 나란히 열고 Ghostty의 Herdr에서 같은 **실제 worktree 디렉터리**로 이동할 수도 있다. 이 경우 파일과 Git 상태는 같은 디렉터리를 통해 공유하지만 Orca의 터미널 탭과 Herdr pane은 별도 세션이다.

기본 역할 분담은 Orca가 작업 폴더·에이전트를 관리하고 Herdr는 그 폴더 안의 수동 도구 공간을 관리하는 방식이다. Orca에서 생성한 worktree를 Herdr가 다시 생성·삭제·이동하도록 구성하지 않는다. [Orca worktree 공식 설명](https://www.onorca.dev/docs/model/worktrees)

Herdr에서 Codex·Claude를 직접 시작하는 방식도 별도 운영 선택이다. 그 프로세스가 Orca의 에이전트 카드·재개 기능에 자동 편입된다고 가정하지 않는다. 기본 구성에서는 Orca가 관리할 에이전트는 Orca에서 시작한다.

## 3. 조합 B: Paseo + Herdr

### 기본 사용 흐름

1. Mac mini의 Paseo 앱 또는 headless daemon 중 선택한 운영 경로를 준비한다.
2. Paseo에서 저장소와 workspace를 선택한다. 기존 폴더 사용인지 별도 Git worktree인지 구분한다.
3. Ghostty를 열고 **daemon이 실행되는 Mac mini의 해당 작업 경로**로 이동한다.
4. Herdr 안에 Yazi·Neovim·lazygit 작업 공간을 구성한다.
5. Paseo가 관리하는 에이전트는 Paseo에서 시작하고, Herdr는 파일 탐색·수동 편집·Git 작업에 사용한다.
6. 모바일·웹·다른 데스크톱에서 Paseo에 연결하더라도 명령·에이전트는 daemon 호스트에서 실행된다는 점을 유지한다.

Paseo의 local workspace와 Git worktree는 공식 문서에 구분되어 있다. [Workspace 안내](https://paseo.sh/docs/workspaces), [Git worktree 안내](https://paseo.sh/docs/worktrees)

### 터미널과 원격 세션의 경계

Paseo의 터미널 화면을 Herdr 실행 화면으로 쓰는 경우에도 중첩 TUI의 키 입력·화면·이미지 미리보기 지원은 이번에 시험하지 않았다. 기본 구성은 별도 Ghostty + Herdr이며, Paseo의 프로젝트 경로와 맞추는 방식이다.

Paseo의 모바일 접속은 Paseo가 관리하는 작업에 대한 접근이다. 별도로 열린 Herdr 세션 전체가 Paseo에 자동 노출되는 기능으로 설명하지 않는다. Herdr를 통해 직접 시작한 에이전트를 Paseo에서도 다루려면 해당 세션의 별도 지원 경로가 있어야 하며, 이번 자료에서는 자동 흡수 근거를 확보하지 않았다.

Paseo가 만든 worktree는 Paseo를 생성·정리 주체로 유지한다. Herdr나 lazygit에서 해당 폴더를 별도로 제거하는 흐름을 기본값으로 두지 않는다. 앱과 별도 daemon을 같은 홈·포트로 중복 운영하지 않는 설치 원칙은 [12 문서](12-fish-posh-herdr-aside-paseo.md)를 따른다.

## 4. Herdr 작업 공간 배치

권장하는 최소 배치는 다음과 같다. 고정 단축키나 자동 배치 스크립트를 이번에 만들지는 않는다.

| 작업 공간 | 주 용도 | 실행할 도구 |
| --- | --- | --- |
| 탐색·편집 | 파일 선택 후 편집, 편집 종료 후 탐색으로 복귀 | Yazi → Neovim |
| Git | 변경 파일·diff·staging·branch 관리 | lazygit |
| 개발 셸 | 런타임 전환과 필요 명령 입력 | Zsh 또는 Fish |

작은 화면에서는 pane을 계속 분할하기보다 tab으로 나누는 운영안을 쓴다. Yazi에서 Neovim을 blocking opener로 열면 같은 pane에서 교대로 사용할 수 있다. [Yazi opener 공식 설명](https://yazi-rs.github.io/docs/configuration/yazi/#opener)

Herdr는 detach해도 서버와 pane이 계속 실행될 수 있으므로 창 닫기와 작업 종료를 구분한다. 세션 정리는 사용 중인 에이전트·편집기 작업을 마친 뒤 수행한다. tmux 세션·플러그인을 Herdr로 복사하는 단계는 없다. [Herdr 공식 빠른 시작](https://herdr.dev/docs/quick-start/)

## 5. 필수 설치 목록과 순서

새 Mac에서 나중에 사용할 설치 명령이다. 현재 장치에서는 실행하지 않았다.

```sh
brew install --cask ghostty
brew install herdr yazi neovim lazygit
```

Orca는 `brew install --cask stablyai/orca/orca`, Paseo 앱은 `brew install --cask paseo`를 사용한다. 둘의 설치 가이드는 [06](06-app-cli-custom.md)과 [12](12-fish-posh-herdr-aside-paseo.md)에 있다.

lazygit은 기존 관측에서 별도 tap을 사용했지만, 새 설치는 [공식 README의 Homebrew 명령](https://github.com/jesseduffield/lazygit#homebrew)인 `brew install lazygit`으로 통일한다. 같은 CLI를 두 tap에서 중복 설치하지 않는다. Neovim도 [공식 Homebrew 설치](https://neovim.io/doc/install/)를 사용하며 nightly·HEAD를 기본으로 하지 않는다.

Yazi의 최신 공식 설치 예시에는 다양한 미리보기용 선택 의존성이 포함된다. 현재 이전 목록의 fd·ripgrep·fzf·zoxide·jq·7-Zip·Poppler·FFmpeg·ImageMagick 등과 대조하여 필요한 항목만 추가한다. resvg는 SVG 미리보기가 필요할 때 추가한다. 최신 문서의 `ffmpeg-full`·`imagemagick-full`과 기존 기본 패키지는 동일한 설치 항목으로 간주하지 않으며 강제 link/overwrite를 일괄 실행하지 않는다. [Yazi 공식 설치](https://yazi-rs.github.io/docs/installation/)

## 6. Yazi → Neovim 연결

### 기본 편집기

Fish의 사용자 설정에 아래 값을 반영한다.

```fish
set -gx EDITOR nvim
set -gx VISUAL nvim
```

Zsh에서는 아래 문법을 사용한다.

```sh
export EDITOR=nvim
export VISUAL=nvim
```

Yazi `yazi.toml`의 edit opener가 사용자 편집기를 쓰도록 연결한다. 조회한 최신 공식 문법의 예시는 다음과 같다.

```toml
[opener]
edit = [
    { run = "nvim %s", block = true, for = "unix" },
]
```

현재 공식 문서는 파일 인자로 `%s`를 설명한다. 과거 버전의 `$@` 예시와 혼합하지 않는다. 기존 `[open]` 규칙이 text·소스 파일을 `edit`로 연결하는지 설정 내용을 기준으로 맞춘다. 모든 파일을 무조건 편집기로 여는 wildcard 규칙은 추가하지 않는다. [Yazi 설정 근거](https://yazi-rs.github.io/docs/configuration/yazi/)

Yazi 종료 후 탐색한 폴더로 부모 셸도 이동하려면 공식 `y` 셸 wrapper가 필요하다. 일반 `yazi` 실행 자체와 구분한다. 기존 Zsh `y` 함수는 관측되었지만 Fish에는 [공식 빠른 시작](https://yazi-rs.github.io/docs/quick-start/)의 Fish용 wrapper를 따로 반영한다.

보관할 자료는 `~/.config/yazi/yazi.toml`, `keymap.toml`, `theme.toml`과 사용자 플러그인이다. 이미지·PDF 미리보기는 터미널과 중간 multiplexer 지원에 영향을 받으므로 Ghostty 단독·Orca 터미널·Herdr 중첩에서 동일하게 보인다고 단정하지 않는다.

## 7. Neovim과 lazygit 연결

### 기존 명시 여부

lazygit은 이미 01의 개발 도구 목록, 02의 개별 패키지, 03의 전용 절에 포함되어 있다. 이번에는 현재 파일 `~/.config/nvim/lua/oneyoon/plugins/lazygit.lua`도 직접 읽었다.

| 현재 설정 선언 | 의미 |
| --- | --- |
| `kdheepak/lazygit.nvim` | Neovim에서 lazygit을 여는 플러그인 |
| `nvim-lua/plenary.nvim` | 해당 설정의 의존성 |
| `LazyGit` 등 명령 | lazy loading 대상 명령 |
| `<leader>lg` → `LazyGit` | 기존 사용자 단축키 |

이는 설정 선언 확인이며 플러그인 설치·명령 실행 성공을 확인한 것은 아니다. leader 키의 실제 문자값도 이 파일만으로 확정하지 않는다.

### 새 Mac 적용 순서

1. Neovim과 **lazygit 실행 파일 둘 다** 설치한다. Neovim 플러그인만 복원해서 CLI 설치가 끝났다고 판단하지 않는다.
2. `~/.config/nvim`의 사용자 설정·`lazy-lock.json`을 보관하고 최신 Neovim에 맞춰 플러그인 구성을 복원한다.
3. 기존 `lazygit.nvim` 연결과 `<leader>lg`를 유지한다. 필요하면 Herdr의 별도 Git pane에서도 `lazygit`을 사용할 수 있다.
4. Neovim의 작업 디렉터리가 현재 선택한 worktree를 가리키도록 한다. 파일은 다른 worktree에 열고 Git은 기본 저장소에서 실행하는 혼선을 피한다.
5. Python provider·Mason·LSP·formatter의 실제 실행 경로는 [11 런타임 계획](11-runtime-managers.md)에 맞춘다. pyenv Python을 사용하는 uv 환경과 nvm Node를 GUI가 자동 상속한다고 가정하지 않는다.

`lg` 단축 alias는 기존 Zsh 설정에 관측된다. Fish에는 같은 의도를 Fish 문법으로 따로 등록한다. tmux 기반 popup이나 tmux 전용 Neovim 이동 플러그인은 새 기본 구성에 복원하지 않는다. 발견된 사용자 설정 중 tmux 연동이 있는지 전체 플러그인 코드를 이번에 전수 분석한 것은 아니다.

## 8. worktree·파일·Git 작업의 기준

- 작업마다 실제 디렉터리 하나를 기준으로 Orca/Paseo·Herdr·Yazi·Neovim·lazygit을 맞춘다.
- Orca 또는 Paseo가 worktree를 만든 경우 해당 앱을 생성·정리 주체로 유지한다. Herdr의 worktree 생성 기능은 그 작업에서 중복 사용하지 않는다.
- lazygit은 해당 worktree의 Git 작업 도구다. 별도 pane과 Neovim 내 lazygit에서 commit·checkout·rebase 등을 동시에 진행하지 않는다.
- Neovim의 미저장 버퍼와 디스크 파일은 다르다. 에이전트의 수정과 수동 편집을 같은 파일에 동시에 진행할 때 덮어쓰기 여부를 사람이 조율한다.
- Orca/Paseo의 에이전트와 Herdr에서 직접 실행한 에이전트는 시작 주체·세션 기록이 다를 수 있다. hook 추가만으로 모든 관리 상태가 통합된다고 가정하지 않는다.
- 원격 Paseo daemon을 사용할 때 Yazi·Neovim·lazygit도 실제 파일이 있는 호스트에서 작업한다. 로컬 경로 문자열만 동일하게 만들어 원격 파일과 같은 것으로 취급하지 않는다.

## 9. 이전 문서에 반영할 필수 항목

- [ ] Ghostty 설치, tmux 설치·복원 제외
- [ ] Orca + Herdr 또는 Paseo + Herdr의 작업별 관리 주체 선택
- [ ] Herdr와 Yazi·Neovim·lazygit을 필수 공통 도구로 설치
- [ ] Fish·Zsh별 EDITOR/VISUAL·PATH·사용자 단축키 구성
- [ ] Yazi edit opener와 셸별 y wrapper
- [ ] 기존 Neovim lazygit.nvim·leader 단축키·LSP 설정 복원
- [ ] 앱과 각 도구가 같은 실제 저장소·worktree 경로를 사용하도록 구성

설치·사용 단계의 향후 체크리스트이며 이번에 테스트나 실행 확인을 수행했다는 의미가 아니다. 공식 문서에 없는 제품 간 전용 integration·세션 자동 변환·중첩 TUI 호환성은 미확인으로 남긴다.
