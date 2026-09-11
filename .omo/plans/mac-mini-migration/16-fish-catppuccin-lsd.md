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
