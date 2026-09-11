# AI CLI와 에이전트 설정 이전 계획

## 원칙과 조사 범위

2026-09-06에 파일 목록, 심볼릭 링크, 패키지 메타데이터, 설정 키 이름을 읽어 작성했다. CLI·앱 실행, 로그인, 설치, 테스트, QA는 수행하지 않았다. 대화·로그 본문과 인증 파일 내용은 읽지 않았다. 아래 명령은 새 Mac mini에서 이후 수행할 설치 절차이며 이번 조사에서 실행한 명령이 아니다.

**최신 안정 버전을 설치하고 최신 설정 형식에 맞춰 사용자 설정만 선별 복원한다.** 아래 기존 버전은 관측 기록이며 버전 고정 요구가 아니다. 기존 바이너리, `node_modules`, 플러그인 캐시를 실행 환경으로 통째로 복사하지 않는다. 인증은 새 장치에서 재로그인하거나 비밀 저장소에서 별도로 공급한다.

## 현재 설치 근거

| 도구 | 관측 버전 | 읽기 전용 근거 | 해석 |
| --- | --- | --- | --- |
| Codex CLI | 0.153.4 | `~/.local/lib/node_modules/@openai/codex/package.json`의 `name`, `version`; `~/.local/bin/codex` 링크 | npm 설치본. 앱이 별도 포함하는 CLI 버전과 동일하다고 가정하지 않음 |
| Claude Code | 2.1.207 | `~/.local/bin/claude` → `/Users/oneyoon/.local/share/claude/versions/2.1.207` | 네이티브 설치 링크 기준 |
| Gemini CLI | 0.46.0 | `/opt/homebrew/bin/gemini` → `../Cellar/gemini-cli/0.46.0/bin/gemini` | Homebrew 설치 링크 기준 |
| OpenCode | 미확인 | `~/.opencode/bin/opencode` 존재 | 실행하지 않아 바이너리 버전 미확인. `~/.opencode/package.json`은 CLI 버전이 아닌 `@opencode-ai/plugin` 의존성만 보유 |
| OMO / LazyCodex | 4.19.4 | `~/.codex/plugins/cache/sisyphuslabs/omo/4.19.4/package.json`; 여러 `~/.local/bin/omo-*` 링크 | 현재 링크가 가리키는 플러그인 버전 |
| oh-my-claudecode | 4.14.6 | `~/.claude/plugins/installed_plugins.json`, marketplace의 `package.json` | 설치 등록과 패키지 메타데이터 일치 |
| Kotlin Language Server 플러그인 | 1.0.0 | `~/.claude/plugins/installed_plugins.json` | `kotlin-language-server@claude-code-lsps` |
| Hermes | 미확인 | `~/.local/bin/hermes`, `~/.hermes/hermes-agent/pyproject.toml` 존재 | 런처·소스 경로만 확인 |
| MoAI / Sensai / agy | 미확인 | `~/.local/bin/moai`, `sensai`, `agy` 존재 | 독립 바이너리. 설치 출처·릴리스는 추가 확인 필요 |

## Codex CLI와 앱 연동

### 설치 순서

1. 새 Mac의 Node.js와 npm은 사용자 결정에 따라 nvm으로 구성한다. [런타임 관리자 설치](11-runtime-managers.md)를 따른다. 기존 `~/.local/bin/node`, `npm`, `npx`는 `~/.hermes/node/bin/`에 의존하므로 이 링크를 그대로 옮기지 않는다.
2. Codex CLI의 최신 안정 배포본을 공식 설치 안내에 따라 설치한다. 앱도 별도 설치했다면 앱 관리 런타임과 직접 설치한 CLI의 위치를 구분한다.
3. 새 장치에서 Codex 계정에 로그인한다.
4. 새로 생성된 설정에 아래 사용자 지침과 필요한 기능만 반영한다. 앱·플러그인 관리 경로는 설치 과정에서 다시 생성한다.

공식 근거: [Codex CLI 설치](https://learn.chatgpt.com/docs/codex/cli), [Codex 설정 기본](https://learn.chatgpt.com/docs/config-file/config-basic). 공식 문서의 사용자 설정 경로는 `~/.codex/config.toml`이며 프로젝트 설정과 우선순위를 구분한다.

### 선별 보관 및 복원

| 원본 | 새 장치 처리 |
| --- | --- |
| `~/.codex/AGENTS.md` | 사용자 언어·작업 규칙을 새 설치에 복원 |
| `~/.codex/skills/posting`, `playwright` | 사용자 스킬로 보관. 최신 도구 경로와 호환 여부를 문서 기준으로 반영 |
| `~/.agents/skills/` | 아래 공유 스킬 절의 원본으로 보관 |
| `~/.codex/config.toml` | 모델·승인·샌드박스·기능·화면 선호를 최신 키 기준으로 선별 반영. 파일 전체 덮어쓰기 금지 |
| `~/.codex/hooks.json` | 사용자 hook 의도만 보관. 앱·OMO가 관리하는 hook과 중복 등록하지 않음 |
| `~/.codex/agents/*.toml` | 사용자 수정본이 있으면 참고 사본 보관. OMO 관리 역할은 최신 설치본에서 생성 |
| `~/.codex/skills/.system` | 설치가 제공하는 시스템 스킬이므로 새 배포본 사용 |

현재 직접 MCP 설정 이름은 `codegraph`, `node_repl`, `computer-use`, `pencil`이다. 이름이 존재한다는 사실과 실행·활성 상태는 별개다. 플러그인별 MCP 설정에는 OMO의 `git_bash`, `context7`, `codegraph`도 있다. 도구별 `command`, `args`, `cwd`, `env` 키를 최신 설치 위치에 맞춰 재구성하고 환경 변수의 비밀값은 문서에 옮기지 않는다.

현재 config에 선언된 플러그인에는 documents, spreadsheets, presentations, slack, google-drive, omo, github, chrome, pdf, template-creator, sites, visualize, browser, codex-app-tools가 있다. 캐시에는 hugging-face, deep-research-work, plugin-management, linear 등도 존재한다. **캐시 존재는 현재 활성화를 증명하지 않는다.** 새 앱의 플러그인 목록에서 필요한 항목을 재설치하고 연결 계정은 재인증한다.

### 절대경로 재작성

- `config.toml`의 프로젝트 신뢰 항목, 프로젝트별 열기 대상, hook 상태 키에는 `/Users/oneyoon/Workspace/...`와 기존 Google Drive 경로가 들어 있다. 새 장치의 실제 저장소 위치로 필요한 항목만 다시 등록한다.
- Codegraph 설정에 OMO `4.11.0/components/codegraph/dist/serve.js` 참조가 남아 있지만 현재 실행 링크는 OMO `4.19.4`를 가리킨다. 정적으로 확인한 경로 불일치이며 작동 실패를 시험한 것은 아니다. 최신 OMO가 생성한 경로를 사용한다.
- 브라우저 MCP에는 플러그인 버전 디렉터리, Pencil에는 `~/.pencil/mcp/antigravity/out/mcp-server-darwin-arm64` 경로가 들어 있다. 앱·플러그인을 먼저 설치하고 생성 경로를 다시 반영한다.
- marketplace의 `~/.codex/.tmp/bundled-marketplaces/...`, `~/.cache/codex-runtimes/...` 같은 런타임 경로는 이전하지 않고 앱이 생성하게 한다.
- hook 신뢰 해시·기존 승인 상태는 새 설치에 그대로 이식하지 않는다.

`~/.codex/auth.json`은 존재만 확인했다. 복사 대상에서 제외하고 재로그인한다. `sessions`, `archived_sessions`, `history.jsonl`, `session_index.jsonl`, `thread_history_*`, `state_*`, `memories_*`, `logs_*`, `queue_*`, `goals_*` SQLite 및 WAL/SHM은 실행 설정과 분리한다. 대화나 기억을 보존하려면 별도 보관 범위를 정해야 하며 실행 중인 DB를 새 설치에 덮어쓰지 않는다. `memories/`와 `.chatgpt-projects/`도 사용자 데이터일 수 있어 캐시로 일괄 폐기하지 않는다.

재생성 가능한 제외 항목은 `cache`, `tmp`, `.tmp`, `log`, `shell_snapshots`, `ipc`, `process_manager`, `thread-writer-locks`, `mcp-oauth-locks`, `models_cache.json`, 설치 런타임 및 플러그인 캐시다. `worktrees/`는 미커밋 작업이 있을 수 있으므로 캐시로 취급하지 않고 저장소 이전 범위에서 별도 판단한다.

## OMO / LazyCodex

1. 최신 Codex를 먼저 설치한다.
2. 공식 기본 경로인 `npx lazycodex-ai install`로 최신 배포를 설치한다. 예전 4.19.4를 고정하지 않는다.
3. `~/.omo/config.jsonc`, `~/.omo/omo.jsonc`의 사용자 선호만 최신 형식에 반영한다. 둘 다 존재하며 `codegraph` 설정을 포함하므로 오래된 파일을 무조건 활성 설정으로 정하지 않는다.
4. `~/.local/bin/omo-*`, `ulw`, `ulw-loop`, `lazycodex-executor-verify` 및 `~/.codex/agents`의 관리 파일은 설치자가 생성하도록 한다.

공식 설치자는 Codex 설정·역할·링크를 관리한다. marketplace 경로도 제공되지만 기본 설치 방식은 `npx`다. [LazyCodex 공식 설치 안내](https://github.com/code-yeongyu/lazycodex)

현재 13개 역할 파일은 explorer, librarian, plan, metis, momus, lazycodex-executor, worker-low/medium/high, code-reviewer, clone-fidelity-reviewer, qa-executor, gate-reviewer 계열이다. 설치된 스킬에는 ast-grep, frontend, programming, debugging, git-master, lsp, rules, teammode, ultrawork, ulw-plan, ulw-loop, start-work, review-work, ulw-research 등이 있다. 예전 배포의 역할·스킬·hook을 새 배포에 덮어쓰지 않는다.

`~/.omo/lsp-daemon`, `codegraph`의 실행 상태와 인덱스는 재생성 대상으로 분리한다. `migration-backup-2026-07-30T13-45-25-206Z-opencode-config`는 과거 설정 보관본으로 보존 가능하지만 새 환경의 활성 설정으로 자동 복원하지 않는다. 이 계획에는 OMO 진단·테스트·QA 실행 절차를 포함하지 않는다.

## Claude Code와 oh-my-claudecode

### 최신 설치

1. [Claude Code 공식 설치 안내](https://code.claude.com/docs/en/setup)의 네이티브 설치 방식 `curl -fsSL https://claude.ai/install.sh | bash`를 새 Mac에서 사용한다. 기존 버전을 지정하지 않는다.
2. 계정 로그인 또는 기존 공급자 인증을 새 장치에서 설정한다.
3. `~/.claude/settings.json`은 최신 설정을 바탕으로 사용자 선호를 선별 반영한다.
4. OMC를 사용할 경우 Claude 안에서 `/plugin marketplace add https://github.com/Yeachan-Heo/oh-my-claudecode`, 다음 입력으로 `/plugin install oh-my-claudecode`를 실행하는 공식 최신 설치 경로를 사용한다. [OMC 공식 설치 안내](https://github.com/Yeachan-Heo/oh-my-claudecode)

### 보관할 사용자 파일

`~/.claude/CLAUDE.md`, `ORCHESTRATOR.md`, `PRINCIPLES.md`, `MCP.md`, `COMMANDS.md`, `PERSONAS.md`, `RULES.md`, `MODES.md`, `FLAGS.md`, `commands/sc`, 사용자 스킬 및 사용자 hook을 보관한다. SuperClaude 메타데이터와 여러 지침 파일이 존재하지만 이번 조사에서는 구성 의존성 본문까지 분석하지 않았으므로 오래된 프레임워크 지침은 최신 OMC와 함께 무조건 합치지 않는다. `~/.claude/.omc-config.json`은 `defaultExecutionMode`, `team`, `setupVersion` 등의 키를 가진 참고 설정이다.

현재 활성 플러그인 이름은 `oh-my-claudecode@omc`, `kotlin-language-server@claude-code-lsps`다. `installed_plugins.json`, `known_marketplaces.json`은 필요한 플러그인을 식별하는 참고 자료로 보관하고 새 설치의 등록 파일은 새 장치에서 생성한다.

설정에는 `env`, `permissions`, `model`, `statusLine`, `hooks`, `teammateMode`, `preferredNotifChannel` 등이 있다. `env` 키 이름에는 `ANTHROPIC_AUTH_TOKEN`, `ANTHROPIC_BASE_URL`, 모델 선택 변수, `PATH` 등이 포함된다. **이 파일은 일반 환경설정이면서 비밀값을 포함할 수 있으므로 공유 문서나 공개 저장소로 복사하지 않는다.** 토큰·개인 endpoint를 제외한 설정만 선별하고 인증값은 별도 공급한다.

`~/.claude.json`의 전역 MCP 이름은 `MCP_DOCKER`, `exa`, `filesystem`, `github`, `linear`, `pencil`이다. 이 파일에는 OAuth 계정 및 프로젝트 상태도 있어 전체 이전하지 않는다. MCP 이름·필요 도구만 재구성하고 Docker, Pencil, 파일시스템 대상 경로가 새 장치에 준비된 뒤 연결한다.

hook 이벤트는 PermissionRequest, PostCompact, PostToolUse, PostToolUseFailure, PreToolUse, SessionStart, Stop, StopFailure, SubagentStart, SubagentStop, TeammateIdle, UserPromptSubmit이다. 이벤트 목록만 확인했으며 hook 명령을 실행하지 않았다. 새 OMC와 Orca가 설치하는 hook을 우선하고 사용자 hook 및 statusLine 명령의 경로만 추가한다.

캐시·실행 흔적인 `cache`, `debug`, `paste-cache`, `session-env`, `shell-snapshots`, `stats-cache.json`은 분리한다. `projects`, `sessions`, `history.jsonl`, `file-history`, `tasks`, `teams`, `backups`는 대화·작업 이력이므로 사용자 보관 대상일 수 있으나 설정 복원에 섞지 않는다. macOS 인증 저장소는 별도 이식하지 않고 새 장치 인증을 사용한다.

## Google AI CLI: Antigravity 최신 설치와 기존 Gemini 설정

2026-09-06 Homebrew 공식 API는 `gemini-cli`를 `deprecated: true`, 사유 `unsupported`, 대체 cask `antigravity-cli`로 표시한다. 폐기 지정일은 2026-06-18이며 조사 시점 `disabled`는 false다. 따라서 **최신 버전 우선 이전의 기본 경로는 Antigravity CLI**로 정한다. 기존 Gemini 0.46.0은 관측 기록으로만 남긴다. [Gemini CLI Homebrew 공식 메타데이터](https://formulae.brew.sh/api/formula/gemini-cli.json)

1. 새 Mac에서 `brew install --cask antigravity-cli`로 최신 배포를 설치한다. cask는 Google 배포본을 사용하고 명령 이름을 `agy`로 등록한다. 조사 당시 배포 버전은 1.1.27이지만 고정하지 않는다. 기존 `~/.local/bin/agy`와 명령 이름이 겹치므로 설치 경로 선택은 [앱·CLI 이전 계획](06-app-cli-custom.md)에 맞춘다. [Antigravity CLI Homebrew 공식 메타데이터](https://formulae.brew.sh/api/cask/antigravity-cli.json)
2. Antigravity에서 새로 인증하고 최신 설정을 생성한다. `~/.gemini/settings.json` 전체가 Antigravity와 호환된다고 가정하지 않는다. 기존 `ui`, `security`, MCP·hook 의도만 해당 제품의 지원 설정에 맞춰 선별 반영한다.
3. 기존 Gemini CLI 자체가 필요한 호환성 사유가 있을 때만 별도 설치를 검토한다. 과거 Gemini 설치 문서에는 Homebrew·npm 경로가 남아 있지만 이것을 최신 권장 경로로 사용하지 않는다. [기존 Gemini CLI 설치 문서](https://geminicli.com/docs/get-started/installation/)
4. `oauth_creds.json`, `google_accounts.json`, `google_account_id`는 존재만 확인했으며 내용은 읽지 않았다. 기존 인증 파일을 새 도구에 복사하지 않는다.

현재 MCP 이름은 `pencil`이다. hook 이벤트는 AfterAgent, AfterTool, BeforeAgent, BeforeTool이며 `/Users/oneyoon/.orca/agent-hooks/gemini-hook.sh` 절대경로를 참조한다. **Orca와 Pencil을 먼저 설치한 뒤 생성된 hook·MCP 경로를 사용한다.** 원본 `~/.gemini/GEMINI.md`는 0바이트이므로 이전할 사용자 지침 내용이 없다.

`trustedFolders.json`, `projects.json`의 이전 프로젝트 경로는 새 경로 기준으로 재설정한다. `tmp`, `history`, `state.json`, installation ID는 설정 복원과 분리한다. `antigravity`, `antigravity-cli`, `antigravity-ide`, `antigravity-backup` 디렉터리가 공존하지만 Gemini CLI 설정과 동일한 데이터라고 가정하지 않고 Antigravity 이전 범위에서 따로 취급한다.

## OpenCode

1. 새 Mac에서 공식 Homebrew 경로 `brew install anomalyco/tap/opencode`로 최신 안정 배포를 설치한다. 공식 대안은 `npm install -g opencode-ai`다. [OpenCode 공식 설치 안내](https://opencode.ai/docs/)
2. 현재 `~/.config/opencode/`는 조사 시점에 비어 있었다. 활성 전역 설정이 확인되지 않았으므로 과거 파일을 자동 복원하지 않는다.
3. `~/.config/opencode_original/`, `~/.config/opencode_bk/`에는 `opencode.json`, `AGENTS.md`, package 파일이 있고 후자에는 agents, commands, skills, recipes도 있다. 필요한 사용자 규칙·스킬만 참고 사본으로 보관한다. `node_modules`와 구 설정 스키마는 최신 설치에 덮어쓰지 않는다.
4. 공급자 연결은 새 설치의 `/connect`에서 재설정한다. `~/.local/share/opencode/auth.json`은 존재만 확인했으며 복사 대상에서 제외한다.

`~/.local/share/opencode/opencode.db` 및 WAL/SHM, repos, snapshot은 사용자 이력·복구 데이터로 별도 보관할 수 있다. log와 tool-output은 실행 설정에 포함하지 않는다. 바이너리 버전, 현재 이용 공급자, 프로젝트별 설정의 실제 사용 여부는 이번 비실행 조사에서 미확인이다.

## 공유 스킬과 추가 도구

`~/.agents/skills/`의 실제 디렉터리는 find-skills, orca-cli, orchestration, computer-use, aside-browser다. `~/.claude/skills/`의 computer-use, find-skills, orca-cli, orchestration은 `../../.agents/skills/...` 상대 링크다. 원본 디렉터리를 먼저 옮긴 후 같은 구조로 링크를 재생성한다. aside-browser는 별도 실제 디렉터리이고 omc-reference도 있으므로 모두 동일 링크라고 가정하지 않는다. `~/.agents/.skill-lock.json`은 설치 출처 참고 자료로 보관할 수 있다.

Hermes는 `~/.hermes/config.yaml`, SOUL.md, skills, hooks, plugins가 사용자 설정 후보이며 `.env`, `auth.json`은 비밀값 별도 공급 대상으로 분리한다. 세션·memories·cron은 사용자 데이터 및 자동화 의도를 포함할 수 있으므로 캐시와 구분한다. cache, image_cache, audio_cache, bootstrap-cache, 모델 캐시, logs는 실행 복원에서 제외한다. Hermes 소스·내장 Node를 그대로 복사하기보다 [Hermes 공식 설치 안내](https://hermes-agent.nousresearch.com/docs/getting-started/installation/)의 최신 설치 경로로 재설치하고 설정을 선별 반영한다. 기존 Hermes의 정확한 버전은 미확인이다.

MoAI는 `~/.moai/claude-profiles`, cache, state, logs, reports가 존재한다. Sensai와 agy는 바이너리 존재를 확인했다. agy의 공식 최신 설치 경로는 후속 조사로 [앱 CLI 문서](06-app-cli-custom.md)에 추가했다. MoAI·Sensai는 로컬 바이너리와 공식 배포의 연결을 추가 식별한 뒤 최신 릴리스를 설치한다. 구 바이너리나 `moai.backup.*`를 새 시스템 실행 경로로 복사하지 않는다.

## 추가 AI 도구의 설정 흔적

아래는 디렉터리와 설정 파일의 존재를 확인한 결과다. **설정 흔적만으로 CLI 설치·현재 사용·로그인 성공을 판정하지 않는다.** 특히 Orca가 만든 hook만 존재할 수 있으므로 필요한 도구를 정한 뒤 공식 최신 설치 경로를 적용한다. CLI 실행 파일 목록과 개인 도구 배포는 별도 앱·CLI 문서에서 다룬다.

| 도구 또는 영역 | 확인한 흔적 | 이전 방식 |
| --- | --- | --- |
| CommandCode | `~/.commandcode/settings.json`, skills; 설정 최상위는 hooks | 스킬을 보관하고 hook은 Orca 새 설치 기준으로 재생성 |
| Continue | `~/.continue/config.yaml`, `.continueignore`, skills, schemas | 사용자 설정 선별 복원. 인증·endpoint는 별도 공급. sessions·dev_data는 이력, index·logs는 분리 |
| GitHub Copilot | `~/.copilot/ide`, `hooks/orca.json` | IDE 연동·Orca hook 흔적. 설치·버전 미확인, 계정 연결은 새 환경에서 진행 |
| Factory Droid | `~/.factory/settings.json`, skills; 최상위는 hooks | 사용자 스킬 보관, hook 최신 재생성. CLI 설치 여부는 별도 판정 |
| Grok | `~/.grok/hooks/orca-status.json`, skills | Orca hook 및 스킬 흔적만 확인 |
| Jules | `~/.jules/config.yaml`, cache, history.txt | 설정의 비민감 부분만 복원. history는 사용자 이력, cache는 재생성 |
| Junie | `~/.junie/mcp`, instances, skills | 사용자 스킬·MCP 의도만 보관. instances는 앱 상태로 분리 |
| Kimi Code | `~/.kimi-code/config.toml`와 백업 | 공급자 비밀값을 분리하고 최신 설정 형식으로 선별 복원 |
| Kiro | `~/.kiro/settings/mcp.json`, extensions, argv.json, skills | MCP·사용자 스킬 선별 복원, 확장은 최신 재설치 |
| OMC 전역 상태 | `~/.omc/state`, sessions, rules-injector | 활성 설정과 분리. sessions는 이력, 나머지는 최신 OMC가 재생성할 상태인지 판별 |
| oh-my-pi | `~/.omp/agent/extensions` | 확장 흔적만 확인, CLI 설치·버전 미확인 |
| pi | `~/.pi/agent/extensions`, skills | 사용자 확장·스킬 보관, CLI 설치·버전 미확인 |
| OpenClaude | `~/.openclaude/settings.json`; 최상위는 hooks | hook 설정 흔적만 확인. 최신 연동이 생성한 파일 우선 |
| tweakcc | `~/.tweakcc/config.json`, system-prompts, 패치 JS·바이너리 백업 | 사용자 프롬프트만 참고 보관. 기존 Claude 바이너리·패치를 새 버전에 덮어쓰지 않음 |
| Antigravity | `~/.antigravity/extensions`, argv.json, antigravity | 앱 최신 설치와 확장 재설치로 처리. Gemini의 antigravity 디렉터리와 함께 범위 정리 |
| Pencil | `~/.pencil/mcp`, resources, apps, socket, license-token.json | 앱·MCP 최신 설치 후 명령 경로 재등록. 라이선스는 재인증, socket은 제외 |
| 공용 MCP | `~/.ai/mcp/mcp.json` | 서버 이름·명령 구조를 필요 도구별로 선별 반영. 전체 비밀값 복사 금지 |
| cagent | `~/.cagent/store` | 저장소 흔적만 확인, 설치·내용·버전 미확인. 재생성 가능 캐시라고 단정하지 않음 |

tweakcc의 설정 키에는 `ccInstallationPath`, `ccVersion`, `changesApplied`, `lastModified`, `settings`가 있다. 기존 설치 경로와 패치 적용 여부를 새 버전에 이식하지 않고 최신 도구의 지원 범위를 먼저 확인한다.

### Codegraph 이름 충돌

두 설치는 같은 명령 이름을 사용하지만 서로 다른 위치·배포다.

| 명령 경로 | 실제 대상 | 관측 버전 |
| --- | --- | --- |
| `~/.local/bin/codegraph` | `/Users/oneyoon/.codegraph/versions/v1.2.0/bin/codegraph` | 링크상 v1.2.0 |
| `/opt/homebrew/bin/codegraph` | `/opt/homebrew/lib/node_modules/@colbymchenry/codegraph/npm-shim.js` | package.json상 `@colbymchenry/codegraph` 1.0.1 |
| `~/.local/bin/omo-codegraph` | OMO 플러그인의 `components/codegraph/dist/cli.js` | OMO 4.19.4 경로 |

새 장치에서는 각 소비자 설정이 기대하는 구현을 식별하고 명시 경로를 사용한다. 단순히 `codegraph` 하나를 최신 설치했다고 세 구현이 모두 준비됐다고 간주하지 않는다. 기존 셸의 실제 PATH 우선순위와 실행 결과는 이번 조사에서 시험하지 않았다.

## 완료 조건과 남은 불확실성

이 문서의 완료 범위는 설치·복사·인증·경로 재작성 계획이다. 새 Mac의 실제 설치와 실행 결과를 확인했다는 의미가 아니다. 정확한 목적지 사용자명과 저장소 경로, 선택할 AI 공급자, 보존할 대화·메모리 범위는 실제 이전 단계에서 반영한다. 인증 데이터·캐시·대화 DB가 제외되더라도 사용자 규칙과 사용자 작성 파일은 별도 보관한다.
