# Sidekick.nvim

적용 기준일: 2026-09-11. 이 설정은 Neovim 안에서 이미 설치된 AI CLI를 작은 터미널 창으로 열고, 현재 파일이나 선택 영역을 **제출하지 않은 초안**으로 넣는 용도다. 자동 완성·자동 편집 도구로 설정하지 않았다.

## 역할과 경계

Sidekick은 LazyVim/Neovim의 플러그인이다. AI CLI의 로그인·요금제·모델 선택·권한은 각 CLI가 관리한다. 이 설정은 Codex·Claude Code·OpenCode 중 현재 `PATH`에서 발견되는 도구를 선택할 수 있게 할 뿐, Copilot 구독을 만들거나 tmux/Zellij 세션을 만들지 않는다.

| 도구 | 맡는 일 | Sidekick과의 관계 |
| --- | --- | --- |
| Sidekick.nvim | Neovim 내부 CLI 창, 파일/선택 영역 문맥 삽입, 도구 선택 | 이 문서의 대상 |
| Herdr | 프로젝트 터미널과 개발 셸을 여는 별도 터미널 도구 | Sidekick 세션을 관리하거나 복구하지 않는다 |
| Worktrunk | Git worktree 생성·전환 | Sidekick은 현재 열린 worktree의 파일만 문맥으로 읽는다 |
| Codex·Claude Code·OpenCode | 실제 AI 대화와 모델 호출 | Sidekick이 실행하거나 기존 프로세스에 문맥을 넣는다 |

따라서 Herdr pane을 제어하거나 Worktrunk worktree를 바꾸는 키는 없다. 유료 모델 요청은 CLI의 입력란을 눈으로 검토한 뒤 사용자가 직접 전송한다.

## 설치된 판본과 설정

| 항목 | 값 |
| --- | --- |
| 플러그인 | `folke/sidekick.nvim` |
| 고정 릴리스 | `v2.3.0` |
| 고정 커밋 | `53a2d3afa61e5fd2e17b270b5fa72e5493808304` |
| Neovim 요구 사항 | 0.11.2 이상; 확인한 설치는 0.12.5 |
| 선언 파일 | `local/nvim/lua/plugins/sidekick.lua` |
| lockfile 항목 | `local/nvim/lazy-lock.json`의 `sidekick.nvim` |
| NES | `nes.enabled = false` |
| multiplexer | `cli.mux.enabled = false` |

NES(Next Edit Suggestions)는 Copilot LSP와 Copilot 인증을 써서 편집 제안을 받는 기능이다. 이 환경의 목표는 기존 CLI 연결이므로 끄었다. 따라서 `:LspCopilotSignIn`을 실행할 필요가 없고 Copilot 구독도 필요 없다. `cli.mux.enabled = false`이므로 tmux/Zellij·Herdr에 Sidekick 세션이 남지 않는다. 창을 **숨기는** 동작은 프로세스를 유지하며, `:Sidekick cli close` 또는 Neovim 종료가 내장 터미널 프로세스를 끝낸다.

## 키

`<leader>`는 LazyVim 기본값인 Space다. 키는 Sidekick이 실제로 설치·로드된 뒤에 등록된다.

| 키 | 모드 | 동작 | 전송 여부 |
| --- | --- | --- | --- |
| `Space a a` | 일반 | 설치된 CLI만 고르는 선택기 | 선택 뒤 CLI를 열 뿐 프롬프트는 보내지 않음 |
| `Space a C` | 일반 | Codex CLI 창을 열거나 숨김 | 프롬프트를 보내지 않음 |
| `Space a f` | 일반 | 현재 파일을 가리키는 `@경로` 문맥을 활성 CLI 입력란에 삽입 | `submit = false`; 사용자가 확인 후 직접 Enter |
| `Space a v` | 비주얼 | 선택 영역 문맥을 활성 CLI 입력란에 삽입 | `submit = false`; 사용자가 확인 후 직접 Enter |

`Space a a`에서 표시되는 목록은 Sidekick의 `installed` 필터를 사용한다. 도구가 새로 설치됐으면 Neovim을 재시작하거나 `:Sidekick cli select`를 실행한다. 파일/영역 키를 먼저 누르면 Sidekick이 CLI 창을 만들고 문맥을 넣을 수 있지만, 이 설정은 `submit`을 명시적으로 `false`로 둔다. 텍스트가 어느 CLI로 가는지, 경로와 코드가 적절한지 검토한 다음 그 CLI의 자체 제출 키를 사용한다.

## 처음 사용하기

1. Fish 터미널에서 프로젝트 루트로 이동해 `nvim 파일명`을 실행한다. `fish`가 초기화한 `PATH`를 Neovim이 이어받으므로 Node 버전별 전역 CLI도 보인다. GUI에서 직접 Neovim을 열면 Fish 초기화가 없을 수 있다. 그 경우 터미널에서 시작하거나 `:echo $PATH`와 `command -v codex`를 Fish에서 비교한다.
2. `:Lazy`를 열어 `sidekick.nvim`이 `v2.3.0`인지 확인하고, `:checkhealth sidekick`을 실행한다. NES를 의도적으로 껐으므로 Copilot LSP 경고는 CLI 워크플로의 실패가 아니다.
3. `Space a a`를 누르고 설치된 CLI를 골라 연다. Codex만 곧바로 열려면 `Space a C`를 쓴다.
4. 현재 파일을 CLI가 참조할 수 있게 하려면 `Space a f`, 코드 일부를 텍스트로 넣으려면 비주얼 선택 뒤 `Space a v`를 누른다. 열린 CLI 입력란에서 경로·내용과 비용/권한 영향을 검토하고, 필요할 때만 직접 제출한다.

### 예시

`local/nvim/lua/plugins/sidekick.lua`을 열고 함수 일부를 비주얼 선택한 뒤 `Space a v`를 누른다. CLI 입력란에 선택 영역과 파일 위치가 들어간 것을 확인한 뒤, "이 로직의 경계 조건을 설명해 줘"처럼 필요한 질문을 직접 추가한다. 검토만 필요하면 전송하지 않고 창을 닫으면 된다.

`Space a f`는 파일 본문을 복사하지 않고 `@상대경로` 참조를 삽입한다. 선택한 CLI가 그 경로를 어떻게 읽고 저장하는지는 해당 CLI의 정책에 따른다. 비밀 값, 토큰, 개인 경로, 고객 데이터가 들어간 파일은 참조하거나 선택해 보내지 않는다. Sidekick은 문맥을 CLI 프로세스로 전달하며, 그 뒤 저장·전송 정책은 선택한 CLI와 계정에 따른다.

## 창, 종료, 세션 수명

- Sidekick 터미널의 일반 모드 `q`, `:Sidekick cli hide`, 또는 이미 열린 Codex에서 `Space a C`는 창만 숨긴다. 이 경우 CLI 프로세스와 입력 내용은 남아 있다.
- 숨긴 창은 `Space a C` 또는 `:Sidekick cli show name=codex`로 다시 보인다.
- 프로세스와 연결을 끝내려면 `:Sidekick cli close`를 쓴다. Neovim 종료도 내장 터미널 세션을 끝낸다.
- mux를 끈 상태에서는 detach/resume가 없다. 복구 가능한 장기 AI 세션이 필요하면 각 CLI의 자체 resume 기능을 사용하거나, 별도로 tmux/Zellij 정책을 결정한 뒤에만 설정을 바꾼다.

## 업데이트, 재설치, 제거, 복구

새 릴리스로 올릴 때에는 먼저 [공식 릴리스](https://github.com/folke/sidekick.nvim/releases)를 읽고 `local/nvim/lua/plugins/sidekick.lua`의 `version`을 의도한 태그로 변경한다. 이 저장소의 파일이 진실의 원천이므로, 변경을 검토한 다음 반드시 라이브 설정에 먼저 적용하고 라이브 Neovim에서 **Sidekick만** 갱신한다.

```fish
git diff -- local/nvim/lua/plugins/sidekick.lua
python3 local/apply-config.py
nvim --headless '+Lazy! update sidekick.nvim' +qa
diff -u local/nvim/lazy-lock.json ~/.config/nvim/lazy-lock.json
```

`apply-config.py`는 서로 다른 라이브 파일을 `~/.local/state/wonder-envy/backups/`에 백업한다. `diff -u` 결과에서 `sidekick.nvim`의 커밋만 의도대로 바뀐 것을 확인한 뒤, 라이브 lockfile을 `local/nvim/lazy-lock.json`으로 복사해 저장소에도 같은 고정을 기록한다. 그 복사본을 다시 검토한 뒤 커밋한다. 이 매핑은 lockfile을 자동으로 역동기화하지 않으므로 이 단계가 빠지면 저장소와 실제 Neovim이 달라진다. 전체 `:Lazy sync`나 전체 update는 다른 플러그인도 올릴 수 있으므로 이 환경의 재현성 점검에는 쓰지 않는다. 재설치는 같은 적용·검토·lockfile 역동기화 절차에서 `+Lazy! install sidekick.nvim`을 사용한다.

제거는 업데이트보다 한 단계 더 명시적이다. 먼저 `:Sidekick cli close`로 실행 중인 CLI를 끝내고, `local/nvim/lua/plugins/sidekick.lua`와 `~/.config/nvim/lua/plugins/sidekick.lua`를 각각 백업한다. 그 뒤 저장소 파일을 제거하고 라이브 대상도 별도로 제거한다. `apply-config.py`는 소스에서 사라진 mapping의 기존 대상을 삭제하지 않으므로, 제거에 쓰면 안 된다. 두 lockfile에서 `sidekick.nvim` 항목을 함께 제거한 뒤 `nvim --headless '+Lazy! clean' +qa`를 실행하고, `git diff`와 라이브 lockfile diff로 다른 플러그인 항목이 바뀌지 않았는지 확인한다. 이 작업 전 라이브 설정과 lockfile 백업은 비공개 `.local-setup/ai-tooling/sidekick/backups/`에 있다. 문제가 있으면 해당 백업에서 설정과 lockfile을 복원한 뒤 Neovim을 다시 시작한다.

## 문제 해결

| 증상 | 확인과 조치 |
| --- | --- |
| 선택기에 CLI가 없음 | Fish에서 `command -v codex`, `command -v claude`, `command -v opencode`를 확인하고 Neovim을 터미널에서 재시작한다. Node를 바꿨다면 Fish의 nvm 초기화 뒤 다시 연다. |
| `Space a f`/`Space a v`가 보이지 않음 | `:Lazy`에서 Sidekick 로드 상태, `:verbose nmap <leader>af`, `:verbose xmap <leader>av`를 확인한다. 다른 플러그인이 같은 키를 나중에 등록했다면 그 플러그인의 키를 조정한다. |
| Copilot 또는 tmux 관련 health 경고 | NES가 꺼져 있어 Copilot LSP를 쓰지 않으며, `cli.mux.enabled = false`라 tmux/Zellij 세션도 쓰지 않는다. 다만 Sidekick health check는 Copilot LSP와 기본 mux backend인 tmux의 설치 상태를 별도로 검사하므로 이 경고가 관찰될 수 있다. `LIVE_NES=false`, `LIVE_MUX=false`와 CLI 창/문맥 삽입이 정상인지로 이 구성을 판단한다. |
| CLI가 바로 종료됨 | 터미널에서 해당 CLI를 직접 실행해 인증/실행 문제를 확인한다. Sidekick은 계정을 고치지 않는다. `:Sidekick cli close` 후 다시 선택한다. |
| Herdr/tmux에서 세션을 못 찾음 | 정상이다. mux를 명시적으로 꺼 두었으므로 Sidekick 세션은 Neovim 터미널에만 존재한다. |

## 공식 자료와 검증 범위

- [Sidekick.nvim README](https://github.com/folke/sidekick.nvim)와 [v2.3.0 릴리스](https://github.com/folke/sidekick.nvim/releases/tag/v2.3.0)
- [Lazy.nvim plugin management](https://lazy.folke.io/)
- [Codex CLI 공식 문서](https://developers.openai.com/codex/cli/)

이번 작업은 Sidekick의 공식 stable tag/커밋, `nes.enabled=false`, `cli.mux.enabled=false`, 설정 문법·키 충돌 부재, 설치된 Codex·Claude·OpenCode 탐지, 그리고 실제 PTY에서 CLI를 열고 종료하는 흐름을 검증한다. 문맥 운반은 로컬 fixture로 렌더링해 확인하며, 실제 모델 프롬프트를 제출하지 않는다. 따라서 유료 모델 완성 응답, Copilot NES 제안, 계정 로그인 변경, mux 세션 복구는 검증하거나 주장하지 않는다. 상세 명령 결과는 `local/ai-tools/sidekick/results.json`과 비공개 `.local-setup/ai-tooling/sidekick/`에 남긴다.
