# Fish 기본 셸과 Catppuccin Mocha

적용일: 2026-09-11. macOS 로그인 셸은 `/opt/homebrew/bin/fish`다. Terminal.app·Ghostty·Herdr의 새 터미널도 Fish로 시작한다. 기존에 열려 있는 Zsh는 자동 교체되지 않는다. 현재 창만 바꾸려면 `exec /opt/homebrew/bin/fish -l`을 실행한다.

## Fish에서 개발하기

```fish
status is-login
echo $SHELL
nvm current
nvm use default
node --version
npm --version
pyenv version
pyenv which python
python --version
sdk current java
sdk use java 26.0.2-tem
java --version
uv --version

# 프로젝트 가상환경
uv venv --python (pyenv which python)
source .venv/bin/activate.fish
python --version
deactivate
```

기존 프로젝트의 `.nvmrc`는 `nvm use`, `.python-version`은 pyenv, `.sdkmanrc`는 `sdk env`로 적용한다. 파일에 지정한 버전이 미설치 상태면 먼저 해당 관리자로 설치한다. nvm의 전역 npm 패키지는 Node 버전마다 별도다. 현재 기본 Node에 Codex·OpenCode가 설치되어 있다.

Fish는 POSIX 셸과 문법이 다르다. 환경 변수는 `set -gx NAME value`, 명령 치환은 `(command)`를 사용한다. `.venv/bin/activate` 대신 `activate.fish`를 source한다. 프로젝트의 Bash/Zsh 스크립트는 해당 인터프리터로 실행한다. `dev`는 선택적으로 새 로그인 Fish를 여는 별칭이며 런타임 사용에 필수인 단계가 아니다.

## nvm·SDKMAN 연동 방식

nvm-sh와 SDKMAN의 기존 설치를 보존하고 **Bass**가 Bash에서 바뀐 환경을 현재 Fish에 전달한다. `nvm`과 `sdk`는 `~/.config/fish/functions/`의 함수이며 별도 실행 파일이 아니다. Fish에서 두 관리자의 `.sh` 파일을 직접 source하지 않는다.

- nvm: 부모의 유효한 `NVM_BIN`을 유지하고, 없으면 기본 별칭을 읽는다. 버전 변경은 현재 Fish에 적용된다.
- SDKMAN: Java 경로는 시작 시 설정하고 관리 함수는 `sdk` 호출 시 로드한다. SDKMAN 초기화가 세션의 `sdk use` 선택을 초기화하지 않도록 PATH·JAVA_HOME을 보존한다.
- pyenv: 비대화형 `fish -c`에서도 초기화하고 shim을 상속받은 직접 Python 경로보다 앞에 둔다.
- Bass: upstream 파일을 보관하고 적용본만 수정했다. 내부 환경 비교용 Python은 `/usr/bin/python3`로 고정해 pyenv shim 실행 과정의 PATH 변경이 Fish로 유입되지 않게 했다. 실패 시 임시 파일도 정리한다. 새 Mac에서는 Apple Command Line Tools가 선행 조건이다.
- mise: task 전용이다. 런타임 자동 activation·shim은 추가하지 않았다.

참고: [Fish 문서](https://fishshell.com/docs/current/), [nvm의 Fish 안내](https://github.com/nvm-sh/nvm#fish), [Bass](https://github.com/edc/bass), [SDKMAN](https://sdkman.io/usage/), [pyenv](https://github.com/pyenv/pyenv), [uv 가상환경](https://docs.astral.sh/uv/pip/environments/).

## 테마 적용 위치

기본 flavor는 **Mocha**, 선택 가능한 accent는 **Mauve**다. [Catppuccin 공식 포트](https://github.com/catppuccin)의 파일 또는 도구 내장 테마를 사용한다.

| 도구 | 적용 방식·실제 파일 | 공식 참고 |
| --- | --- | --- |
| Ghostty | `~/.config/ghostty/config`: `theme = Catppuccin Mocha` | [포트](https://github.com/catppuccin/ghostty) |
| Terminal.app | 기본·시작 프로필 `Catppuccin Mocha — Fish`; JetBrainsMono Nerd Font 13pt; Fish 로그인 명령 | [포트](https://github.com/catppuccin/terminal.app) |
| Fish | `fish_config theme choose catppuccin-mocha --color-theme=dark`; Fish 4.9.3 내장 | [포트](https://github.com/catppuccin/fish) |
| Oh My Posh | Homebrew의 `themes/catppuccin_mocha.omp.json` | [공식 테마](https://ohmyposh.dev/docs/themes) |
| LazyVim | `~/.config/nvim/lua/plugins/colorscheme.lua`: `catppuccin-mocha` | [포트](https://github.com/catppuccin/nvim) |
| lazygit | `~/Library/Application Support/lazygit/config.yml` | [포트](https://github.com/catppuccin/lazygit) |
| Yazi | `~/.config/yazi/theme.toml`, 미리보기용 `Catppuccin-mocha.tmTheme` | [Yazi 포트](https://github.com/catppuccin/yazi), [구문 테마](https://github.com/catppuccin/bat) |
| fzf | `~/.config/fish/fzf-catppuccin.fish`; 세션 전역 `FZF_DEFAULT_OPTS` | [포트](https://github.com/catppuccin/fzf) |
| Atuin | `~/.config/atuin/themes/catppuccin-mocha-mauve.toml`, config의 `[theme]` | [포트](https://github.com/catppuccin/atuin) |
| lsd | `~/.config/lsd/config.yaml`의 custom + `colors.yaml` | [포트](https://github.com/catppuccin/lsd) |
| eza | `~/.config/eza/theme.yml` | [포트](https://github.com/catppuccin/eza) |
| Herdr | `~/.config/herdr/config.toml`: 내장 `catppuccin`, auto_switch 꺼짐 | [공식 설정](https://herdr.dev/docs/configuration/) |
| lnav | `~/.config/lnav/config.json`: Mocha 색상으로 직접 작성한 `catppuccin-mocha` | [공식 theme-defs](https://docs.lnav.org/en/latest/config.html#theme-definitions) |
| OpenCode | `~/.config/opencode/tui.json`: 내장 `catppuccin` | [공식 테마](https://opencode.ai/docs/themes/) |

lnav 설정은 Catppuccin 조직의 공식 포트가 아니다. 설치된 lnav의 지원 style 이름에 Mocha 팔레트를 매핑한 로컬 설정이다. jq·yq·fd·rg·Git 등의 ANSI 출력은 터미널 팔레트를 따른다. 개별 도구가 고정 RGB 색상이나 자체 UI를 사용하는 부분까지 모두 바뀌는 것은 아니다. 테마를 적용하지 않은 CLI를 적용 완료로 간주하지 않는다.

Ghostty는 `Cmd+Shift+,`로 설정을 다시 읽거나 새 창에서 확인한다. Terminal.app은 새 프로필로 새 창을 연다. Herdr 기본 서버는 실행 중이 아니어서 설정 reload 대상이 없었으며 다음 실행에 반영된다. 기존 앱의 실행 중인 셸·pane은 종료하지 않았다.

색상이 없으면 `set -q NO_COLOR; and echo NO_COLOR-is-set`을 확인한다. 자동화 환경의 `NO_COLOR`는 그대로 존중한다. 실제 터미널에서 필요할 때만 `set -e NO_COLOR`로 현재 세션의 색상 억제를 해제한다. truecolor 표현은 터미널의 지원 범위를 따른다.

## lsd 별칭과 사용법

```fish
ls          # lsd 기본 목록
ll          # lsd -lah
la          # lsd -A
lt          # lsd --tree
lsd --tree --depth 2
command ls  # 별칭 대신 시스템 ls
```

아이콘은 Nerd Font가 필요하다. 기존 eza도 `eza -lah --git`로 사용할 수 있다. [lsd 상세 매뉴얼](homebrew/lsd.md).

## 재적용·검증·복구

저장소 루트에서 실행한다. 수동으로 설정을 수정했다면 템플릿과 병합한 뒤 재적용한다.

```fish
python3 local/apply-config.py
python3 local/apply-terminal.py
brew bundle check --file=local/Brewfile --no-upgrade
python local/checks/additions.py

set fixture (mktemp -d)
env -i HOME=$HOME USER=$USER PATH=/usr/bin:/bin:/usr/sbin:/sbin TERM=xterm-256color \
    /opt/homebrew/bin/fish -l local/checks/fish-runtime.fish $fixture
# 검증에서 만든 임시 디렉터리만 정리
rm -rf -- $fixture

dscl . -read /Users/(whoami) UserShell
```

`--no-upgrade`는 설치 여부만 확인한다. 이번 작업 중 mise 최신 배포가 갱신되어 일반 `brew bundle check`는 업데이트를 요구했지만 기존 설치는 정상이다. 이번 테마 작업에서는 mise를 업그레이드하지 않았다.

백업은 `~/.local/state/wonder-envy/backups/`의 시각별 폴더다. Terminal 설정은 `terminal-*`에 별도 보관한다. 시스템 로그인 셸 변경에는 관리자 인증을 사용했으며 `/etc/shells`에 Fish를 등록했다. 복구 시 `chsh -s /bin/zsh`와 원하는 이전 Terminal 프로필을 선택하고 파일 백업을 복원한다. 인증 암호는 저장소에 기록하지 않는다.

외부 테마 원본·라이선스·고정 Git tree revision은 [vendor 출처](../local/vendor/README.md)에 있다. [설치 체크리스트](../local/INSTALL-CHECKLIST.md)와 [검증 결과](../local/checks/fish-results.json)를 함께 확인한다.
