# 설치된 앱과 폰트

`/Applications`의 실제 앱 목록을 기준으로 작성했다. 아래 앱을 설치했다는 사실이 로그인·권한·원격 연결까지 완료됐다는 뜻은 아니다. 앱 실행은 Finder 또는 `open -a "앱 이름"`을 사용한다.

| 앱 / 버전 | 기본 사용 방법 | 공식 링크 |
| --- | --- | --- |
| Ghostty 1.3.1 | `open -a Ghostty`; Fish에서 Node·Python·Java 사용, Catppuccin Mocha | [문서](https://ghostty.org/docs) |
| Aside 1.0.910.1 | `open -a Aside`; 브라우저에서 필요한 계정 로그인 | [공식 사이트](https://aside.com/) |
| Visual Studio Code 1.137.0 | `code .`으로 현재 프로젝트 열기, Python은 프로젝트 `.venv` 선택 | [문서](https://code.visualstudio.com/docs) |
| Docker Desktop 4.90.0 | `open -a Docker`; 최초 설정을 완료한 뒤 컨테이너 사용 | [Mac 설치](https://docs.docker.com/desktop/setup/install/mac-install/) |
| Orca 1.4.192 | `open -a Orca`; 프로젝트와 작업 폴더를 선택, 해당 worktree에서 수동 도구 사용 | [문서](https://www.onorca.dev/docs) |
| Paseo 0.7.2 | `open -a Paseo`; 앱에서 로컬 프로젝트·provider 선택 | [문서](https://paseo.sh/docs) |
| ChatGPT 26.901.51231 | `open -a ChatGPT`; 앱에서 사용할 대화·작업 선택 | [공식 도움말](https://help.openai.com/) |
| Claude 1.52386.0 | `open -a Claude`; 로그인 후 대화 시작, Claude Code CLI와 구분 | [공식 도움말](https://support.claude.com/) |
| Discord 0.0.410 | `open -a Discord`; 서버·채널 선택 후 대화·통화 | [공식 지원](https://support.discord.com/) |
| Magnet 3.0.7 | `open -a Magnet`; 메뉴 막대의 창 배치 메뉴 사용 | [공식 사이트](https://magnet.crowdcafe.com/) |
| Raycast 2.3.0.0 | `open -a Raycast`; 설정한 호출 키로 앱·명령 검색 | [문서](https://manual.raycast.com/) |
| Remote Desktop 3.10 | `open -a "Remote Desktop"`; 접근 권한이 있는 Mac을 등록해 관리 | [Apple 사용 설명서](https://support.apple.com/guide/remote-desktop/welcome/mac) |
| Safari 26.6.2 | `open -a Safari`; 주소창에 URL 입력 | [Apple 사용 설명서](https://support.apple.com/guide/safari/welcome/mac) |
| Zen 1.21.16b | `open -a Zen`; 탭·workspace로 브라우징. 기존 beta 설치본 유지 | [문서](https://docs.zen-browser.app/) |
| Zoom 7.1.5 | `open -a zoom.us`; 회의 링크 또는 회의 ID로 참가 | [공식 지원](https://support.zoom.com/) |
| JetBrainsMono Nerd Font 3.5.1 | Ghostty의 `font-family = JetBrainsMono Nerd Font`; CLI가 아닌 폰트 자료 | [Nerd Fonts](https://www.nerdfonts.com/), [JetBrains Mono](https://www.jetbrains.com/lp/mono/) |

Ghostty·Herdr·LazyVim에서 같은 폰트가 보이는지 확인할 때 터미널이 실제 선택한 폰트와 아이콘 fallback을 확인한다. 폰트를 설치하는 것과 앱의 기본 폰트를 선택하는 것은 별도 단계다. 기존 앱의 인증·자료는 이 설정 작업에서 복사하거나 초기화하지 않았다.
