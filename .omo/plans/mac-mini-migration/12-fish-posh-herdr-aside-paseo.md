# Fish·Oh My Posh·Herdr·Aside·Paseo 추가 설치 가이드

## 적용 범위와 현재 상태

2026-09-06 공식 설치·설정 문서를 검색하고 본문을 읽어 작성했다. Herdr는 사용자가 지정한 [herdr.dev](https://herdr.dev/)의 제품이다. 최신 정식 배포를 우선한다. 아래 명령은 새 Mac mini의 향후 설치 절차이며 이번 조사에서 실행하지 않았다. 설치·앱 실행·서비스 시작·테스트·OMO QA는 하지 않았다.

| 도구 | 현재 Mac에서 확인한 범위 | 문서 반영 |
| --- | --- | --- |
| Fish | `/opt/homebrew/bin/fish`, `~/.config/fish/config.fish` 존재 | 기존 짧은 안내를 상세화 |
| Oh My Posh | `/opt/homebrew/bin/oh-my-posh`와 기본 설정 후보 디렉터리 미관측 | 신규 설치 대상으로 추가 |
| Herdr | `/opt/homebrew/bin/herdr`, `~/.local/bin/herdr`, `~/.config/herdr` 미관측 | 신규 설치 대상으로 추가 |
| Aside | `/Applications/Aside.app`, 사용자 CLI 링크 존재 | 앱·CLI 분리 설치 및 이전 안내 보강 |
| Paseo | 기본 bin 후보와 `~/.paseo` 미관측 | 데스크톱·headless 설치 가이드 추가 |

미관측은 조사한 경로에 한정되며 모든 위치의 미설치를 확정하는 말이 아니다. 기존 Homebrew 203종·Caskroom 13개 숫자는 과거 관측 목록으로 유지한다. 새 요청 도구를 기존 설치 수에 더하지 않는다.

## 1. 전체 설치 순서

앱 조합은 [Orca + Herdr 또는 Paseo + Herdr 작업 구성](13-workflow-orca-paseo-herdr.md)을 따른다. Yazi·Neovim·lazygit을 공통 필수 도구로 포함하며 앱별 에이전트 관리와 Herdr의 수동 작업 공간을 구분한다.

터미널 앱은 Ghostty, 세션·pane 관리 도구는 Herdr로 확정한다. tmux는 설치·설정 복원에서 제외한다. Ghostty는 기존 목록에도 있었으며 [셸·터미널 문서](03-shell-terminal.md)의 상세 설치 단계를 보강했다.

1. [런타임 관리자](11-runtime-managers.md)의 SDKMAN·nvm·pyenv·uv를 준비한다.
2. `brew install --cask ghostty`로 Ghostty를 설치한 뒤 Fish와 Nerd Font·Oh My Posh를 설치하고 Fish 설정을 작성한다.
3. Codex·Claude Code 등 사용할 에이전트와 계정 인증을 준비한다.
4. Herdr를 설치하고 사용할 에이전트 integration만 연결한다.
5. Aside 브라우저와 필요한 경우 Aside CLI를 별도 설치한다.
6. Paseo는 데스크톱 앱 또는 headless daemon 중 한 운영 경로를 선택한다. Mac mini 기본안은 데스크톱 앱이다.
7. 앱/daemon이 사용할 런타임 경로와 사용자 저장소 경로를 반영한다. 원격 pairing은 설치와 별도 설정 단계로 둔다.

## 2. Fish 설치와 셸 운영

### 2.1 최신 Fish 설치

[Fish 공식 안내](https://fishshell.com/docs/current/)와 Homebrew 배포를 따른다.

```sh
brew install fish
```

Apple Silicon Homebrew의 실행 경로는 `/opt/homebrew/bin/fish`다. 첫 설치에서는 시스템 로그인 셸을 바꾸지 않고 터미널 앱의 프로필 실행 파일을 이 경로로 지정하는 방식으로 시작한다. 기존 개발용 `/bin/zsh` 프로필도 유지한다. Fish 공식 문서는 터미널 프로필 지정과 로그인 셸 변경을 서로 다른 방법으로 설명한다.

로그인 셸 자체를 Fish로 바꾸려면 `/etc/shells`에 정확한 Fish 경로를 중복 없이 등록한 뒤 `chsh -s /opt/homebrew/bin/fish`를 사용하는 별도 단계가 필요하다. 이 설정은 SSH 로그인에도 영향을 주며 이번 기본 계획에서 자동 변경하지 않는다.

### 2.2 설정 파일과 PATH

새 Mac의 `~/.config/fish/config.fish`에 아래 내용을 병합한다. 실제 설정 파일은 이번에 만들거나 바꾸지 않았다.

```fish
fish_add_path /opt/homebrew/bin /opt/homebrew/sbin "$HOME/.local/bin"

if status is-interactive
    set -gx PYENV_ROOT "$HOME/.pyenv"
    pyenv init - fish | source
    oh-my-posh init fish | source
end
```

`fish_add_path`는 Fish 전용 PATH 도구다. 사용자 PATH 중복을 줄이도록 설계되어 있지만 이미 저장된 `fish_user_paths`에 옛 장치 경로가 있다면 새 설정에서 선별한다. 기존 `fish_variables` 전체 복원은 피하고 필요한 사용자 변수만 옮긴다. [Fish PATH 공식 문서](https://fishshell.com/docs/current/cmds/fish_add_path.html)

이 예시는 pyenv·Oh My Posh 설치가 선행된 상태다. `pyenv init - fish`는 pyenv upstream의 Fish 연동 방식이며, uv 설정의 `only-system`·`python-downloads = "never"`는 [11 문서](11-runtime-managers.md)와 같다.

### 2.3 SDKMAN·nvm과 Fish의 경계

| 항목 | Fish에서의 처리 |
| --- | --- |
| pyenv | `pyenv init - fish` 사용 |
| uv | 독립 실행 파일이므로 Fish에서도 사용 가능 |
| nvm-sh/nvm | Fish 직접 지원 없음; Zsh 개발 프로필 또는 아래 선택적 Bass 연결 |
| SDKMAN | 공식 설치 대상은 Bash·Zsh; Java 버전 변경은 Zsh 개발 프로필에서 수행 |

Fish에서 `zsh -il`로 개발 셸을 열면 11 문서의 nvm·SDKMAN 초기화가 적용된다. 그 안에서 `nvm use`, `sdk env` 후 작업한다. `exit`로 Fish에 돌아오면 자식 Zsh에서 변경한 환경이 부모 Fish로 역전파되지 않는다는 점을 구분한다. Fish의 `JAVA_HOME`·Node PATH에 특정 버전을 영구 고정해 이 차이를 숨기지 않는다.

Fish용 `nvm.fish`는 nvm-sh/nvm과 다른 구현이다. 사용자가 선택한 nvm을 유지하기 위해 기본안에서 교체하지 않는다. 근거: [nvm 공식 Fish 제한](https://github.com/nvm-sh/nvm#installation-and-update), [SDKMAN 공식 셸 지원](https://sdkman.io/install/).

### 2.4 선택 사항: Fish에서 기존 nvm 사용

Zsh로 전환하지 않고 Fish 안에서 nvm을 호출해야 할 때는 upstream README에 소개된 제삼자 Bass 연결을 추가할 수 있다. 기본 필수 설치에는 포함하지 않는다.

1. [Fisher 공식 저장소](https://github.com/jorgebucaran/fisher)의 설치 절차로 플러그인 관리자를 준비한다.
2. Fish에서 `fisher install edc/bass`로 [Bass](https://github.com/edc/bass)를 설치한다. Bass가 사용할 Python은 앞서 구성한 pyenv Python으로 준비한다.
3. `~/.config/fish/functions/nvm.fish`에 다음 함수를 둔다.

```fish
function nvm
    bass source "$HOME/.nvm/nvm.sh" --no-use ';' nvm $argv
end
```

이 경로도 `.nvmrc` 자동 전환을 기본 제공한다고 가정하지 않고 프로젝트에서 `nvm use`를 명시한다. SDKMAN까지 임의 Bash bridge로 묶어 공식 지원이라고 주장하지 않는다. 해당 bridge는 이번 조사에서 설치·실행하지 않았다.

## 3. Oh My Posh와 Nerd Font

### 3.1 설치

[Oh My Posh 공식 macOS 안내](https://ohmyposh.dev/docs/installation/macos)에 따른 명령이다.

```sh
brew install jandedobbeleer/oh-my-posh/oh-my-posh
brew install --cask font-jetbrains-mono-nerd-font
```

Nerd Font는 기존 Mac에도 관측된 JetBrains Mono 계열을 기본으로 쓴다. 폰트 설치 후 Ghostty·cmux·기타 터미널 및 VS Code 통합 터미널에서 실제 표시 폰트를 선택한다. 설치만으로 터미널의 사용 폰트가 자동 변경되지는 않는다. [공식 폰트 안내](https://ohmyposh.dev/docs/installation/fonts)

### 3.2 Fish 프롬프트 구성

2절처럼 `oh-my-posh init fish | source`를 대화형 셸 블록 마지막에 둔다. 공식 안내는 최신 Fish를 권장하며 Fish 4.1.0 미만에는 제한이 있다. [Fish 프롬프트 초기화](https://ohmyposh.dev/docs/installation/prompt)

사용자 테마를 관리하려면 공식 테마 또는 직접 편집한 설정을 `~/.config/ohmyposh/theme.omp.json`에 보관하고 초기화 행을 다음으로 바꾼다.

```fish
oh-my-posh init fish --config "$HOME/.config/ohmyposh/theme.omp.json" | source
```

테마 파일을 먼저 확보한 뒤 적용하며, 파일을 만들지 않은 상태로 해당 경로만 넣지 않는다. 기본 초기화와 사용자 테마 초기화를 동시에 두지 않는다. [공식 테마 설정](https://ohmyposh.dev/docs/installation/customize)

기존 Fish 사용자 `fish_prompt` 함수가 있다면 보관 후 Oh My Posh와 역할을 겹치지 않게 정리한다. Zsh의 기존 Powerlevel10k는 별도 프로필에서 유지할 수 있다. Zsh에서도 Oh My Posh를 채택할 경우에만 해당 Zsh 프롬프트 초기화를 교체한다. Oh My Zsh·Oh My Fish·Oh My Posh는 서로 다른 도구이며 모두 설치할 필요는 없다.

### 3.3 업데이트와 이전 자료

Homebrew 설치본은 `brew upgrade oh-my-posh`로 업데이트한다. 이전 대상은 사용자 테마·Fish 함수·선택한 폰트 이름이다. 프롬프트 캐시나 이전 바이너리는 새 설치에 덮어쓰지 않는다. 렌더링·아이콘 출력 시험은 수행하지 않았다.

## 4. Herdr 설치와 에이전트 연결

### 4.1 최신 설치

Herdr는 Ghostty 안에서 workspace·tab·pane과 에이전트를 관리하며 사용자 결정에 따라 tmux의 대체로 사용한다. [공식 설치 안내](https://herdr.dev/docs/install/)에 따라 기존 Homebrew를 사용한다. tmux 설정·플러그인·기존 세션을 Herdr에 그대로 가져오는 단계는 없다.

```sh
brew install herdr
```

직접 다운로드가 필요하면 같은 공식 페이지에서 연결한 stable 릴리스의 `herdr-macos-aarch64`를 선택한다. Homebrew와 직접 설치를 중복하지 않는다. Homebrew 설치본 업데이트는 `brew upgrade herdr`로 관리한다.

### 4.2 사용자 설정

설정 위치는 `~/.config/herdr/config.toml`이다. 설정 파일 없이도 시작할 수 있으므로 처음부터 전체 기본값을 복사할 필요는 없다. [공식 구성 문서](https://herdr.dev/docs/configuration/)

개발 pane에서 기존 nvm·SDKMAN을 직접 쓰는 기본 예시는 다음과 같다.

```toml
[terminal]
default_shell = "/bin/zsh"
shell_mode = "login"
```

Fish pane을 기본으로 하고 싶다면 `default_shell = "/opt/homebrew/bin/fish"`로 바꾸고 2절의 런타임 제한을 적용한다. `default_shell`에는 `/bin/zsh -il` 같은 명령 문자열을 넣지 않는다. 실행 파일 경로와 `shell_mode`는 별도 필드다. 변경은 새 pane에 적용되며 기존 pane의 셸을 바꾸지는 않는다.

### 4.3 최초 구성과 integration

1. Codex·Claude Code·OpenCode 등 실제 사용할 CLI를 먼저 설치하고 인증한다.
2. 향후 실제 사용을 시작할 때 프로젝트 폴더에서 `herdr`를 실행하고 최초 설정 화면을 따른다. 이 명령은 서버를 시작하는 실제 사용 단계이며 이번 조사에서는 실행하지 않았다.
3. Settings의 integrations 탭에서 사용할 에이전트만 연결한다. CLI를 이용하는 설치 예시는 다음과 같다.

```sh
herdr integration install claude
herdr integration install codex
```

OpenCode를 사용한다면 공식 안내의 `herdr integration install opencode`가 `~/.config/opencode/plugins/herdr-agent-state.js`를 생성한다. 해당 config 디렉터리가 먼저 있어야 한다. [Herdr 공식 integration 안내](https://herdr.dev/docs/integrations/)

OMO·OMC·Orca가 이미 구성한 hook과 사용자 hook을 보관한 뒤 필요한 Herdr 항목을 추가한다. 기존 hook 파일 전체를 Herdr 템플릿으로 덮어쓰지 않는다. Herdr integration이 모든 에이전트 상태를 같은 방식으로 관측하는 것은 아니며 Claude·Codex의 session 복원 식별과 화면 상태 관측을 구분한다.

### 4.4 세션·데이터 보관

터미널을 닫거나 detach해도 서버·에이전트가 계속 실행될 수 있다. 향후 작업 종료 시 앱의 detach와 서버 종료를 구분한다. 세션 종료를 위한 `herdr server stop`은 해당 pane도 중단하므로 설치 과정에서 자동 호출하지 않는다. [공식 빠른 시작](https://herdr.dev/docs/quick-start/)

사용자 설정·사용자 플러그인·worktree의 실제 소스는 보관하고, 소켓·PID·실행 중 서버 상태는 새 장치에 활성 상태로 복원하지 않는다. 이번 조사에서 Herdr 사용자 데이터가 있다고 확인하지 않았으므로 가상의 보관 경로를 만들지 않는다.

## 5. Aside 브라우저와 CLI 설치

### 5.1 브라우저 앱

1. [Aside 공홈](https://aside.com/)에서 최신 macOS 앱을 받거나, [Homebrew Aside 배포](https://formulae.brew.sh/cask/aside)를 이용한다.

```sh
brew install --cask aside
```

2. 배포 요구사항은 조회일 기준 macOS 13 이상이다. 앱은 `/Applications/Aside.app`에 설치되고 자동 업데이트를 제공한다.
3. 새 Mac에서 앱을 열 때 자체 안내에 따라 계정과 필요한 웹 서비스에 로그인한다. 기존 브라우저 쿠키가 일반 설정 파일 복사로 이전된다고 가정하지 않는다.
4. 필요한 macOS 권한은 새 장치의 앱 요청에 따라 설정한다. 이번에는 앱·브라우저를 열거나 권한을 변경하지 않았다.

### 5.2 CLI의 공식 배포 근거

[Aside 공식 CLI 설치 스크립트](https://releases.aside.com/install.sh)를 HTTP로 내려받아 텍스트만 읽었다. 기본값은 다음과 같다.

| 항목 | 공식 스크립트 기본값 |
| --- | --- |
| 버전 | `latest` |
| Mac mini 아키텍처 | `darwin-arm64` |
| 압축 파일 | `AsideCLI-darwin-arm64-latest.zip` |
| 다운로드 원점 | `https://releases.aside.com/cli` |
| 설치 앱 | `~/.aside/cli/Aside CLI.app` |
| 명령 링크 | `~/.local/bin/aside` |

스크립트는 기존 CLI 앱을 교체하고 마지막에 `aside --help`·`--version`을 호출한다. 요청한 비실행 조사 범위에 따라 이 설치자는 실행하지 않았다. 브라우저 cask의 artifact는 Aside.app이며 CLI까지 설치한다고 확인된 것은 아니다.

### 5.3 실행 호출 없는 CLI 파일 배치 계획

1. 새 Mac에서 [공식 Apple Silicon CLI 압축 파일](https://releases.aside.com/cli/AsideCLI-darwin-arm64-latest.zip)을 다운로드한다. 이 URL은 공식 설치자의 기본값으로부터 구성했으며 이번에 ZIP 자체를 다운로드하거나 실행하지 않았다.
2. 별도 다운로드 폴더에서 압축을 해제한다. `Aside CLI.app`을 `~/.aside/cli/`에 배치한다. 같은 이름의 기존 앱이 있으면 별도 보관 후 교체한다.
3. `~/.local/bin`에 기존 `aside`가 없는 경우 아래 링크를 등록한다.

```sh
ln -s "$HOME/.aside/cli/Aside CLI.app/Contents/MacOS/aside" "$HOME/.local/bin/aside"
```

부모 디렉터리를 먼저 준비하며 기존 링크를 강제 덮어쓰지 않는다. 이 명령은 링크 등록만 하고 CLI를 호출하지 않는다.

4. Fish에는 `fish_add_path "$HOME/.local/bin"`, Zsh에는 11 문서의 사용자 bin PATH를 반영한다.
5. 인증·브라우저 연결은 새 앱의 안내로 구성한다. `~/.aside/accounts.json`, `u/`의 프로필과 쿠키·로그를 공개 문서에 복사하지 않는다.
6. Aside 연동 사용자 스킬은 원본을 보관하고 최신 CLI 경로로 맞춘다. 기존 `.aside/runtime*`·버전별 CLI 앱 번들은 재설치 대상으로 분리한다.

## 6. Paseo 설치

### 6.1 먼저 선택할 운영 형태

| 형태 | 용도 | 이번 기본안 |
| --- | --- | --- |
| 데스크톱 앱 | Mac mini에서 UI와 내장 daemon 사용 | 기본 |
| npm CLI·headless | UI 없이 서버 운영 | 대안 |
| Docker | 컨테이너로 독립 서버 운영 | 기본 설치에 추가하지 않음 |

[공식 시작 안내](https://paseo.sh/docs)는 데스크톱 앱이 daemon을 포함하고 자동으로 시작한다고 명시한다. 따라서 데스크톱 설치 직후 별도 npm daemon을 같은 홈·포트로 중복 시작하지 않는다. Paseo는 에이전트를 관리하는 도구이며 Codex·Claude 등의 provider CLI는 별도 설치가 필요하다.

### 6.2 Mac mini 데스크톱 설치

1. [공식 다운로드 페이지](https://paseo.sh/download)에서 Apple Silicon stable 앱을 받거나 다음을 사용한다.

```sh
brew install --cask paseo
```

2. 조회일 페이지는 v0.7.2와 macOS 13 이상을 안내하지만 설치일 최신 정식 릴리스를 선택한다. 홈페이지 화면 속 beta 세션 예시를 배포 채널로 해석하지 않는다.
3. 앱을 처음 열면 내장 daemon이 시작되는 실제 사용 단계가 된다. 이번에는 앱을 실행하지 않았다.
4. 사용할 provider CLI·계정·프로젝트 경로를 설정한다. PR 관련 기능을 쓸 경우 `gh`와 GitHub 인증도 준비한다.
5. 스마트폰 연결이 필요할 때 Settings → host → Pair Device로 이동한다. 원격 연결은 별도 선택 단계다.

### 6.3 headless 대안

데스크톱 UI 없이 운영하기로 정한 경우 nvm의 기본 Node가 활성화된 Zsh에서 다음으로 설치한다.

```sh
npm install -g @getpaseo/cli
```

실제 서버 운영 시작 명령은 `paseo`다. 첫 시작은 relay 사용과 pairing을 질문할 수 있다. 이 명령은 설치 명령과 분리하여 나중에 실행하며 이번 조사에서는 실행하지 않았다. [공식 headless 설치](https://paseo.sh/docs#server--cli)

nvm Node 버전별 전역 패키지가 분리되므로 Node 업데이트 시 Paseo CLI도 새 기본 Node에 설치한다. 로그인 셸과 daemon의 PATH가 항상 같지 않으며 LaunchAgent·앱에서 시작한 daemon에는 실제 provider 실행 경로를 지정해야 할 수 있다. nvm·SDKMAN 셸 함수를 직접 executable로 등록하지 않는다.

### 6.4 설정·인증·원격 연결

기본 홈은 `~/.paseo`, 설정은 `~/.paseo/config.json`이다. `PASEO_HOME`으로 별도 홈을 지정할 수 있다. 최소 로컬 설정의 문서 예시는 다음과 같다. 기존 파일에는 필요한 항목만 병합한다.

```json
{
  "$schema": "https://paseo.sh/schemas/paseo.config.v1.json",
  "version": 1,
  "daemon": {
    "listen": "127.0.0.1:6767",
    "relay": { "enabled": false }
  }
}
```

이는 최초 로컬 사용을 위한 기본안이다. 실제 설정을 저장하지 않았다. 환경 변수·실행 인자가 파일보다 우선할 수 있다. [공식 설정](https://paseo.sh/docs/configuration)

원격 접속은 E2EE relay pairing 또는 Tailscale/VPN 등의 직접 연결 중 선택한다. localhost 설정만으로 다른 장치가 직접 접속할 수는 없다. relay는 사용자가 pairing 과정에서 활성화하고, 직접 네트워크 연결은 접근 주소·인증을 따로 구성한다. pairing QR·offer URL·비밀번호는 공유 설치 문서에 넣지 않는다. [공식 연결 안내](https://paseo.sh/docs/connectivity)

계정 권한은 각 provider의 기존 인증을 사용하며 Paseo를 설치했다고 provider 로그인이 완료되는 것은 아니다. OMO·OMC 설정을 Paseo용으로 통째 교체하지 않는다. daemon이 읽을 홈과 실제 CLI 위치를 맞춘다.

### 6.5 업데이트와 자료 이전

데스크톱은 설치 채널의 업데이트 방식을 사용하고 Homebrew 설치라면 `brew upgrade --cask paseo`로 관리한다. npm CLI 경로는 최신 `@getpaseo/cli`로 갱신한다. 앱과 별도 daemon의 버전·운영 홈을 혼동하지 않는다. [공식 업데이트 안내](https://paseo.sh/docs/updates)

`~/.paseo/config.json`의 사용자 선택, 프로젝트 선언, 실제 worktree 소스를 보관 대상으로 분리한다. 기본 worktree는 Paseo 홈 하위에 있을 수 있어 전체 홈을 캐시로 삭제하지 않는다. daemon 로그·실행 상태와 계정·pairing 정보는 별도 취급한다. 앱 종료·detach·daemon 중단은 서로 다른 상태이며 이번에 어느 것도 실행하지 않았다.

## 7. 누락 방지 목록

- [ ] Ghostty 최신 정식 배포 및 사용자 폰트·테마
- [ ] Fish 및 새 `config.fish`
- [ ] Oh My Posh와 선택한 Nerd Font·사용자 테마
- [ ] pyenv Fish 연동, nvm·SDKMAN용 Zsh 개발 프로필
- [ ] tmux 설치·설정 복원 제외, Herdr 및 필요한 Claude·Codex integration
- [ ] Aside 브라우저, 별도 CLI, 사용자 스킬·새 로그인
- [ ] Paseo 데스크톱 또는 headless 경로 하나, provider CLI·계정·프로젝트 경로
- [ ] 원격 접속이 필요할 때만 Paseo pairing·연결 설정

이 목록은 새 Mac의 향후 설치 체크리스트다. 현재 조사 결과나 실행 성공 표시가 아니며 테스트·doctor·provider diagnostics·OMO QA 항목을 포함하지 않는다.

## 8. 공식 출처와 수집 한계

본문에 연결한 Fish·Oh My Posh·Herdr·Paseo 공식 페이지와 Aside 공홈·Homebrew cask 페이지를 실제 열람했다. 선택적 Fish bridge는 nvm upstream에서 소개한 Bass와 Fisher 저장소를 읽었다. 이들은 각기 제삼자 프로젝트이며 SDKMAN의 공식 Fish 지원을 의미하지 않는다.

Aside CLI 스크립트는 웹 도구 열람 실패와 sandbox DNS 실패 후 공개 URL 읽기 권한으로 텍스트 수집에 성공했다. 스크립트 실행 및 CLI ZIP 다운로드는 하지 않았다. Aside cask JSON API는 웹 도구에서 읽지 못했으나 같은 Homebrew의 cask HTML 페이지에서 앱·명령·요구사항을 확인했다. 실제 장치의 설치·권한·연결·프롬프트 렌더링은 확인하지 않았다.
