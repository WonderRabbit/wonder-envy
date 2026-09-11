# Mac mini 개발 환경 이전 계획

## 핵심 요약

현재 Mac의 설치 흔적·설정·공식 배포 정보를 바탕으로 최신 도구를 새 Mac mini에 설치하고 사용자 설정을 선별 복원하는 계획이다. 기존 버전 고정 재현은 하지 않는다. 문서 작성일은 2026-09-06이다.

Homebrew Formula 203종, Caskroom 13개, 주요 전역 실행 디렉터리 942개 항목과 사용자 Python 경로 10개 항목을 기록했다. 실행 파일 수는 고유 제품 수가 아니다. Codex·Claude Code·OMO·OMC·OpenCode·Antigravity, 셸·런타임·MCP·스킬·인증 이전도 함께 다룬다.

실제 설치·설정 변경·테스트·OMO QA는 하지 않았다. 아래 체크박스는 새 Mac의 향후 이전 작업이며 현재 완료됐다는 표시가 아니다.

## 문서 안내

| 문서 | 내용 |
| --- | --- |
| [01 관리자와 전역 도구](mac-mini-migration/01-packages.md) | Homebrew·npm·uv·pipx·Ruby 설치 순서 |
| [02 도구별 전체 카탈로그](mac-mini-migration/02-package-catalog.md) | Formula 203종·Cask 13개 각각의 관측 버전·설치 경로·공홈·단계 |
| [03 셸과 터미널](mac-mini-migration/03-shell-terminal.md) | Zsh·dotfiles·플러그인·터미널·Neovim·Yazi |
| [04 개발 환경과 보안](mac-mini-migration/04-dev-security.md) | Python·Ruby·JDK·Rust·Android·Flutter·Docker·SSH·GPG |
| [05 AI 도구와 설정](mac-mini-migration/05-ai-tools.md) | Codex·Claude·OMO·OMC·MCP·공유 스킬·추가 AI 흔적 |
| [06 앱 CLI와 개인 도구](mac-mini-migration/06-app-cli-custom.md) | Orca·Aside·cmux·VS Code·Ollama·LM Studio·agy·개인 도구 |
| [07 전체 이전 순서](mac-mini-migration/07-transfer-order.md) | 새 Mac에서 따라갈 순서·전달 자료·인증·캐시 분류 |
| [08 실행 파일 대응표](mac-mini-migration/08-executable-map.md) | 6개 전역 디렉터리의 명령과 링크 원본 942개 |
| [09 공식 최신 배포 근거](mac-mini-migration/09-official-sources.md) | 216개 Homebrew API 조회·공홈 조회·이름 변경·지원 상태 |
| [10 사용자 Python 도구](mac-mini-migration/10-python-user-tools.md) | IPython·Jupyter·debugpy·Pygments 및 추가 런타임 흔적 |
| [11 런타임 관리자 설치](mac-mini-migration/11-runtime-managers.md) | SDKMAN·nvm·pyenv·uv 공식 설치·프로젝트별 전환·업데이트·MCP 연결 |
| [12 추가 도구 설치](mac-mini-migration/12-fish-posh-herdr-aside-paseo.md) | Fish·Oh My Posh·Herdr·Aside 앱/CLI·Paseo 데스크톱/headless |
| [13 통합 개발 작업 구성](mac-mini-migration/13-workflow-orca-paseo-herdr.md) | Orca/Paseo + Herdr와 Yazi·Neovim·lazygit의 역할·실제 작업 경로·사용 순서 |

07의 순서로 읽고, 각 단계에서 01~06·10의 도구별 절차와 02를 참조한다. 설치 채널·지원 상태가 충돌하면 최신 공식 조회를 기록한 09와 각 도구 공식 문서를 우선한다.

## 범위와 기본 결정

- 출발 장치: macOS 26.5.2, build 25F84, arm64. 대상 장치의 실제 사양·홈 경로는 미관측이다.
- 기본 버전: 설치 당시 최신 공식 정식 배포. Node/JDK의 LTS는 프로젝트·운영 요구가 있을 때 호환성 선택으로 사용한다.
- 확정 관리자: Java는 SDKMAN, Node는 nvm, Python 인터프리터는 pyenv, Python 가상환경·패키지는 uv. 상세 설치·설정은 11 문서를 우선한다.
- 확정 터미널 구성: Ghostty를 설치하고 세션·pane 관리는 Herdr로 대체한다. tmux·설정·플러그인·자동 attach는 설치 및 복원 대상에서 제외한다. 기존 설치 관측 기록은 보존한다.
- 개발 작업 구성: Orca + Herdr 또는 Paseo + Herdr를 사용하고 Yazi·Neovim·lazygit을 공통 필수 도구로 설치한다. 작업별 앱 관리 주체와 worktree 경로를 구분하는 13 문서를 따른다.
- 추가 설치 범위: Fish·Oh My Posh·Herdr·Aside 브라우저와 CLI·Paseo. Fish와 nvm·SDKMAN의 셸 차이, 앱과 daemon 운영 방식은 12 문서를 따른다. 새 도구를 기존 설치 관측 숫자에 합산하지 않는다.
- 예외: AeroSpace의 공식 배포는 Beta 표기가 있으므로 안정판으로 오인하지 않는다. 지원 종료·비활성 패키지는 자동 복원하지 않는다.
- 기본 전략: 최신 프로그램 설치 → 사용자 설정 의미 복원 → 새 경로 적용 → 계정 연결. 기존 프로그램 디렉터리 통째 복사는 기본 전략이 아니다.
- 원본 보존: 개인키·대화·메모리·미커밋 자료·모델·DB는 재생성 캐시와 구분한다.
- 금지: 현재 시스템 변경, 도구 설치·업데이트, 원본 삭제, 비밀값 문서화, 테스트·빌드·런타임 QA·OMO 테스트 기능.

## 조사 근거와 한계

설치 영수증·package 메타데이터·파일과 링크·설정 키를 읽었다. 공식 Homebrew API 216건 중 212건 HTTP 200, 4건 404가 기록되었고, 동명의 다른 제품인 core Orca는 적용에서 제외했다. vendor tap과 대체 이름을 별도로 조사했다. 직접 설치 항목의 공홈·설치 문서 60건 중 58건은 응답을 확보했고 2건은 수집 실패로 남겼다. 추가 AI·앱 공식 문서는 해당 절에 연결했다.

공식 API의 stable 필드는 Homebrew 제공 버전이다. upstream 전체 채널 중 가장 최근 버전이라는 보장은 아니다. 공홈 링크가 있다는 사실과 페이지 본문을 실제 열람했다는 사실을 구분했다.

프로젝트별 가상환경의 모든 패키지·모든 저장소별 설정·디스크 전체 실행 파일·Keychain·실행 중 서비스 데이터는 전수 수집 범위가 아니다. sensai 등 개인 배포 출처 미확인은 해당 문서에 남겼다. 이 계획을 장치 이전 성공 또는 실행 가능성 시험 결과로 해석하지 않는다.

## 우선 반영할 발견 사항

| 발견 | 이전 처리 |
| --- | --- |
| Node가 Homebrew·/usr/local·Hermes·n에 공존 | 사용자 결정에 따라 nvm으로 관리하고 전역 도구 재설치 |
| Gemini CLI 공식 API deprecated·unsupported | Antigravity CLI를 신규 기본 경로로 계획, 기존 설정은 선별 이관 |
| Alacritty 공식 cask disabled | 자동 설치 보류, 현재 사용하던 Ghostty를 우선 구성 |
| core orca는 Plotly 제품 | `stablyai/orca/orca` 사용 |
| Codex codegraph는 OMO 4.11.0 경로 참조, 현재 링크는 4.19.4 | 최신 OMO가 생성한 경로로 MCP 재등록 |
| ~/.zshrc에 /tmp OpenCode 경로 4개 | 새 설정에서는 제외 |
| Flutter cask 디렉터리와 SDK 내부 버전이 다름 | 최신 stable 신규 설치 |
| Cursor·Kiro·spring 도구 링크 대상 없음 | 링크 복사 제외, 원본/앱 확보까지 보류 |
| docker·docker-desktop 설치 흔적 중복 | 최신 Docker Desktop 하나로 설치 |
| Python 3.9 사용자 CLI 별도 존재 | 최신 Python 도구 환경에서 진입점 재생성 |

## 이전 작업과 의존 순서

### 첫 단계: 기반과 설정 원본

- [ ] 1. 자료 보관과 목적지 경로를 준비한다.
  - 참고: 07의 1단계 및 전달 자료 분류표.
  - 산출 상태: 새 홈·저장소·동기화 경로, 사용자 자료 보관 범위가 정해져 있다.
  - 제한: 원본 삭제·계정 강제 교체 없음.

- [ ] 2. macOS 개발 도구와 Homebrew를 설치한다.
  - 선행: 1. 참고: 07의 2단계, 01.
  - 산출 상태: Apple Silicon 기본 설치 prefix와 셸 등록 위치가 정해져 있다.
  - 제한: 구 Cellar·/usr/local 전체 복원 없음.

- [ ] 3. 셸·터미널·폰트·사용자 dotfiles를 구성한다.
  - 선행: 2. 참고: 03, 06의 cmux, 02의 폰트·터미널.
  - 산출 상태: 최신 도구와 새 경로를 참조하는 사용자 설정이 구성되어 있다.
  - 제한: 임시 PATH·오래된 hook·중복 초기화 자동 복원 없음.

### 두 번째 단계: 개발 도구와 인증

- [ ] 4. 최신 런타임과 일반 CLI를 설치한다.
  - 선행: 2. 참고: 01·02·04·09·10.
  - 산출 상태: 계속 사용할 도구가 최신 채널로 설치되며 프로젝트별 버전 예외가 분리되어 있다.
  - 제한: 구버전 숫자 재현·전이 의존성 전부 수동 설치 없음.

- [ ] 5. Git·SSH·GPG·Docker·SDK 설정과 필요한 사용자 데이터를 옮긴다.
  - 선행: 1·4. 참고: 04, 07의 5단계.
  - 산출 상태: 공개 설정과 비밀 자료·영속 데이터가 구분되어 새 경로에 반영되어 있다.
  - 제한: 키 폐기·볼륨 삭제·DB 초기화 없음.

### 세 번째 단계: AI 도구와 앱 연결

- [ ] 6. 최신 AI CLI와 사용자 지침을 구성한다.
  - 선행: 3·4. 참고: 05·06.
  - 산출 상태: CLI·사용자 규칙·공유 스킬·계정 연결이 새 설치 기준으로 구성되어 있다.
  - 제한: auth 파일·구 plugin cache 전체 복원 없음.

- [ ] 7. OMO·OMC·MCP·앱 hook을 최신 구조로 연결한다.
  - 선행: 6·8. 참고: 05의 MCP·절대경로·Codegraph 절.
  - 산출 상태: 각 소비자가 올바른 새 실행 파일과 사용자 자료 경로를 가리킨다.
  - 제한: OMO 테스트·doctor·QA·자동 검토 없음.

- [ ] 8. 앱 CLI와 개인 도구·모델 자료를 정리한다.
  - 선행: 3·4. 참고: 06, 07의 7단계.
  - 산출 상태: 최신 앱 포함 CLI를 사용하며 출처 미확인 도구와 대용량 사용자 자료는 별도 목록에 남는다.
  - 제한: 사라진 링크 대상이 복원됐다고 추정하지 않음.

위 작업은 1 → 2 → 3·4 → 5·6·8 → 7 순서로 진행한다. 번호 7은 앱 설치인 8도 선행해야 한다. 각 항목의 산출 상태는 향후 이전 완료를 기록할 기준이며 이번 조사에서 실행한 검증이 아니다.

## 테스트와 변경 관리

테스트 전략은 없음이다. 사용자 요청에 따라 스킬 템플릿의 테스트·자동 검토·수동 QA·최종 검증 wave는 적용하지 않는다. 체크박스 수는 이전 작업 8개, QA 작업 0개다. commit·PR·배포도 범위가 아니다.

계획 산출물은 현재 디렉터리의 Markdown뿐이다. 실제 Mac mini 설치는 이 계획을 읽고 새 장치에서 수행하는 별도 작업이다.
