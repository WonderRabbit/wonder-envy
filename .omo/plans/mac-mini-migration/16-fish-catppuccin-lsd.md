# 16. Fish 기본 셸·Catppuccin·lsd 적용

작성일: 2026-09-11. 사용자 요청에 따라 기존 Zsh 중심 정책을 변경한다. 기존 런타임과 도구는 재사용한다. 세부 진행 상태는 [설치 체크리스트](../../../local/INSTALL-CHECKLIST.md)가 기준이다.

## 실행 순서

1. 이 계획과 체크리스트를 먼저 커밋하고 main에 푸시한다.
2. 기존 설정을 백업하고 lsd와 필요한 Fish 연동 파일을 설치한다.
3. Fish에서 nvm·Node·npm, SDKMAN·Java, pyenv·Python, uv가 동작하도록 구성한다.
4. macOS 로그인 셸, Terminal, Ghostty, Herdr의 새 터미널을 Fish로 설정한다. 시스템 셸 등록·계정 변경에 OS 인증이 필요하면 사용자 설정을 먼저 적용하고 인증 필요 상태를 명시한다.
5. Catppuccin Mocha를 적용하고 기능 검증 후 계획·체크리스트·menual 문서를 갱신해 커밋·푸시한다.

## Fish 및 런타임

- Homebrew Fish 경로 `/opt/homebrew/bin/fish`를 사용한다. 명시적으로 실행하는 Zsh 스크립트는 유지한다.
- Herdr의 기존 `/bin/zsh` 기본값과 Fish의 `dev -> zsh` 우회 설정을 수정한다.
- nvm은 공식적으로 Fish 문법을 지원하지 않는다. 기존 `~/.nvm`을 유지하고 Bass로 Bash 환경 변경을 Fish에 전달한다. 별도 Node 관리자를 설치하지 않는다.
- SDKMAN도 Bash 연동을 통해 `sdk use`, `sdk current`, Java 환경을 Fish에 전달한다. Bash 자체는 연동용으로 유지한다.
- pyenv init은 Fish 문법을 사용한다. uv·uvx와 사용자 CLI 경로를 유지한다.
- mise는 task 전용이며 Fish 런타임 자동 activation 차단을 유지한다.
- 깨끗한 환경의 새 Fish에서 실행 경로·버전·버전 전환·간단한 프로그램 실행을 확인한다.

## 테마와 lsd

- 사용자 세부 flavor 지정이 없으므로 어두운 Catppuccin **Mocha**, accent **Mauve**를 기본으로 선택한다.
- Ghostty, Fish 구문 강조, Oh My Posh, LazyVim, lazygit, Yazi(미리보기 포함), fzf, Atuin, lsd에 공식 테마/내장 테마를 우선 적용한다.
- Terminal.app도 새 프로필에 Mocha 팔레트를 적용한다. Herdr 및 기타 TUI는 지원 설정을 조사한 뒤 지원되는 범위만 반영한다.
- lnav 등 추가 테마 지원 도구는 공식 지원 여부를 확인한다. jq·yq·fd·rg·Hurl 등의 단순 CLI는 별도 테마가 없으면 터미널 팔레트를 사용하고 한계를 문서화한다.
- `lsd`를 Brewfile에 추가하고 Fish에서 `ls`, `ll`, `la`, `lt`를 제공한다. 기존 eza 설치는 유지한다.
- 테마 출처·라이선스·고정 revision을 기록한다. 인증 파일이나 개인 이력을 저장소에 추가하지 않는다.

## 완료 기준

- 새 터미널이 Fish로 시작하며 Node·Python·Java·uv 및 관리 명령이 Fish에서 실행된다.
- Catppuccin 설정 로드에 오류가 없고 lsd가 파일 목록·아이콘을 출력한다.
- 설정 재적용이 기존 LazyVim·테마 파일을 이전 구성으로 덮어쓰지 않는다.
- 남은 OS 인증/GUI 확인이 있다면 완료로 표시하지 않는다.
- 변경된 계획과 설치 결과가 원격 main에 반영된다.

## 공식 참고

- [Catppuccin 포트](https://github.com/catppuccin)
- [Fish 기본 셸](https://fishshell.com/docs/current/tutorial.html#switching-to-fish)
- [nvm Fish 지원 안내](https://github.com/nvm-sh/nvm#fish)
- [Bass](https://github.com/edc/bass)
- [SDKMAN 설치](https://sdkman.io/install)
- [lsd](https://github.com/lsd-rs/lsd)
- [Catppuccin Fish](https://github.com/catppuccin/fish)
- [Catppuccin lsd](https://github.com/catppuccin/lsd)

## 실제 적용과 계획 보완 (2026-09-11)

- 계획을 `7598005`로 먼저 커밋·푸시한 뒤 설치했다. lsd 1.2.0을 추가했고 기존 런타임을 유지했다.
- macOS 계정 셸 변경은 일반 권한으로 거부되어 OS 관리자 인증으로 완료했다. `/etc/shells`와 계정 UserShell을 확인했다.
- Terminal 기본·시작 프로필은 `Catppuccin Mocha — Fish`, Ghostty·Herdr 기본 셸은 Fish로 적용했다. Terminal 프로필은 Nerd Font 13pt도 지정한다.
- Bass 원본을 고정 revision·LICENSE와 보관하고 적용 함수에 system Python 사용·실패 임시 파일 정리를 추가했다. pyenv shim이 내부 Python 실행으로 PATH 뒤로 밀리는 실제 문제를 해결했다.
- SDKMAN은 관리 명령마다 init이 기본 Java를 다시 선택하므로 Fish의 기존 JAVA_HOME·PATH를 보존한 뒤 요청 명령을 실행한다. `sdk use` 이후 `sdk current`를 실행해도 세션 선택이 유지됨을 확인했다.
- Fish·Ghostty·Oh My Posh·Herdr·OpenCode는 내장 Catppuccin을 선택했다. 다른 포트는 원본과 LICENSE를 `local/vendor/`에 고정했다. OpenCode의 설정 위치는 현재 공식 안내에 따라 `tui.json`이다.
- lnav 공식 Catppuccin 포트가 확인되지 않아 지원 schema에 Mocha 색상을 직접 지정했다. 단순 CLI는 ANSI 팔레트를 따르며 고정 RGB 출력까지 변경했다고 주장하지 않는다.
- fzf 공식 예제의 universal export는 재적용 시 사용자 영속 변수를 누적 변경하지 않도록 global export로 조정했다.
- TUI 검증 도구는 controlling PTY·대화형 Fish를 사용해야 했다. 자동화 환경의 NO_COLOR는 검증 프로세스에서만 해제했다. 실제 셸은 사용자 NO_COLOR를 존중한다.
- Herdr 기본 서버가 실행 중이지 않아 reload 대상은 없었다. 디스크 설정은 다음 실행에 적용되며 사용자 세션을 강제로 시작/종료하지 않았다.
- 작업 중 mise의 새 배포가 나타나 일반 Brewfile check는 업데이트를 요구했다. 설치 여부 확인은 `--no-upgrade`로 통과했고 mise 업그레이드는 이번 변경에 포함하지 않았다.

검증: [Fish 런타임 결과](../../../local/checks/fish-results.json), [기존 CLI 통합 결과](../../../local/checks/latest-results.json). 현재 운영 안내는 [Fish·테마 매뉴얼](../../../menual/fish-and-themes.md)이다.
