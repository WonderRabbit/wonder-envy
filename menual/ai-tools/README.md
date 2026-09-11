# AI 보조 도구 5종 설치와 운영

적용 기준일: 2026-09-11. 이 안내는 기존 Fish, nvm, pyenv, uv, LazyVim 위에 설치한 QMD·Repomix·Promptfoo·LLM·Sidekick.nvim의 단일 시작점이다. 도구마다 할 수 있는 일과 데이터 경계가 다르므로, "AI 도구"라는 이유만으로 인증·모델·문서를 서로 공유하지 않는다.

## 역할 선택

| 도구 | 먼저 쓰는 상황 | 로컬 데이터·기록 | 실제 모델/API 필요 여부 | 상세 매뉴얼 |
| --- | --- | --- | --- | --- |
| QMD | 어느 Markdown 문서에 답이 있는지 모르는 검색 | `~/.config/qmd/`, `~/.cache/qmd/`의 색인·모델 | 공개 매뉴얼의 로컬 검색은 불필요 | [QMD](qmd.md) |
| Repomix | 검토한 공개 파일만 하나의 AI 문맥 파일로 묶기 | 기본 출력 `.local-setup/ai-tooling/node/` | 묶기에는 불필요, 외부에 보내면 그 서비스의 인증·정책 적용 | [Repomix](repomix.md) |
| Promptfoo | 프롬프트/모델 평가 정의의 성공과 실패를 반복 검사 | `~/.promptfoo/`, 명시 출력 파일 | `echo` fixture는 불필요, 외부 provider는 키·과금 필요 | [Promptfoo](promptfoo.md) |
| LLM | 한 입력을 요약·변환·구조화해 다음 셸 명령에 넘기기 | `~/Library/Application Support/io.datasette.llm/`; 기본 로그 꺼짐 | 현재는 공급자 미연결. 실제 추론은 키·비용 승인 필요 | [LLM](llm.md) |
| Sidekick.nvim | Neovim에서 기존 AI CLI를 열고 파일/선택 영역을 전송 전 초안으로 넣기 | `~/.config/nvim/`, Lazy 플러그인 캐시 | 플러그인 자체는 불필요. 선택한 CLI의 로그인 필요 | [Sidekick.nvim](sidekick.md) |

`rg`는 이미 아는 문자열을 찾는 첫 선택이고, QMD는 개념으로 문서를 찾을 때 쓴다. Repomix는 검색기가 아니라 외부에 전달할 공개 파일 묶음을 만든다. Promptfoo의 로컬 fixture 성공은 실제 모델 답변의 품질을 뜻하지 않으며, LLM과 Sidekick은 공급자 모델을 설치하거나 인증하지 않는다.

## 설치와 첫 작업

저장소 루트에서 실행한다. 공통 설치기는 기존 nvm Node와 pyenv가 고른 Python·uv를 사용하며 새 런타임 관리자를 만들지 않는다.

```fish
cd ~/Workspace/Projects/wonder-envy
fish local/ai-tools/install.fish
```

이 명령은 QMD·Repomix·Promptfoo의 고정 npm 패키지, LLM 0.35와 "로그 끔" 정책을 적용하고, Sidekick 설정을 홈 Neovim 경로로 복사한 뒤 고정 플러그인을 설치한다. `apply-config.py`는 다른 기존 설정을 발견하면 `~/.local/state/wonder-envy/backups/`에 보관한 다음 교체한다.

QMD는 설치 뒤에도 공개 `menual/` 컬렉션을 만들고, 로컬 모델을 내려받고, 색인해야 검색할 수 있다. 경로를 확인한 뒤 [QMD의 처음 설정하기](qmd.md#처음-설정하기)를 별도로 실행한다. 이 단계는 모델 다운로드와 디스크 공간이 필요하며 홈 전체·Volt·인증 파일을 색인하지 않는다.

처음 한 번의 안전한 흐름은 다음과 같다.

1. QMD에서 `menual/`만 `wonder-envy-menual` 컬렉션으로 만들고 `qmd search`를 실행한다.
2. Repomix의 allowlist 설정으로 공개 파일만 `.local-setup/` 출력에 묶고 파일 목록을 눈으로 확인한다.
3. Promptfoo `echo` fixture의 성공과 의도 실패 종료 코드를 확인한다.
4. LLM의 `llm logs status`가 `Logging is OFF`인지 확인한다. 공급자 키를 넣지 않아도 된다.
5. `nvim`에서 `Space a a`로 이미 설치된 CLI를 골라 열고, `Space a f` 또는 비주얼 `Space a v`로 문맥을 넣은 뒤 사용자가 직접 전송한다.

## 재현 명세와 확인 명령

| 범위 | 고정 명세/설정 | 설치·확인 |
| --- | --- | --- |
| Node 세 도구 | `local/ai-tools/node/package.json`, `package-lock.json`, `install.fish` | `fish local/ai-tools/node/install.fish`; `qmd --version`; `repomix --version`; `promptfoo --version` |
| QMD 검색 | `local/ai-tools/node/config/qmd-index.example.yml` | 컬렉션·모델·색인 후 `fish local/ai-tools/node/checks/run.fish` |
| Repomix | `local/ai-tools/node/config/repomix.config.json` | `repomix . --config local/ai-tools/node/config/repomix.config.json` |
| Promptfoo | `local/ai-tools/node/examples/promptfoo/` | `promptfoo eval -c local/ai-tools/node/examples/promptfoo/promptfooconfig.yaml --no-cache --no-share` |
| LLM | `local/ai-tools/llm/install.fish`, `configure.fish` | `fish local/ai-tools/llm/check-offline.fish` |
| Sidekick | `local/nvim/lua/plugins/sidekick.lua`, `local/nvim/lazy-lock.json` | `nvim --headless '+Lazy! load sidekick.nvim' '+lua assert(require("sidekick"))' +qa` |

설치·검증의 기계 판독 요약은 [공통 결과](../../local/checks/ai-tools-results.json)와 도구별 `local/ai-tools/*/results.json`에 있다. 실제 실행 로그와 임시 fixture 출력은 인증 상태를 포함할 수 있어 `.local-setup/ai-tooling/`에만 남긴다.

`node/install.fish`의 전역 npm 설치는 각 패키지의 정확한 버전(`--save-exact`)을 사용한다. `package-lock.json`은 이 저장소에서 그 버전군을 검토·재현할 때 쓰는 npm 해석 기록이지만, npm 전역 설치가 lockfile을 읽는다는 뜻은 아니다. 전역 설치의 실제 확인은 각 CLI의 `--version`과 도구별 receipt를 함께 본다.

## 업데이트, 제거, 복구

각 도구의 상세 매뉴얼에 있는 고정 버전·fixture 검증을 함께 따른다. Node 도구는 `package.json`과 `package-lock.json`을 같이 갱신하고, LLM은 같은 `(pyenv which python3)`으로 `uv tool install`한다. Sidekick은 선언의 `version`과 `lazy-lock.json`의 해당 커밋을 함께 바꾼 다음 `python3 local/apply-config.py`로 홈의 live 선언을 갱신하고 해당 플러그인만 Lazy에서 갱신한다. 저장소의 `sidekick.lua`만 바꾸어도 현재 `~/.config/nvim`은 자동으로 바뀌지 않는다.

제거는 전역 npm 패키지, uv tool, Lazy 플러그인과 각 홈 데이터가 서로 별개임을 전제로 한다. 먼저 설정·색인·결과를 확인하고 필요한 것만 비공개 백업한다. 특히 Sidekick은 저장소 source를 지우고 `:Lazy clean`만 실행해도 이미 복사된 홈 선언이 남을 수 있다. [Sidekick 제거 절차](sidekick.md#업데이트-재설치-제거-복구)에 따라 source와 live target을 모두 처리하고, source 제거와 같은 변경에서 `local/apply-config.py`의 Sidekick mapping도 제거한다. `npm uninstall --global`, `uv tool uninstall`, `:Lazy clean`은 모델·색인·로그·외부 계정 데이터를 자동으로 모두 지우지 않는다. 사용자 데이터나 API 키를 저장소·문서·공개 결과에 복사하지 않는다.

## 공통 문제 해결

| 증상 | 확인 순서 |
| --- | --- |
| 명령을 찾지 못함 | 새 Fish에서 `command -v qmd repomix promptfoo llm`을 확인하고 `node --version`, `pyenv which python3`, `uv tool list`를 본다. Node를 바꿨다면 nvm 전역 도구는 다시 설치한다. |
| QMD가 검색하지 못함 | `qmd status`, `qmd doctor`, 컬렉션 범위 `-c wonder-envy-menual`, `qmd update`와 `qmd embed` 순으로 확인한다. |
| 외부 호출·과금 오류 | Promptfoo/LLM/Sidekick의 CLI 로그인·API 키·모델 ID·조직 권한을 해당 공급자에서 확인한다. 이 저장소의 설치는 키를 만들거나 복구하지 않는다. |
| 파일을 외부 AI에 보내기 전 | Repomix allowlist와 생성 파일 목록을 다시 보고, QMD의 로컬 검색 결과도 외부 프롬프트에 붙이면 전송된다는 점을 확인한다. |
| Sidekick 키가 없음 | `:Lazy`, `:verbose nmap <leader>af`, `:verbose xmap <leader>av`로 플러그인 로드와 충돌을 확인한다. |

각 상세 매뉴얼의 "이번 검증 범위"는 실제로 실행한 로컬 fixture와 아직 실행하지 않은 모델/API/GUI 작업을 구분한다. 특히 실제 모델 품질, 유료 API 호출, 공급자 보존 정책, 전역 MCP 등록은 이 설치의 재현 가능한 결과로 주장하지 않는다.
