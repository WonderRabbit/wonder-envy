# Mac mini 개발 환경 이전 안내

현재 Mac을 읽기 전용으로 조사한 **최신 버전 우선 이전 계획**이다. 작성일은 2026-09-06이다. 실제 설치·설정 변경·테스트·OMO QA는 수행하지 않았다.

처음에는 [전체 계획](.omo/plans/mac-mini-migration.md)과 [단계별 이전 순서](.omo/plans/mac-mini-migration/07-transfer-order.md)를 읽으면 된다.

터미널 구성은 **Ghostty + Herdr**로 확정했다. Ghostty는 필수 설치 대상이며 tmux와 tmux 설정·플러그인은 새 Mac의 설치·복원 대상에서 제외한다.

개발 작업은 **Orca + Herdr 또는 Paseo + Herdr**를 중심으로 Yazi·Neovim·lazygit을 함께 사용한다. [전체 작업 구성](.omo/plans/mac-mini-migration/13-workflow-orca-paseo-herdr.md)에 역할·사용 순서·worktree 관리 기준을 정리했다.

## 카테고리별 문서

| 구분 | 문서 |
| --- | --- |
| 패키지 관리자·전역 도구 | [Homebrew·npm·Python·Ruby](.omo/plans/mac-mini-migration/01-packages.md) |
| 전체 설치 카탈로그 | [Formula 203종·Caskroom 13개 개별 절차](.omo/plans/mac-mini-migration/02-package-catalog.md) |
| 셸·터미널·에디터 | [Zsh·dotfiles·터미널·Neovim](.omo/plans/mac-mini-migration/03-shell-terminal.md) |
| 런타임·SDK·인증 | [개발 환경·Docker·Git·SSH·GPG](.omo/plans/mac-mini-migration/04-dev-security.md) |
| LLM·에이전트 설정 | [Codex·Claude Code·OMO·OMC·MCP·스킬](.omo/plans/mac-mini-migration/05-ai-tools.md) |
| 앱 CLI·개인 도구 | [Orca·Aside·cmux·VS Code·로컬 LLM](.omo/plans/mac-mini-migration/06-app-cli-custom.md) |
| 전달과 복원 순서 | [7단계 이전 절차·설정과 인증 분류](.omo/plans/mac-mini-migration/07-transfer-order.md) |
| 실행 파일 목록 | [942개 명령 경로와 설치 원본](.omo/plans/mac-mini-migration/08-executable-map.md) |
| 공홈·최신 배포 상태 | [공식 API·설치 문서·지원 종료와 이름 변경](.omo/plans/mac-mini-migration/09-official-sources.md) |
| 추가 Python CLI | [IPython·Jupyter·debugpy·Pygments](.omo/plans/mac-mini-migration/10-python-user-tools.md) |
| 런타임 관리자 설치 | [SDKMAN·nvm·pyenv·uv 설치와 프로젝트별 버전 제어](.omo/plans/mac-mini-migration/11-runtime-managers.md) |
| 추가 셸·에이전트 도구 | [Fish·Oh My Posh·Herdr·Aside·Paseo 상세 설치](.omo/plans/mac-mini-migration/12-fish-posh-herdr-aside-paseo.md) |
| 통합 개발 작업 구성 | [Orca/Paseo + Herdr + Yazi·Neovim·lazygit](.omo/plans/mac-mini-migration/13-workflow-orca-paseo-herdr.md) |

## 읽을 때 알아둘 점

- 기존 버전은 설치 흔적의 기록이다. 새 Mac은 설치 시점 최신 정식 배포를 우선하며, 프로젝트가 요구하는 버전만 예외로 추가한다.
- 일반 설정, 비밀값, 대화·메모리, 모델·DB 자료, 재생성 캐시를 구분했다. 비밀값 자체는 문서에 담지 않았다.
- CLI 실행 파일 개수는 제품 개수가 아니다. 보조 명령과 중복 링크가 포함된다.
- 디스크 전체·모든 프로젝트별 가상환경을 전수 조사했다는 의미는 아니다. 조사 경계·개인 도구 출처 미확인·웹 수집 실패는 각 문서에 남겼다.
- 설치 경로가 충돌할 때는 09의 공식 최신 상태와 각 도구의 현재 공식 안내를 우선한다.
