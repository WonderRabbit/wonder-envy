# 셸과 터미널 이전 계획

> 2026-09-11 후속 적용: 기본 셸과 개발 환경은 Fish로 변경했다. 아래 과거 Zsh 운영 방침은 [계획 16](16-fish-catppuccin-lsd.md)이 대체한다. nvm·SDKMAN은 Bass로 연동하고 테마는 Catppuccin Mocha를 사용한다.

## 적용 원칙과 조사 범위

런타임 초기화는 후속 확정된 [SDKMAN·nvm·pyenv·uv 설치 계획](11-runtime-managers.md)의 Zsh 예시를 우선한다. pyenv shims는 사용하고, Conda 자동 활성화·옛 Hermes Node 링크는 복원하지 않는다.

2026-09-06 현재 Mac의 파일 목록과 셸 설정을 읽어 작성했다. 설정 파일을 실행하거나 source하지 않았다. 아래 절차는 Mac mini에서 나중에 수행할 설치·설정 계획이며 이번 조사에서는 실행하지 않았다. 테스트·QA 단계는 포함하지 않는다.

Mac mini에는 최신 안정 버전을 우선 설치한다. 기존 설정에서 단축키·테마·함수 등 사용자 의도를 옮기되, 오래된 버전 경로와 임시 경로는 복원하지 않는다. 이 문서의 `~`는 각 Mac의 사용자 홈이다. 기존 홈 경로 `/Users/oneyoon`은 새 Mac의 실제 홈 또는 `$HOME`으로 바꾼다.

## Zsh와 dotfiles

### 현재 근거

- `~/.zshrc`는 `dotfiles/.zshrc`를 가리키는 상대 심볼릭 링크다. `~/dotfiles`가 존재한다.
- `~/.zprofile`, `~/.zshenv`, `~/.bash_profile`이 있다. `.zshrc`와 `.zprofile` 양쪽에 Homebrew `shellenv` 참조가 있다.
- PATH에는 `.local/bin`, `.pyenv/bin`, `.go/bin`, `go/bin`, Android SDK, Docker completions, LM Studio, Antigravity, OpenCode, IntelliJ 관련 항목이 있다.
- `.zshrc:291,294,297,300`에는 `/tmp/sensai-.../home/.opencode/bin` 임시 PATH가 네 번 추가되어 있다. `.zshrc:258`의 `/usr/local/opt/sqlite/bin`, `.bash_profile:1`의 `/usr/local/opt/python/libexec/bin`도 새 Apple Silicon 설치 경로와 분리하여 다뤄야 한다.

### 이전 순서

1. Mac mini의 기본 Zsh를 사용하고 Homebrew 설치를 먼저 마친다. Homebrew 환경 등록은 새 설치 안내에 맞춰 `.zprofile` 한 곳에서 관리한다.
2. `~/dotfiles`의 사용자 설정 원본과 세 시작 파일을 별도 보관한다. 셸 이력 파일은 이 계획의 이전 대상에서 제외한다.
3. 새 Mac의 기존 `.zshrc`가 있으면 별도 이름으로 보관하고, 정리한 `~/dotfiles/.zshrc`를 만든 뒤 `~/.zshrc` 상대 링크를 다시 만든다. 기존 파일을 강제 덮어쓰는 명령은 사용하지 않는다.
4. `.zshenv`에는 모든 셸에 필요한 최소 환경만 두고, `.zprofile`에는 로그인 환경, `.zshrc`에는 대화형 플러그인·alias·함수를 둔다. [Zsh 시작 파일 설명](https://zsh.sourceforge.io/Guide/zshguide02.html)
5. `/Users/oneyoon` 상수는 `$HOME`으로 전환한다. `/tmp/sensai-*` 네 항목, 설치되지 않은 도구 초기화, 중복 `.local/bin` 추가는 새 설정에서 빼고 실제 설치한 도구의 경로만 넣는다.
6. `.go/bin`과 `go/bin`은 서로 다른 경로다. 새 Go 설치 및 프로젝트의 GOPATH 정책에 맞는 한 경로를 사용한다. 둘 중 어느 것이 현재 유효한지는 이번 조사에서 실행 확인하지 않았다.

## Zinit

현재 `~/.local/share/zinit/zinit.git`와 플러그인 하위 디렉터리가 있고, `.zshrc:1`의 `ZINIT_HOME` 및 `:9`의 source가 연결된다.

1. [Zinit 공식 설치 안내](https://github.com/zdharma-continuum/zinit)의 현재 설치 방법으로 새 Mac에 설치한다.
2. 기존 `.zshrc`에서 필요한 플러그인 선언을 옮긴다. 다운로드 캐시와 기존 바이너리 빌드는 새 설치에 포함하지 않는다.
3. Oh My Zsh 및 Homebrew와 중복 제공하는 플러그인의 로드 위치를 하나로 정한다. 이번 조사에서는 플러그인 전체의 실제 실행 순서를 판정하지 않았다.

## Oh My Zsh

현재 `~/.oh-my-zsh`가 있고 `.zshrc:158`의 플러그인은 `git`, `brew`, `docker`, `zsh-syntax-highlighting`, `zsh-autosuggestions`다. `ZSH_THEME`는 `pygmalion`이며 `:166`에서 프레임워크를 읽는다.

1. [공식 설치 문서](https://github.com/ohmyzsh/ohmyzsh)에 따라 설치하되 새 `.zshrc`가 사용자 원본을 덮어쓰지 않도록 설치용 파일과 복원용 파일을 분리한다.
2. `custom` 아래 직접 작성한 테마·플러그인만 선별 복원한다. 기본 플러그인은 새 버전을 사용한다.
3. autosuggestions와 syntax-highlighting을 Zinit, Oh My Zsh, 직접 source 중 한 방식으로만 등록한다. 현재 `.zshrc:199`에 Homebrew syntax-highlighting 직접 source도 있다.

## Powerlevel10k

현재 `~/powerlevel10k`, `~/.p10k.zsh`가 있고 `.zshrc:79`에 instant prompt 캐시 참조, `:193`에 테마 직접 source가 있다. Oh My Zsh의 `pygmalion` 설정도 함께 존재한다.

1. 기존 프롬프트를 유지할 경우 [Powerlevel10k 공식 설치 안내](https://github.com/romkatv/powerlevel10k)에 따라 설치하고 `~/.p10k.zsh`를 옮긴다.
2. 새 셸에서는 Powerlevel10k를 쓸 경우 `pygmalion`과 중복 테마 활성화를 제거한다. 외형 유지가 필요 없다면 기본 프롬프트를 쓰고 Powerlevel10k는 선택 설치로 남긴다.
3. 예전 instant prompt 캐시는 복사하지 않는다. 터미널 폰트 설정과 필요한 글꼴 설치는 함께 반영한다.

## Alias와 사용자 함수

관찰된 alias는 `nvim`, `c`, `py`, `lg`, `cd`, `vim`, `vi`, `vimdiff`, `ls`, `lsa`, `lt`, `lta`이고 함수 이름은 `y`다. 함수 본문에는 파일 경로 등 사용자 정보가 섞일 수 있으므로 문서에 복제하지 않았다.

1. `py → python3`, `lg → lazygit`, `cd → z`, `ls/lt → eza` 등 대상 도구를 먼저 설치한다.
2. `.zshrc:201`에서 `vim` alias의 첫 명령은 `nmin`으로 관찰됐다. 의도한 별도 명령인지 미확인이다. 새 설정에서 무조건 복원하지 말고 Neovim을 의도했다면 `nvim`으로 작성한다.
3. `y` 함수는 기존 원본을 사용자 설정으로 보관하고, 호출 도구와 임시 파일 처리 경로를 새 Yazi 설치에 맞춰 옮긴다.
4. 로그인·토큰·서비스 접속을 포함할 수 있는 다른 설정은 alias 묶음에 합치지 않는다.

## fzf

`.zshrc:18,55,56,66`에 fzf 참조가 있다. [공식 설치 및 셸 연동 안내](https://github.com/junegunn/fzf#installation)에 따라 최신판을 설치하고, 기존 키 바인딩과 completion 설정을 현재 Zsh 연동 방식에 맞춰 한 번만 등록한다. 인증 복원은 필요하지 않다.

## zoxide

`.zshrc:69`에 초기화 참조가 있고 `cd` alias는 `z`를 사용한다. [공식 설치 문서](https://github.com/ajeetdsouza/zoxide#installation)에 따라 설치한 뒤 Zsh 초기화를 등록하고 `cd` alias를 복원한다. 과거 디렉터리 이동 데이터베이스는 새 Mac의 경로와 일치한다고 가정하지 않는다.

## eza

`ls`와 `lt` alias가 eza를 사용한다. [공식 설치 문서](https://github.com/eza-community/eza/blob/main/INSTALL.md)에 따라 최신판을 설치하고 원본 alias의 옵션을 옮긴다. 글리프를 사용하는 옵션은 새 터미널에 설치한 폰트와 함께 복원한다.

## lazygit

공통 필수 도구로 `brew install lazygit`을 사용한다. [통합 작업 구성](13-workflow-orca-paseo-herdr.md)에 Herdr Git pane과 Neovim 내 사용 순서를 명시했다. 현재 플러그인 파일에서 `kdheepak/lazygit.nvim`, `plenary.nvim`, `<leader>lg` → `LazyGit` 선언을 직접 확인했으며 실행하지 않았다.

`lg` alias와 `~/.config/nvim/lua/oneyoon/plugins/lazygit.lua`가 있다. [공식 설치 안내](https://github.com/jesseduffield/lazygit#installation)에 따라 설치한 뒤 alias 및 Neovim 연동을 복원한다. Git 인증은 [개발환경과 보안 이전 계획](04-dev-security.md)의 Git·SSH 절차로 처리한다.

## Ghostty

현재 `~/.config/ghostty/config`와 `themes/catppuccin-*.conf` 네 파일이 있다. 설정 키로 폰트·폰트 크기·여백·투명도·테마를 관찰했다. `th/ghostty`에는 별도 테마 저장소 형태의 파일이 있다.

1. Ghostty는 사용자 확정 설치 대상이다. [공식 설치 안내](https://ghostty.org/docs/install/binary)에 따라 `brew install --cask ghostty`로 최신 정식 배포를 설치한다. 공식 DMG 다운로드 후 `/Applications`에 배치하는 방법도 제공되며 두 설치 경로를 중복 사용하지 않는다.
2. `config`와 실제 참조하는 `themes` 파일을 새 `~/.config/ghostty`에 옮긴다. `th`의 참고 저장소 전체를 필수 설정으로 취급하지 않는다.
3. 설정에 지정한 폰트를 설치하고 경로가 들어간 항목만 새 홈 기준으로 바꾼다. 이 조사에서는 색상·폰트 값 자체를 문서에 추출하지 않았다.
4. [공식 설정 문서](https://ghostty.org/docs/config)를 기준으로 기존 폰트·테마·여백 설정을 선별 복원한다. Fish 사용은 [12 문서](12-fish-posh-herdr-aside-paseo.md)의 셸 구성을 따르고 nvm·SDKMAN용 Zsh 개발 환경도 유지한다.
5. 세션·pane 관리는 Herdr를 사용한다. Ghostty 설정과 셸 시작 파일에 tmux 자동 시작·attach 명령을 넣지 않는다. 기존 `.tmux.conf`와 tmux 플러그인은 이전 제외다.
6. 향후 Homebrew 설치본 업데이트는 `brew upgrade --cask ghostty`를 사용한다. 설치·프롬프트 렌더링·앱 실행은 이번 조사에서 수행하지 않았다.

## Alacritty

`~/.config/alacritty/alacritty.toml`과 테마 디렉터리가 있다. import, TERM, 창 투명도·여백, Option 키 동작, normal/bold/italic 글꼴 항목을 관찰했다.

1. [공식 최신 상태 조사](09-official-sources.md) 및 [Homebrew 공식 API](https://formulae.brew.sh/api/cask/alacritty.json)에서 Alacritty cask가 `fails_gatekeeper_check` 사유로 비활성화된 것을 확인했다. Homebrew 자동 설치 대상으로 넣지 않고, 공식 최신 배포판의 서명·배포 안내가 명확해질 때까지 설치를 보류한다. 터미널은 기존 사용 흔적이 있는 Ghostty를 우선 구성한다. Gatekeeper 비활성화나 검역 속성 제거를 이전 절차로 사용하지 않는다.
2. 설치를 재개할 때 `alacritty.toml`과 import 대상 테마 파일을 함께 옮긴다. 전체 테마 라이브러리는 필요할 때만 복사한다. 설정 경로와 import 문법은 [공식 설정 문서](https://alacritty.org/config-alacritty.html)를 따른다.
3. 글꼴을 설치하고 import의 절대 홈 경로를 새 경로로 바꾼다. 예전 macOS 앱 번들 경로가 있으면 새 `/Applications` 설치 위치에 맞춘다.

## iTerm2

현재 `~/Library/Preferences/com.googlecode.iterm2.plist`와 `~/.config/iterm2/{AppSupport,sockets}`가 있다. plist 내용·프로필 호스트는 읽지 않았다.

1. 최신 iTerm2를 설치한다.
2. 기존 환경에서 별도 Preferences 폴더를 사용했다면 그 설정 파일을 보관하고, 새 앱의 General → Preferences에서 이전 설정 폴더를 지정한다. [공식 Preferences 설명](https://iterm2.com/documentation-preferences-general.html)
3. 프로필의 기본 디렉터리·사용자 셸·SSH 명령은 새 Mac 기준으로 바꾼다. 소켓과 실행 중 상태는 이식하지 않는다.
4. plist만으로 복원해야 한다면 앱을 종료한 상태에서 사용자 설정 백업을 보관한 후 새 Preferences에 배치한다. 로그인 정보는 별도 인증 절차를 따른다.

## cmux

`~/.config/cmux/cmux.json`이 있다. 본문 및 세션 정보는 읽지 않았다.

1. [공식 설치 안내](https://cmux.com/docs/getting-started)에 따라 최신 안정판을 설치한다.
2. 사용자 설정 파일을 보호된 경로로 옮기고 작업 디렉터리·실행 명령의 절대 경로를 새 Mac에 맞춘다.
3. 외부 셸에서도 CLI가 필요하면 새 앱 번들의 CLI 위치를 PATH에 연결한다. 문서의 강제 링크 명령을 그대로 적용하기보다 기존 링크 대상이 없는 새 경로를 사용한다.
4. 실행 중 프로세스 상태를 설정 파일만으로 이전할 수 있다고 가정하지 않는다. cmux 공식 문서는 임의 프로세스의 체크포인트 복원과 레이아웃 복원을 구분한다.

## Fish

후속 요청에 따라 Fish를 명시적 설치 대상에 포함한다. 설치 명령·설정 예시·Oh My Posh·Nerd Font·nvm/SDKMAN 연결은 [추가 도구 상세 가이드](12-fish-posh-herdr-aside-paseo.md)의 2~3절을 우선한다.

`~/.config/fish/config.fish`와 `fish_variables`가 있다. 사용 중인 기본 셸이라는 근거는 확보하지 않았다.

1. `brew install fish`로 최신 Fish를 설치한다. [공식 문서](https://fishshell.com/docs/current/)
2. `config.fish`를 복원하고 `fish_variables`는 경로 및 민감 변수 포함 가능성을 고려해 필요한 항목만 옮긴다.
3. Zsh용 `export`·초기화 문법을 그대로 붙이지 않고 해당 도구의 Fish 연동 방법을 따른다. 기본 로그인 셸 변경은 필수 이전 단계가 아니다.

## Neovim

Yazi와 함께 쓰는 공통 필수 편집기다. [13 문서](13-workflow-orca-paseo-herdr.md)의 EDITOR/VISUAL·lazygit 연결·작업 디렉터리 기준을 따른다.

현재 `~/.config/nvim/init.lua`, `lazy-lock.json`, `lua/oneyoon/{core,plugins}` 및 lazy 설정이 있다. LSP·Mason·treesitter·formatting·linting·lazygit 관련 플러그인 파일이 관찰됐다.

1. [공식 설치 안내](https://neovim.io/doc/install/)에 따라 최신 안정판을 설치한다.
2. `~/.config/nvim`의 사용자 Lua 설정을 옮긴다. 기존 lockfile은 참고용으로 보관하고 최신 플러그인에 맞춰 새 설치를 구성한다. 프로젝트가 특정 버전을 요구하는 경우만 별도 고정한다.
3. Mason으로 설치했던 실행 파일·파서·캐시는 새 Mac에서 해당 플러그인의 설치 흐름으로 다시 설치한다. 기존 아키텍처별 바이너리 디렉터리를 복사하지 않는다.
4. LSP 실행 경로·Python provider·프로젝트 루트 절대 경로가 있다면 최신 런타임 설치 결과에 맞춰 설정한다. 세션 복구 파일은 이 문서에서 다루지 않는다.

## Yazi

파일 탐색의 공통 필수 도구다. [13 문서](13-workflow-orca-paseo-herdr.md)에 Neovim edit opener와 Fish/Zsh 셸 연결을 정리했다.

`~/.config/yazi/{yazi.toml,keymap.toml,theme.toml}`가 있다.

1. [공식 설치 안내](https://yazi-rs.github.io/docs/installation/)에 따라 최신판과 사용할 미리보기 의존성을 설치한다.
2. 세 설정 파일의 사용자 키 바인딩·테마·파일 연결을 현재 설정 형식에 맞춰 옮긴다.
3. Zsh의 `y` 함수와 연결하고, 파일 열기 명령이 가리키는 앱·편집기 경로를 새 Mac에 맞춘다.

## 조사하지 않은 영역

현재 로그인 셸의 실제 PATH 우선순위, 플러그인 실행 결과, 폰트 렌더링, 터미널 프로필별 접속 대상, 소켓·세션 내용은 확인하지 않았다. 문서 생성 외에 설정 수정·앱 실행·설치·테스트·QA를 하지 않았다.
