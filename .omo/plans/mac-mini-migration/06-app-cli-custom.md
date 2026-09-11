# 앱에 포함된 CLI와 개인 도구 이전

관측일: 2026-09-06. 파일·링크·설치 메타데이터와 공식 웹 문서를 읽은 결과다. 아래 명령은 새 Mac mini용 계획이며 실행하지 않았다. 설치 버전을 고정하지 않고 최신 안정 배포를 우선한다.

## Visual Studio Code와 확장

현재 `/Applications/Visual Studio Code.app`, `~/Library/Application Support/Code/User/settings.json`, `snippets/`, `~/.vscode/extensions/`가 존재한다. 확장 디렉터리에는 여러 구버전이 공존하므로 디렉터리 개수와 활성 확장 개수는 다르다.

1. [공식 macOS 설치 문서](https://code.visualstudio.com/docs/setup/mac)에서 Apple Silicon 최신 stable 앱을 받아 `/Applications`에 설치한다.
2. 명령 팔레트에서 `Shell Command: Install 'code' command in PATH`를 선택한다. 앱의 `Contents/Resources/app/bin/code`를 따로 복사하지 않는다.
3. 기존 `settings.json`과 `snippets/`를 새 사용자 설정에 병합한다. 기존 `keybindings.json`은 관측되지 않았으므로 있다고 가정하지 않는다.
4. 아래 확장 ID를 Marketplace에서 최신 버전으로 설치한다. 버전별 확장 디렉터리는 복사하지 않는다. Settings Sync를 사용하는 경우 중복 수동 설치를 피한다.
5. `globalStorage/`, `workspaceStorage/`, `History/`는 설정과 분리된 로컬 상태다. 로그인은 새 장치에서 다시 진행한다.

관측된 확장 ID:

```text
hollowtree.vue-snippets
ms-azuretools.vscode-containers
ms-ceintl.vscode-language-pack-ko
ms-python.debugpy
ms-python.python
ms-python.vscode-pylance
ms-python.vscode-python-envs
ms-toolsai.jupyter
ms-toolsai.jupyter-keymap
ms-toolsai.jupyter-renderers
ms-toolsai.vscode-jupyter-cell-tags
ms-toolsai.vscode-jupyter-slideshow
ms-vscode-remote.remote-containers
ms-vscode.makefile-tools
naumovs.color-highlight
openai.chatgpt
tonybaloney.vscode-pets
vue.volar
```

## Orca와 orca CLI

현재 `/opt/homebrew/bin/orca`는 `/Applications/Orca.app/Contents/Resources/bin/orca`를 참조한다. `~/.orca/keybindings.json`, `~/.orca/agent-hooks/`도 존재한다. 같은 이름의 다른 오픈소스·과학 계산 제품과 혼동하지 않는다.

1. [Orca 공식 설치 문서](https://www.onorca.dev/docs/install)에 따라 `brew install --cask stablyai/orca/orca`로 최신 stable을 설치한다. RC는 기본 선택이 아니다.
2. Codex·Claude Code와 셸 설정을 먼저 준비한다. Orca의 첫 실행은 기존 `~/.claude`, `~/.codex`, Ghostty 설정 가져오기를 제안하므로, 이전 설정을 정리한 뒤 가져온다.
3. `keybindings.json`의 사용자 단축키와 `agent-hooks/`에서 직접 작성한 항목을 새 설치의 설정 구조에 맞춰 옮긴다. 오래된 앱 캐시나 앱 번들 속 CLI 파일을 덮어쓰지 않는다.
4. 프로젝트는 새 Mac의 경로로 등록한다. 옛 worktree·터미널 식별자·실행 중 프로세스를 새 환경의 유효한 상태로 간주하지 않는다.
5. GitHub·AI 계정과 macOS 접근 권한은 새 장치에서 다시 설정한다. 이 조사에서는 Orca CLI·앱을 실행하거나 managed worktree를 변경하지 않았다.

## Aside와 aside CLI

후속 공식 배포 조사로 브라우저 cask와 별도 CLI 설치 경로를 확인했다. [추가 도구 가이드 5절](12-fish-posh-herdr-aside-paseo.md)의 상세 안내가 아래 초기 조사보다 우선한다.

현재 `~/.local/bin/aside`는 `~/.aside/cli/Aside CLI.app/Contents/MacOS/aside`를 참조한다. `/Applications/Aside.app`과 `~/.aside/{accounts.json,cli,runtime,runtime-computer-use,u,logs}`가 존재한다. 계정 파일 내용은 수집하지 않았다.

1. [Aside 공식 홈페이지](https://aside.com/)에서 최신 macOS 앱을 설치한다.
2. 브라우저는 `brew install --cask aside`, CLI는 공식 별도 배포를 사용한다. 12 문서에 기록한 공식 CLI 스크립트와 수동 파일 배치·링크 등록 절차를 따른다. 스크립트 자체의 help/version 호출은 이번 조사에서 실행하지 않았다.
3. `~/.agents/skills/aside-browser` 같은 사용자 측 연동 지침은 별도로 보존하고 새 앱의 CLI 위치와 맞춘다.
4. 계정·연결된 웹 서비스는 새 Mac에서 로그인한다. `accounts.json`, 프로필 `u/`, 세션·쿠키를 일반 설정 문서와 함께 복사하지 않는다.
5. `runtime*`, `cli` 앱 번들은 최신 설치에서 재생성한다. 로그는 작동 설정 이전의 필수 항목이 아니다.

## cmux와 앱 내부 래퍼

현재 `/Applications/cmux.app/Contents/Resources/bin/`에 `cmux`, `cmux-claude-wrapper`, `ghostty`, `grok`, `open`, `start-cmux-profiling`, `submit-cmux-profile`이 있다. `~/.config/cmux/cmux.json`도 존재한다. 이 파일들의 존재는 별도 전역 grok 설치를 의미하지 않는다.

1. [공식 설치 문서](https://cmux.com/docs/getting-started)에 따라 최신 DMG를 설치하거나 다음 명령을 새 Mac에서 사용한다.

   ```sh
   brew tap manaflow-ai/cmux
   brew install --cask cmux
   ```

2. `cmux.json`의 사용자 설정을 최신 앱 설정과 병합한다. `~/.cmuxterm`은 구형 상태 후보로 보존만 하고 자동 덮어쓰지 않는다.
3. 앱 내부 터미널에서는 포함 CLI를 사용한다. 외부 셸에서도 필요하다면 새 앱의 `Contents/Resources/bin/cmux`에 대한 링크를 새로 등록한다. 기존 파일이 있는 위치를 강제로 덮어쓰지 않는다.
4. 래퍼·프로파일링 파일은 앱 업데이트에 맡긴다. 각각 별도 npm 패키지처럼 설치하지 않는다.
5. 세션 복원은 임의의 실행 중 프로세스까지 이전하지 않는다. 소켓과 프로파일링 상태는 이전 대상에서 제외한다. 프로파일링·테스트 명령은 실행하지 않는다.

## Ollama와 로컬 모델

현재 `/usr/local/bin/ollama`는 `/Applications/Ollama.app/Contents/Resources/ollama`를 참조한다. `~/.ollama/models`, `cache`, `logs`, `history` 및 키 파일이 존재한다.

1. [공식 macOS 설치 문서](https://docs.ollama.com/macos)에 따라 최신 앱을 `/Applications`에 설치한다.
2. 새 설치가 CLI 링크를 등록하도록 한다. 구형 앱 속 실행 파일만 가져오지 않는다.
3. 모델을 다시 다운로드하거나 기존 `models/`를 별도 데이터 묶음으로 옮긴다. 앱 최신화와 모델 선택·버전은 서로 다른 결정이다.
4. 모델 저장 경로를 바꾼 경우 새 저장 경로에 맞춰 환경 설정을 재작성한다. Mac mini의 메모리·저장 용량은 아직 확인되지 않았으므로 모델 전체를 적재할 수 있다고 가정하지 않는다.
5. `id_ed25519`는 민감한 개인 키다. 일반 설정 패키지에 포함하지 않는다. 로그·캐시·history는 모델 가중치와 분리한다.

## LM Studio와 lms

현재 `/Applications/LM Studio.app`, `~/.lmstudio/bin/lms`, `settings.json`, `mcp.json`, `config-presets/`, `models/`, `extensions/`가 존재한다. `credentials/`, `conversations/`, `server-logs/`는 설정과 분리한다.

1. [LM Studio CLI 공식 문서](https://lmstudio.ai/docs/cli)에서 연결된 최신 LM Studio 설치 경로를 따른다. CLI는 앱에 포함된다.
2. 새 설치가 제공하는 `lms` 등록 안내에 따라 `~/.lmstudio/bin` 연결을 구성한다.
3. `settings.json`과 `config-presets/`에서 사용자 선택을 복원한다. 내장 runtime·extensions의 구형 바이너리를 덮어쓰지 않는다.
4. `mcp.json`의 서버 정의는 새 설치의 실행 경로로 수정하고 계정 인증은 새로 진행한다.
5. `models/`는 저장 공간을 고려해 별도 이전한다. 대화 기록·projects·user-files는 보존 자료로 분리한다. 모델 서버 실행·추론은 이 계획 작성 범위가 아니다.

## Antigravity CLI와 agy

현재 `~/.local/bin/agy` 일반 실행 파일과 `Antigravity.app`, `Antigravity IDE.app`이 공존한다. 로컬 바이너리를 실행하지 않았으므로 바이너리 자체 버전은 미확인이다.

1. [Google 공식 CLI 시작 문서](https://antigravity.google/docs/cli/getting-started)의 최신 설치 경로를 사용한다.

   ```sh
   curl -fsSL https://antigravity.google/cli/install.sh | bash
   ```

2. 공식 설치 위치는 macOS에서 `~/.local/bin/agy`다. 새 셸의 해당 PATH 항목을 준비한다.
3. 기존 `.antigravity`와 `.gemini`의 사용자 규칙·MCP·skills는 [AI 도구 문서](05-ai-tools.md)의 분류에 따라 옮긴다. IDE와 CLI 설정이 항상 같은 스키마라고 가정하지 않는다.
4. 새 장치에서 인증한다. CLI·IDE·데스크톱 앱을 각각의 배포로 구분한다.

## 개인 sensai

현재 `~/.local/bin/sensai` 일반 파일이 존재하고 `~/Workspace/Personal/wonder-sensai`, `wonder-sensai2` 디렉터리가 관측된다. 이름 유사성만으로 해당 바이너리의 빌드 원본을 확정하지 않았다.

1. 기존 실행 파일은 개인 자료 보관에 포함하되 새 Mac의 기본 설치에 바로 복원하지 않는다.
2. 두 저장소의 README·배포 정의에서 실제 `sensai` 제공 여부와 공식 배포 위치를 확정한다. 이번 조사에서는 해당 연결이 미확인이다.
3. 출처가 확인되면 그 프로젝트의 최신 안정 배포를 사용한다. 공개 설치 채널이 없다면 소스와 설치 설명을 함께 넘기는 미해결 개인 도구 항목으로 남긴다.
4. 이름만 보고 동명의 외부 패키지를 설치하지 않는다. 임의의 `npm install -g sensai` 명령을 제시하지 않는다.

## 개인 spring-create와 spring-creator

두 링크의 실제 대상 파일은 현재 존재하지 않는다.

| 링크 | 관측된 대상 |
| --- | --- |
| `~/.local/bin/spring-create` | `~/Workspace/Personal/Traning/spring-creator/spring-create` |
| `~/.local/bin/spring-creator` | `~/Workspace/Personal/Traning/spring-creator2/spring-creator.sh` |

1. 링크 자체를 새 Mac의 작동 도구로 옮기지 않는다.
2. 개인 저장소 또는 백업에서 실제 스크립트를 확보한다. `Traning` 철자를 임의 교정하면 원래 경로와 달라지므로 원본부터 식별한다.
3. 스크립트 출처와 새 저장소 위치가 정해지면 새 절대경로로 링크를 등록한다.
4. 원본을 찾지 못하면 이전 보류로 유지한다. 공홈·공개 설치 채널은 확인되지 않았다.

## Cursor와 Kiro의 남은 링크

현재 `/usr/local/bin/cursor`, `/usr/local/bin/kiro`가 가리키는 앱 대상은 존재하지 않는다. 관련 숨김 설정 디렉터리만으로 설치 완료를 판단하지 않는다.

1. 이전 목록에서는 설치 흔적으로 기록한다.
2. 사용할 경우 각 공급자의 최신 앱을 새로 설치하고 앱의 CLI 등록 절차를 따른다.
3. `~/.cursor`, `~/.kiro`에 남은 개인 설정은 현재 사용 여부를 결정한 뒤 선별 복원한다.
4. 현재 링크를 복사하거나, 기존 설정만으로 로그인 완료를 가정하지 않는다. 이 두 앱의 최신 설치 문서는 본 조사에서 별도 열람하지 않았으므로 명령은 확정하지 않는다.

## 직접 설치된 npm 래퍼와 중복 실행 파일

`/opt/homebrew/bin`의 `chelper`, `coding-helper`, `jhipster`, `n`, `oh-my-claudecode`, `omc`, `omc-cli`, `yo`, `yo-complete`는 Cellar 패키지가 아닌 npm 전역 설치로 연결된다. [관리자별 이전](01-packages.md)의 해당 패키지를 설치하면 재생성된다.

`jules`는 일반 파일이고 같은 디렉터리의 `run.cjs`도 일반 파일이다. `/opt/homebrew/lib/node_modules/@google/jules/package.json`에는 별도 npm 설치 기록이 있다. 이름·근접 위치만으로 일반 파일의 소유 패키지를 확정하지 않으며, 최신 공식 Jules 배포를 사용해 중복을 줄인다.

`codegraph`는 `~/.local/bin`의 독립 설치, `/opt/homebrew/bin`의 `@colbymchenry/codegraph`, OMO의 `omo-codegraph`가 공존한다. 서로 같은 프로그램이라고 가정하지 않는다. MCP 서버가 의도한 구현과 실행 경로를 05 문서에서 맞춘다.

## 문서·미디어 변환과 보조 도구

`mmdc`는 npm `@mermaid-js/mermaid-cli`가 제공한다. 최신 패키지를 설치하고 자체 설정·Puppeteer 설정이 있으면 별도 이전한다. 브라우저 캐시는 재다운로드 대상으로 취급한다. [공식 Mermaid CLI 저장소](https://github.com/mermaid-js/mermaid-cli)는 설치 채널 참고 링크이며 여기서는 별도 열람하지 않았다.

`activate-global-python-argcomplete`, `register-python-argcomplete`, `python-argcomplete-check-easy-install-script`, `userpath`는 Python 설치에서 만들어진 진입점이다. 01 문서의 pipx·Python 환경을 재구성하면 필요한 항목만 새 shebang으로 생성한다. 기존 파일의 옛 인터프리터 경로를 통째 복사하지 않는다.

FFmpeg·ImageMagick·Poppler·Tesseract·7-Zip 등의 다수 명령은 한 패키지에서 함께 제공된다. 개별 executable마다 별도 설치할 필요 없이 [전체 패키지 카탈로그](02-package-catalog.md)와 [실행 파일 대응표](08-executable-map.md)를 연결해서 사용한다.
