# Mac mini로 전달할 자료와 전체 이전 순서

## 정책

2026-09-06 사용자 결정: 기존 버전 재현은 필요 없으며 최신 버전 우선이다. 이 문서의 설치 명령은 새 Mac mini에서 나중에 수행할 절차다. 현재 Mac에서는 조사와 Markdown 작성만 수행했다. OMO 테스트·QA·doctor·앱 동작 시험·추론·빌드·서비스 실행은 수행하지 않는다.

새 Mac mini는 Apple Silicon을 기준으로 설명한다. 실제 장치의 CPU·메모리·저장 용량·macOS 버전·계정 이름은 아직 관측하지 않았다. 최신은 설치 시점의 공식 안정 배포를 뜻하며 문서에 적힌 관측 숫자로 버전을 고정하지 않는다. 공급자가 beta만 제공하거나 지원을 종료한 도구는 별도 예외로 표시한다.

## 1단계: 백업과 목적지 경로 준비

1. 기존 Mac의 원본 파일을 유지한 상태에서 설정과 사용자 자료의 별도 백업을 준비한다. 이 계획 작성 과정에서 원본을 이동·삭제·압축하지 않았다.
2. Mac mini의 실제 사용자 홈과 개발 저장소 위치를 정한다. 기존 사용자명과 같게 만들 필요는 없다.
3. `~/Workspace/Personal`, `~/dotfiles` 또는 실제 dotfiles 원본, Obsidian vault·Google Drive 자료의 새 위치를 기록한다.
4. 현재 문서가 저장된 Google Drive 경로는 한글·공백·계정 식별자를 포함한다. 새 장치의 실제 동기화 경로를 사용하고 기존 절대경로를 추측해서 만들지 않는다.
5. 로컬 복사 작업과 클라우드 동기화가 동시에 같은 설정 파일을 덮어쓰지 않도록 복원 순서를 정한다. 온라인 전용 파일은 원본 다운로드가 끝난 자료만 별도 복사 대상으로 삼는다.

[Apple 마이그레이션 지원 공식 안내](https://support.apple.com/en-us/102613)는 문서·앱·계정·설정을 옮기는 경로를 제공한다. 이 계획은 최신 도구 재설치가 목적이므로 앱·개발환경 전체 복제를 기본으로 삼지 않는다. 마이그레이션 지원을 사용하는 경우 계정 충돌 화면에서 기존 계정 교체를 임의 선택하지 않는다.

## 2단계: 기본 개발 기반 설치

1. 새 Mac에서 지원되는 macOS 업데이트를 적용한다.
2. Apple Command Line Tools를 설치한다. Xcode가 필요한 iOS 작업은 Xcode를 별도로 설치한다.

   ```sh
   xcode-select --install
   ```

3. [Homebrew 공식 설치 안내](https://docs.brew.sh/Installation)의 설치 스크립트를 사용한다.

   ```sh
   /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
   ```

4. 설치자가 출력한 `brew shellenv` 안내를 새 계정의 셸 설정에 한 번 반영한다. Apple Silicon 기본 prefix는 `/opt/homebrew`다.
5. 이전 Mac의 `/opt/homebrew`, `/usr/local`, `.hermes/node`를 시스템 런타임으로 통째 복사하지 않는다.

## 3단계: 셸·터미널·폰트

1. [셸과 터미널](03-shell-terminal.md)의 실제 dotfiles 원본을 먼저 준비한다. `.zshrc` 링크만 복사하면 원본이 없어질 수 있다.
2. Ghostty·파일 검색 도구와 사용하던 Nerd Font를 최신으로 설치한다. 세션·pane 관리는 Herdr로 대체하며 tmux는 설치하지 않는다. Fish·Oh My Posh도 명시적 설치 대상이며 [12 문서](12-fish-posh-herdr-aside-paseo.md)에 따라 Fish 프로필과 Zsh 개발 프로필을 구성한다.
3. Zinit·Oh My Zsh·Powerlevel10k의 역할을 기존 설정에서 읽어 필요한 부분만 구성한다. 여러 초기화 블록을 중복 활성화하지 않는다.
4. 일반 PATH는 새 Homebrew와 사용자 실행 경로를 기준으로 재작성한다. 언어 관리자의 shims는 해당 언어 관리자를 사용할 때만 넣는다.
5. `/tmp` OpenCode 경로, 특정 앱 구버전 경로, 옛 사용자명 경로는 새 `.zshrc`에 가져오지 않는다. `vim → nmin` 등 오타 후보는 원문 보관 후 의도한 명령으로 정리한다.
6. Alacritty cask는 현재 비활성 상태이므로 자동 설치 묶음에서 제외한다. 최신 공식 배포의 해결 여부가 확인된 뒤 설치 경로를 정한다.

## 4단계: 런타임과 일반 CLI

1. [관리자별 설치](01-packages.md)와 [도구 전체 목록](02-package-catalog.md)을 함께 사용한다. 설치 당시의 기록보다 [공식 최신 상태](09-official-sources.md)가 우선한다.
2. Node는 nvm으로 최신 정식 배포를 기본 설치한다. [관리자별 상세 계획](11-runtime-managers.md)에 따라 `.nvmrc`와 버전별 전역 도구를 구성한다. 프로젝트가 요구하면 LTS를 추가하며 기존 Hermes Node 링크는 복원하지 않는다.
3. Python은 pyenv로 최신 정식 버전을 설치하고 uv로 가상환경·의존성을 구성한다. [관리자별 상세 계획](11-runtime-managers.md)의 명시적 인터프리터 지정을 따른다. Ruby는 별도 관리하며 프로젝트 버전 선언·잠금 요구는 유지한다.
4. JDK는 SDKMAN으로 설치·전환한다. Gradle·Flutter·Android SDK도 최신 정식 도구를 설치하되 프로젝트 wrapper·빌드 파일·SDK 선언은 유지한다. Flutter의 기존 prerelease 흔적은 stable로 대체한다.
5. npm·uv·Ruby 전역 CLI를 새 런타임에서 설치해 진입점과 shebang을 재생성한다.
6. Formula 203개를 일괄 수동 설치하지 않는다. 직접 사용하는 도구를 설치하면 현재 공식 의존성 그래프에 따라 라이브러리가 설치된다. 기존에 의존성으로 들어온 `deno`, `gnupg`, `tesseract`, `rustup` 등을 직접 명령으로 사용하는 경우에는 명시적 설치 대상에 추가할 수 있다.
7. 7-Zip 전환에서 `7z`와 `7zz` 등 호출 이름 차이를 스크립트 편집에 반영한다. `sdl2`는 현재 `sdl2-compat` 이름을 참조한다.

## 5단계: 보안·개발 데이터

1. Git 사용자 설정의 의미와 include 파일을 새 경로에 맞게 복원한다. 사용자명·이메일·토큰은 공개 문서에 기록하지 않는다.
2. SSH·GPG·age 키와 mkcert CA는 일반 설정 묶음과 분리한다. 기존 키를 사용할지 새 키를 발급할지는 서비스·서명·복호화 연속성에 따라 결정한다. 복호화에 필요한 원본 키를 삭제하지 않는다.
3. GitHub CLI, Docker registry, AI 계정 및 앱 연결을 새 장치에서 재인증한다. 설정 복사만으로 키체인 항목이 복원됐다고 가정하지 않는다.
4. Docker는 최신 Docker Desktop 한 개를 설치한다. VM 디스크·volume·DB 데이터는 설정 파일과 다른 데이터 이전 작업으로 보존한다. 이 조사에서는 Docker daemon에 접근하지 않았으므로 volume별 내용·용량은 미확인이다.
5. Android 서명 keystore·Gradle 비밀 설정·Maven 서버 자격 증명이 있으면 비밀 자료로 별도 취급한다. 새 런타임 설치 과정에서 이를 폐기하지 않는다.

## 6단계: AI 도구와 플러그인

1. [AI 도구 이전](05-ai-tools.md)에 따라 최신 Codex·Claude Code·OpenCode와 사용할 추가 AI 도구를 설치한다.
2. Gemini의 신규 기본 경로는 Antigravity CLI다. 기존 Gemini 설정을 agy에 파일 전체로 덮어쓰지 않고 공식 migration 안내에 맞춰 의미를 옮긴다.
3. 사용자 `AGENTS.md`, `CLAUDE.md`, 사용자 스킬·명령·규칙을 복원한다. 설치자가 제공하는 시스템 스킬은 최신 설치본을 쓴다.
4. 최신 OMO·OMC를 설치하고 관리 hook·역할·CLI 링크를 설치자에게 맡긴다. OMO 테스트 기능은 사용하지 않는다.
5. Orca·Aside·Pencil 등 MCP 서버를 제공하는 앱을 설치한 뒤 명령 경로와 hook 경로를 다시 연결한다.
6. 환경 변수 키 이름에 맞춰 인증값은 비밀 저장소에서 별도로 공급한다. 과거 승인 해시·프로젝트 신뢰·소켓·캐시는 자동 이전하지 않는다.
7. `codegraph` 세 구현의 소비자를 구분한다. MCP가 요구하는 구현을 명시하고 예전 OMO 캐시 버전 경로를 제거한 새 설정을 만든다.

## 7단계: 앱 CLI와 개인 도구

이 단계의 실제 운영 형태는 [Orca/Paseo + Herdr 작업 구성](13-workflow-orca-paseo-herdr.md)을 따른다. Yazi·Neovim·lazygit은 공통 필수이며 각 도구의 현재 경로를 앱이 선택한 실제 worktree와 맞춘다.

1. [앱 CLI와 개인 도구](06-app-cli-custom.md)에 따라 VS Code·Orca·Aside·cmux·Ollama·LM Studio를 설치한다. Herdr·Paseo와 Aside 앱/CLI 분리 설치는 [추가 도구 가이드](12-fish-posh-herdr-aside-paseo.md)를 함께 따른다. Paseo 데스크톱과 별도 headless daemon을 같은 홈으로 중복 시작하지 않는다.
2. 확장은 이름을 기준으로 최신 버전을 설치한다. 앱 내부 CLI 래퍼는 앱 설치에서 제공받는다.
3. sensai·spring-create 등 출처가 미확인인 항목은 개인 원본 확보까지 이전 보류 목록으로 유지한다.
4. 모델 가중치·문서·개인 스킬·미커밋 작업·worktree 자료는 각각 사용자 데이터로 옮긴다.
5. LaunchAgents는 연결된 앱·실행 파일·새 경로가 준비된 이후 필요한 자동화만 재등록한다. 기존 plist 전체를 먼저 로드하지 않는다.

## 전달 자료 분류표

아래는 복사 명령이 아닌 보관·복원 정책이다. 원본 설정에 비밀값이 섞인 파일은 비민감 항목만 선별한다.

| 분류 | 기존 위치 | Mac mini 처리 |
| --- | --- | --- |
| 셸 원본 | `.zshrc`가 가리키는 dotfiles, `.zprofile`, `.zshenv`, `.p10k.zsh` | 원본 파일 보관, 최신 도구 경로로 편집한 뒤 링크 구성 |
| 이전 제외 | `.tmux.conf`, tmux 플러그인·자동 시작·attach 설정 | 새 Mac에 복원하지 않음; Ghostty + Herdr 사용 |
| 터미널·에디터 | `~/.config/{ghostty,alacritty,fish,nvim,yazi,cmux}`, VS Code User | 사용자 선택 병합, 오래된 runtime 제외 |
| 사용자 지침 | `~/.codex/AGENTS.md`, `~/.claude/CLAUDE.md`, `.agents/skills` | 사용자 작성 원본 보관·복원 |
| AI 설정 | `.codex/config.toml`, `.claude/settings.json`, `.claude.json`, `.gemini/settings.json` | 비밀값·절대경로·구 스키마 분리 후 선별 재작성 |
| 프레임워크 설정 | `.omo`, `.omc`, Claude/Codex plugin 등록 | 사용자 선호 보관, 설치 관리 파일·캐시는 최신 배포로 재생성 |
| 인증·암호 키 | `.ssh`, `.gnupg`, `.age`, 각 도구 auth·credentials·`.env` | 암호화된 별도 자료 또는 새 장치 로그인; 공개 MD 제외 |
| AWS 설정 흔적 | `~/.aws` | 디렉터리 존재만 확인. profiles·credentials는 별도 식별·인증, AWS CLI 설치는 이번 목록에서 확정되지 않음 |
| Maven·Gradle | `.m2`, `.gradle` | 사용자 settings·init·properties와 의존성 캐시를 구분; 인증 포함 파일 별도 보관 |
| 프로젝트 자료 | `~/Workspace`, Obsidian vault, 앱 worktrees | 소스·잠금 파일·미커밋 자료 보관, 전체 Git 작업 상태를 원격 clone만으로 대체하지 않음 |
| 대화·기억 | Codex memories·sessions, Claude projects, Hermes memories, OpenCode DB | 설정과 별도 사용자 자료로 보존; 새 앱 DB에 무조건 덮어쓰기 금지 |
| 로컬 모델 | `.ollama/models`, `.lmstudio/models` | 저장 용량에 따라 별도 전달 또는 재다운로드 |
| 재생성 자료 | node_modules, venv, Cellar, plugin cache, SDK 다운로드 캐시 | 최신 도구/프로젝트 설치 절차에서 재생성 |
| 실행 상태 | socket, pid, lock, shell snapshot, 임시 `/tmp` 경로 | 활성 환경에 복원하지 않음 |
| 예약 작업 | `~/Library/LaunchAgents` | 사용자 의도 보존, 새 경로와 앱 준비 후 재등록 |

## 범위와 남은 확인 사항

- 현재 Mac: macOS 26.5.2, build 25F84, arm64를 시스템 정보에서 확인했다.
- Homebrew의 모든 Cellar Formula 203종과 Caskroom 13개를 조사했다. 설치된 버전 디렉터리가 복수일 수 있다.
- [실행 파일 대응표](08-executable-map.md)는 지정한 6개 전역 실행 디렉터리의 942개 항목을 기록한다. 고유 도구 942종이라는 뜻은 아니다.
- 앱 번들 내부·언어별 가상환경·프로젝트 `node_modules/.bin`·SDK·macOS 기본 명령은 위 942개와 별도다. 일부 앱 포함 CLI는 06 문서에 추가했다.
- Python/Ruby의 모든 프로젝트별 라이브러리, 모든 저장소별 설정, 디스크 전체 실행 파일, 로그인 키체인, 실제 장치 권한과 동작을 전수 조사한 것은 아니다.
- 새 Mac의 설치·서비스·모델 실행이 완료됐다는 의미가 아니다. 테스트를 생략한 분석 문서이며 미확인 상태를 그대로 남긴다.
