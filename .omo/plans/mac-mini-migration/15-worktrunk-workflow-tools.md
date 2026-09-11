# Worktrunk·Atuin·mise·Hurl·lnav·difftastic 추가 계획

작성일: 2026-09-11. [공유 대화 「CLI 툴 리서치」](https://chatgpt.com/share/6aa377f9-f540-83e8-93d6-f0b32666798a?ogimg=plain)의 최종 선정 6종과 설치 순서를 현재 Mac 계획에 반영한다. 이번 작업은 문서 추가이며 설치·셸 변경·서비스 실행은 수행하지 않는다.

## 2026-09-11 실행 결과

사용자의 후속 설치 요청에 따라 실행했다. 초안의 “이번 작업은 문서만” 표기는 당시 범위이며, 현재 상태는 [설치 체크리스트](../../../local/INSTALL-CHECKLIST.md)와 [검증 결과](../../../local/checks/latest-results.json)를 따른다.

6종 설치 및 CLI 확인을 완료했다. 계획과 다른 실제 사항은 다음과 같다.

- Homebrew mise가 Fish에서 자동 activate되어, 같은 이름의 사용자 `conf.d/mise-activate.fish`로 vendor 초기화를 차단했다.
- 중첩 로그인 Zsh에서 macOS PATH 초기화가 SDKMAN Java보다 시스템 java를 앞세워, SDKMAN 초기화 마지막에 선택된 JAVA_HOME/bin을 앞으로 정리했다. 이후 mise task의 3개 런타임 경로 확인이 통과했다.
- Worktrunk Fish 최신 설치자는 init 한 줄 대신 autoload 함수·completion 파일을 생성한다. 공식 설치자를 사용하고 두 파일을 템플릿에 보관했다.
- Atuin은 `--disable-up-arrow --disable-ai`, `enter_accept=false`, `auto_sync=false`로 구성했다.
- Hurl은 실제 프로젝트 API 대신 임시 loopback 서버로 성공·실패를 확인했고 서버를 종료했다.
- Herdr pane 제어는 수행하지 않았다. 현재 작업은 HERDR_ENV가 없는 환경이며, 설치된 `herdr --skill`은 “Do not inspect or control the focused Herdr session from outside Herdr.”를 요구한다. worktree 분리 자체는 Zsh/Fish와 Git 상태로 확인했다. 실제 pane 확인은 체크리스트에 남긴다.
- Git 실습의 `/var`와 `/private/var` 경로가 같은 폴더이므로 확인 스크립트는 실제 경로로 정규화한다. 사용자 저장소에는 실습 branch를 만들지 않았다.

## 1. 출처와 반영 범위

공유 대화에서 확인한 순서는 **백업 → Worktrunk·Herdr → Atuin → mise → Hurl → lnav → difftastic**이다. 도구별 설정·완료 기준·복구와 두 worktree의 분리 확인도 계획에 포함한다.

공유 페이지의 대화 내용은 확인했으나 `macos-cli-installation-plan.md`, `macos-cli-power-user-research.md` 첨부 파일 원문은 확보하지 못했다. 따라서 첨부 보고서 전체나 그 안의 12개 후보·60개 출처를 검토했다고 간주하지 않는다. 아래 세부 명령은 별도로 열람한 공식 문서에 근거한다.

현재 Homebrew 설치 목록에는 6종이 없고, 기존 계획에는 mise의 과거 설치 흔적·기본 제외 정책만 있다. 실제 설치 직전에 상태를 다시 확인하고 이미 설치된 도구는 재사용한다.

## 2. 기존 계획과 충돌하는 부분의 처리

| 기존 기준 | 이번 추가 계획 |
| --- | --- |
| [11 런타임 관리자](11-runtime-managers.md): nvm·pyenv+uv·SDKMAN | mise를 우선 **프로젝트 작업 실행기**로 도입. Node·Python·Java 관리자는 유지 |
| [04 개발 환경](04-dev-security.md): mise 기본 설치 제외 | 런타임 대체 제외 정책은 유지하되, 이 문서에서 작업 실행 목적의 설치 예외를 추가 |
| [13 작업 구성](13-workflow-orca-paseo-herdr.md): Orca/Paseo가 만든 worktree는 해당 앱이 관리 | Worktrunk는 직접 관리하는 작업의 별도 생성·정리 주체로 사용 |
| Ghostty·Herdr 기본, tmux 제외 | 공유 대화의 tmux 사용 전제는 현재 Mac에 이식하지 않음 |
| [14 LazyVim·CLI](14-lazyvim-cli-integration.md): 편집·파일/본문/구조 검색 | 동일 도구를 추가 설치하지 않고 이력·작업 실행·API·로그·diff를 보완 |
| fzf가 셸 이력 키 사용 | Ctrl-R은 Atuin으로 일원화, fzf의 파일·디렉터리 선택 기능 유지 |
| lazygit·Git 기본 diff | difftastic은 명시적 호출로 시작, 전역 pager·diff 설정 변경 없음 |

이 역할 제한은 공유 대화의 도구 선정을 현재 저장소의 확정 사항과 맞추기 위한 적용 결정이다. mise로 런타임 전체를 이전하거나 Worktrunk로 앱의 작업 상태를 가져오는 계획은 포함하지 않는다.

## 3. 설치 명세와 적용 순서

기존 [local/Brewfile](../../../local/Brewfile)을 단일 명세로 유지한다. 실제 설치 작업에서 아래 이름을 없는 경우에만 한 줄씩 추가한다. 이번 문서 작성에서는 Brewfile을 변경하지 않는다.

| 순서 | Formula / CLI | 추가 역할 | 설정·자료 위치 |
| --- | --- | --- | --- |
| 1 | `worktrunk` / `wt` | worktree 생성·전환·정리 | `~/.config/worktrunk/config.toml`, 선택적 프로젝트 `.config/wt.toml` |
| 2 | `atuin` / `atuin` | 맥락을 포함하는 셸 이력 검색 | `~/.config/atuin/config.toml`; 실제 DB 경로는 설치 후 확인·기록 |
| 3 | `mise` / `mise` | 프로젝트의 반복 명령을 이름으로 실행 | 프로젝트 `mise.toml`; 상위·사용자 설정의 병합 여부도 확인 |
| 4 | `hurl` / `hurl` | HTTP 요청과 응답 조건을 파일로 보관 | 프로젝트 `tests/http/*.hurl` 또는 기존 테스트 규약 |
| 5 | `lnav` / `lnav` | 여러 로그의 시간순 탐색·SQL 조회 | 사용자 lnav 설정·사용자 포맷의 실제 경로 기록, 원본 로그는 원래 위치 유지 |
| 6 | `difftastic` / `difft` | 구문 구조를 고려한 코드 diff | 초기에는 전역 설정 없이 명시적 실행 |

향후 설치 명령은 `brew install <Formula>`이며 위 순서로 도구별 설정을 마친다. 여섯 도구를 npm·Cargo·mise에서 다시 설치하지 않는다. 도구별 버전은 설치일 정식 배포를 사용하고 실행 경로·버전을 적용 결과에 기록한다.

### 공통 선행 작업

- [현재 적용 결과](../../../local/README.md)의 백업 방식에 따라 `.zshrc`, Fish 설정, Git 설정과 기존 도구 설정의 변경 전 사본을 보관한다.
- `local/config/zshrc`, `local/config/config.fish`도 함께 수정하도록 계획한다. 홈 파일만 변경하면 `local/apply-config.py` 재실행 시 새 초기화가 사라진다.
- 현재 worktree 목록·실제 작업 경로와 사용 중인 프로세스를 파악한다. 별도 실습 저장소에서 신규 동작을 먼저 확인한다.
- 14의 LazyVim 도입과 본 계획은 공통 셸 템플릿 변경을 조율한다. 본 계획은 LazyVim 설치 완료를 선행 조건으로 요구하지 않는다.

## 4. Worktrunk + Herdr

공식 설치·셸 연동 명령은 다음과 같다. 셸 설정을 변경하는 실제 설치 단계에서 실행한다.

```sh
brew install worktrunk
wt config shell install
wt config show
```

Zsh와 Fish 각각에 필요한 연동이 생성되었는지 확인한다. 설치자가 만든 초기화를 저장소의 해당 셸 템플릿에 반영하고 중복 블록을 제거한다. Git 저장소의 작업 디렉터리를 바꾸는 shell integration과 단순 바이너리 설치를 구분한다. [Worktrunk 설치](https://worktrunk.dev/), [설정 위치와 셸 연동](https://worktrunk.dev/config/)

사용 흐름은 **Worktrunk로 생성·전환 → 실제 경로 확인 → Herdr pane에서 동일 경로 사용 → Yazi/Neovim/lazygit 작업**으로 한다. `wt switch`는 실행한 부모 셸만 전환하며 이미 열린 다른 pane의 cwd를 바꾸지 않는다. Worktrunk가 만든 branch와 Herdr 세션, Orca/Paseo 작업 카드가 자동으로 연결된다고 가정하지 않는다.

초기에는 앱 관리 worktree 밖의 별도 실습 저장소를 사용한다. 최초 커밋이 있는 저장소에서 `setup/worktrunk-a`, `setup/worktrunk-b`처럼 실습 전용 브랜치 두 개를 `wt switch --create`로 만든다. 각 pane에서 실제 경로·브랜치를 확인하고, 한쪽의 파일 변경이 다른 쪽 파일과 Git 상태에 섞이지 않는지 확인한다. 이 확인은 향후 계획이며 이번에 브랜치를 만들지는 않는다.

자동 의존성 설치·서버 시작·에이전트 실행 hook, LLM 커밋 생성, `wt merge` 자동 흐름은 초기 설정에서 추가하지 않는다. 프로젝트 `.config/wt.toml`이 이미 있으면 hook 내용을 먼저 확인한다.

**완료 기준:** Zsh/Fish의 전환이 동작하고 두 worktree와 pane의 경로·수정 상태가 분리되어 있다. 앱 관리 worktree를 생성·정리하지 않았다.

**복구·정리:** 실습 변경을 보관하거나 정리하고 해당 경로를 쓰는 작업을 종료한 뒤, 지정한 실습 worktree에만 `wt remove --no-delete-branch --foreground <branch>`를 사용한다. branch는 보존하고 강제 삭제·프로세스 강제 종료 옵션은 쓰지 않는다. 셸 연동을 제거할 때는 생성된 블록과 저장소 템플릿을 함께 되돌린다. [Worktrunk 제거·브랜치 보존](https://worktrunk.dev/remove/)

## 5. Atuin과 fzf 키 배치

```sh
brew install atuin
```

기존 fzf 연동 뒤에 Atuin 초기화를 한 번 배치한다. Zsh에서는 SDKMAN의 마지막 초기화 위치를 유지하고, Fish에서는 Oh My Posh의 프롬프트 구성을 유지한다. 실제 삽입 위치와 키 바인딩은 설치된 버전의 초기화 출력으로 확인한다.

```sh
# Zsh 대화형 설정의 Atuin 초기화
eval "$(atuin init zsh)"
```

```fish
# Fish 대화형 설정의 Atuin 초기화
atuin init fish | source
```

Ctrl-R은 Atuin, Ctrl-T·Alt-C의 파일/디렉터리 선택은 fzf로 구성한다. 위·아래 방향키를 유지하려면 설치 버전이 제공하는 Atuin 키 설정으로 조정한다. tty가 없는 셸에서 키 초기화 오류가 나지 않도록 기존 fzf 보호 조건도 보존한다. [Atuin 설치·셸 구성](https://docs.atuin.sh/latest/guide/installation/)

초기 범위는 로컬 이력 검색이다. 계정 등록·클라우드 동기화·dotfiles 동기화·기존 이력 일괄 import는 기본 단계에 넣지 않는다. 새로 저장되는 이력 DB는 사용자 자료로 취급하며 Git 저장소에 넣지 않는다. 기존 셸 history 파일을 삭제하지 않는다.

**완료 기준:** 새 로컬 명령을 이력에서 찾고 선택할 수 있으며 Ctrl-T·Alt-C와 프롬프트가 유지된다. 실제 명령 실행은 사용자가 선택한 경우에만 이루어진다.

**복구:** Atuin 초기화 블록을 홈 설정과 템플릿에서 함께 제거하고 새 셸에서 기존 fzf 이력 키로 복귀한다. Atuin DB·기존 셸 이력은 보존한다.

## 6. mise를 작업 실행기로 제한 도입

```sh
brew install mise
```

초기 구성에서는 `mise activate`, mise shims PATH, 전역 `mise use` 또는 Node·Python·Java `[tools]` 선언을 추가하지 않는다. 작업 실행에는 셸 activation이 필수가 아니다. Zsh 개발 셸에서 기존 nvm·pyenv·SDKMAN을 선택한 뒤 `mise run`을 호출한다. [mise 시작 안내](https://mise.jdx.dev/getting-started.html), [Tasks](https://mise.jdx.dev/tasks/)

기존 파일이 없는 실습 프로젝트에서 아래와 같은 명세부터 시작한다.

```toml
[tasks.env-paths]
description = "현재 개발 런타임 경로 확인"
run = "command -v node; command -v python; command -v java"
```

```sh
mise tasks ls
mise run env-paths
```

mise는 작업 실행 시 병합된 설정의 도구 설치·환경 선언도 처리할 수 있다. 프로젝트·상위 디렉터리·사용자 설정을 확인하고 해당 실습에 `[tools]`나 기존 runtime 선택을 덮어쓰는 env 설정이 적용되지 않게 한다. `mise trust`가 필요하면 대상 파일을 읽고 그 파일만 신뢰한다. 전역 자동 신뢰는 추가하지 않는다.

실제 저장소로 확장할 때 기존 npm scripts·Gradle wrapper·uv 명령을 짧은 task로 호출한다. 자체 패키지 명세를 mise로 다시 작성하지 않는다. 셸 함수 `nvm`·`sdk`가 비대화형 task 안에서도 자동 제공된다고 가정하지 않는다.

**완료 기준:** 이름 붙인 명령을 실행할 수 있고 Node·Python·Java 경로가 기존 관리자 설치본을 유지한다.

**복구:** 새로 추가한 task와 신뢰 항목만 정리한다. 기존 `mise.toml`은 백업을 기준으로 병합 복원하고, 런타임 디렉터리는 제거하지 않는다.

## 7. Hurl로 로컬 API 확인 명세 보관

```sh
brew install hurl
```

프로젝트에 이미 HTTP 테스트 위치가 있으면 그 규칙을 따른다. 없으면 `tests/http/`에 공개 가능한 요청과 응답 조건을 둔다. 아래는 향후 예시이며 실제 서비스의 경로·응답 계약에 맞춰 작성한다.

```hurl
GET {{base_url}}/health
HTTP 200
```

```sh
# 해당 로컬 서버가 준비된 경우에만
hurl --test --variable base_url=http://127.0.0.1:8080 tests/http/health.hurl
```

초기에는 로컬 또는 전용 테스트 환경의 조회 요청만 다룬다. Hurl 설치만으로 서버가 실행되지는 않는다. 인증값은 커밋하는 `.hurl`에 넣지 않고 설치 버전의 변수 공급 방식으로 분리한다. 저장소의 formatter·일반 테스트 실행 시 운영 API를 자동 호출하는 hook은 추가하지 않는다. [Hurl 설치](https://hurl.dev/docs/installation.html), [첫 Hurl 파일](https://hurl.dev/docs/tutorial/your-first-hurl-file.html)

**완료 기준:** 준비된 로컬 응답에 대한 성공·실패 조건이 의도한 종료 상태로 구분된다. 대상 API가 없으면 설치만 완료로 기록하고 API 확인은 미완료로 남긴다.

**복구:** 이번에 만든 샘플·선택적 mise task만 제거한다. 기존 API 명세·인증 자료·서비스 상태는 변경하지 않는다.

## 8. lnav로 로그 탐색 보완

```sh
brew install lnav
lnav path/to/application.log
```

실제 사용할 로그 형식을 선정하고 내장 포맷 인식 여부를 먼저 확인한다. 여러 로그를 시간순으로 비교하고 인식된 테이블에서 SQL 조회를 사용하는 흐름을 문서화한다. JSON 로그라고 해서 필드·타임스탬프가 자동으로 원하는 의미로 인식된다고 가정하지 않는다. 사용자 포맷은 내장 지원이 부족한 경우에만 추가한다. [lnav 설치](https://lnav.org/downloads), [공식 문서](https://docs.lnav.org/en/latest/)

파일은 원래 위치에서 조회하며 로그 수집 daemon·강제 rotation·로그 삭제를 설치 과정에 포함하지 않는다. jq/yq의 구조 조회·변환과 구분해 lnav는 대화형 시간 탐색·집계에 사용한다.

**완료 기준:** 비민감 샘플 로그의 시간·수준이 인식되고 필터·집계 결과가 샘플 내용과 일치한다.

**복구:** 추가한 사용자 포맷·설정만 되돌린다. 원본 로그와 별도 보관 자료는 유지한다.

## 9. difftastic을 선택적 코드 diff로 추가

```sh
brew install difftastic
git -c diff.external=difft diff
```

명시적 일회성 호출을 기본으로 한다. 지원 코드 파일에서 문법 구조를 고려한 비교가 필요한 경우 사용한다. Git의 기존 `core.pager`, 전역 `diff.external`, lazygit의 diff 설정을 동시에 바꾸지 않는다. patch 생성·적용은 기존 Git 흐름을 유지한다. [Difftastic Git 연동](https://difftastic.wilfred.me.uk/git.html)

사용감이 확인된 후에만 별도 Git alias 또는 lazygit 연동을 검토한다. 그때도 14의 LazyVim/lazygit 설정과 한 곳에서 관리한다.

**완료 기준:** 샘플의 포맷 변경과 코드 변경을 비교할 수 있고 일반 `git diff`의 기존 동작은 유지된다.

**복구:** 일회성 명령은 환경 복구가 필요 없다. 이후 alias를 추가했다면 해당 항목만 제거하고 기존 pager 설정을 보존한다.

## 10. 실행 체크리스트와 산출물

- [x] 기존 설치·셸 설정·worktree 관리 주체 확인, 백업 준비.
- [x] Worktrunk 설치·Zsh/Fish 연동·두 worktree 분리 확인.
- [ ] Herdr 실제 pane 화면의 경로 분리 확인.
- [x] Atuin 설치, Ctrl-R 배치, 로컬 이력 보관 및 기존 fzf 키 유지.
- [x] mise 설치, task 전용 구성, 기존 런타임 선택 유지 확인.
- [x] Hurl 설치·임시 로컬 응답 성공/실패 확인.
- [ ] 실제 프로젝트 API에 요청 명세 연결.
- [x] lnav 설치, 샘플 포맷 인식·시간 탐색 확인.
- [x] difftastic 설치, 일회성 diff 사용 확인.
- [x] 기존 `local/Brewfile`·셸 템플릿·`local/README.md`에 실제 적용 상태 반영.
- [x] 14에서 계획한 `local/cli-workflows.md`에 여섯 도구 사용법을 합쳐 기록.

문서 작성 완료와 실제 설치 완료를 구분한다. 공유 대화의 수동 확인 취지는 위 완료 기준으로 반영했으며, 이번 작업에서 테스트·OMO doctor·QA를 실행하거나 별도 테스트 스위트를 만들지 않는다. 설치 기록은 도구별 성공·실패·미확인 상태를 나누고, 전체 이전 계획의 체크박스를 일괄 완료 처리하지 않는다.
