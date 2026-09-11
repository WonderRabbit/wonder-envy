# LazyVim 도입과 기존 CLI 연동 추가 계획

작성일: 2026-09-11. 사용자 요청에 따른 **추가 계획**이며, 이 문서 작성에서는 설치·업데이트·사용자 설정 변경을 수행하지 않았다. 현재 설치 목록과 저장소 설정을 읽고 공식 문서를 확인했다. 아래 체크박스는 향후 작업이다.

## 2026-09-11 실행 결과

사용자의 후속 설치 요청에 따라 실행했다. 초안의 “이번 작업은 문서만” 표기는 당시 범위이며, 현재 상태는 [설치 체크리스트](../../../local/INSTALL-CHECKLIST.md)와 [검증 결과](../../../local/checks/latest-results.json)를 따른다.

LazyVim·tree-sitter-cli 설치와 기본 nvim 전환을 완료했다. stable commit과 32개 plugin revision을 `local/nvim/lazy-lock.json`에 기록했다. `apply-config.py`의 init.lua 매핑은 제거했고, 기존 최소 설정과 데이터는 백업했다. 기본 lazygit 키를 사용하며 기존 `<leader>lg`는 이관하지 않았다. 사용법은 요청한 `menual/`로 통합하고 `local/cli-workflows.md`에서 연결한다. 화면상 폰트·Herdr 중첩 키 입력은 별도 미확인으로 기록했다.

## 1. 기존 계획과의 경계

패키지 설치 채널과 공통 셸 설정은 기존 문서를 단일 기준으로 유지한다. 여기서는 신규 구성인 LazyVim과 기존 계획에 없는 연결·충돌 해결만 추가한다.

| 기존 기준 | 계속 담당하는 범위 |
| --- | --- |
| [01 패키지](01-packages.md), [02 카탈로그](02-package-catalog.md) | 기존 CLI의 Homebrew 설치 경로와 도구 목록 |
| [03 셸·터미널](03-shell-terminal.md) | fzf 초기화, 사용자 alias, 에디터 설정 복원 원칙 |
| [11 런타임](11-runtime-managers.md) | nvm·SDKMAN·pyenv·uv와 개발 셸 PATH |
| [12 추가 도구](12-fish-posh-herdr-aside-paseo.md) | Fish·Oh My Posh, JetBrainsMono Nerd Font 설치·터미널 폰트 선택 |
| [13 작업 구성](13-workflow-orca-paseo-herdr.md) | Yazi opener·`y` wrapper, Herdr pane, 앱별 worktree 관리 |
| [현재 적용 결과](../../../local/README.md), [Brewfile](../../../local/Brewfile) | 2026-09-11 실제 설치·설정 상태와 공통 패키지 명세 |

이 문서의 LazyVim 전환 단계는 03·13의 **기존 Neovim 플러그인 전체 복원 단계 대신 선택하는 경로**다. 과거 `oneyoon` 설정 복원과 LazyVim starter 도입을 동시에 같은 `init.lua`에 적용하지 않는다. 기존 바이너리 설치와 Yazi·Herdr 역할은 그대로 재사용한다.

## 2. 요청 도구별 차이와 추가 작업

아래 버전은 현재 Mac의 설치 영수증 조회값이며 향후 버전 고정 요구가 아니다. LazyVim은 `lazy.nvim` 플러그인 관리자를 사용하는 Neovim 구성이다. 현재의 최소 `init.lua` 또는 lazygit 설치만으로 LazyVim 설치가 완료되지는 않는다.

| 요청 도구 | 현재 상태 / 실행 이름 | 기존 담당 | 이번 추가 범위 |
| --- | --- | --- | --- |
| LazyVim | 미도입; Neovim 0.12.5 + LuaJIT 설치 | 03·13은 Neovim 일반 구성 | starter 분리 도입, 설정 관리 전환, 기본 편집기로 승격 |
| lazygit | 0.65.0 / `lazygit`, alias `lg` | 01·03·13 | LazyVim 기본 Git 연동 재사용, 기존 키 충돌 정리 |
| fd | 10.5.0 / `fd` | 01·02·13 | 파일명 검색과 fzf 입력 역할 정의 |
| Yazi | 26.9.1 / `yazi`, wrapper `y` | 03·13 | LazyVim 전환 후 기존 `nvim` opener를 그대로 연결 |
| mdq | 0.10.0 / `mdq` | 01·02 | Markdown 구조 조회용 사용 예와 문서 정리 |
| yq | 4.53.6 / `yq` | 01·02 | Mike Farah 구현으로 통일, YAML→JSON 연결 |
| jq | 1.8.2 / `jq` | 01·02·13 | JSON 조회·필터와 yq 출력 연결 |
| fzf | 0.74.3 / `fzf` | 03·12 및 현재 셸 설정 | CLI 검색 흐름 정리; 편집기 fzf-lua는 선택 사항 |
| Nerd Font | JetBrainsMono Nerd Font 3.5.1 | 12 | LazyVim 아이콘 표시 확인; 다른 폰트 추가 설치 없음 |
| ast-grep | 0.45.3 / `ast-grep`, `sg` | 01·02 | 구조 검색 역할과 프로젝트 규칙의 관리 위치 정의 |
| ripgrep | 15.2.0 / `rg` | 01·02·13 | 본문 검색, 무시 파일·숨김 파일 처리 기준 |

**추가 설치 후보는 LazyVim starter와 `tree-sitter-cli`다.** 현재 PATH에는 `tree-sitter`가 없고 공통 Brewfile에도 CLI 선언이 없다. 설치 시점에 다시 확인한 뒤 없는 항목만 추가한다. 나머지 요청 도구를 새 Brewfile이나 npm·Cargo로 중복 설치하지 않는다.

## 3. 작업 A — LazyVim 의존성 보완

선행 조건: 기존 11·12·13 단계의 공통 환경이 준비되어 있어야 한다.

1. Neovim·Git·curl·C compiler·Nerd Font·CLI의 설치 경로를 확인한다. 현재 Neovim은 공식 문서의 요구사항인 0.11.2 이상과 LuaJIT 조건을 충족한다. 설치 시점 요구사항은 다시 확인한다.
2. Treesitter용 **CLI**가 없으면 `local/Brewfile`에 `brew "tree-sitter-cli"`를 한 번 추가하고 해당 항목만 설치한다. `tree-sitter` 라이브러리 설치 흔적과 `tree-sitter` 실행 파일을 구분한다.

   ```sh
   # 향후 설치 시, CLI가 없다고 확인한 경우에만 실행
   brew install tree-sitter-cli
   ```

3. 첫 LazyVim 설치는 `dev`로 진입한 Zsh 또는 Herdr의 Zsh pane에서 수행한다. Node 기반 LSP 설치가 필요할 때 nvm Node를 사용할 수 있어야 한다.
4. Mason·언어 extras는 실제 사용할 언어만 선택한다. 전역 Python 환경은 pyenv+uv를 유지하고, 프로젝트의 Python 분석 환경은 해당 `.venv`를 연결한다. LSP 도구 환경과 프로젝트 인터프리터를 구분한다.

근거: [LazyVim 요구사항](https://www.lazyvim.org/), [tree-sitter-cli Homebrew](https://formulae.brew.sh/formula/tree-sitter-cli).

## 4. 작업 B — 현재 Neovim을 유지하며 LazyVim 구성 준비

1. `~/.config/nvim`, `~/.local/share/nvim`, `~/.local/state/nvim`, `~/.cache/nvim`의 존재·링크를 확인하고 필요한 자료를 시각별 백업 경로에 보관한다. 기존 `.bak` 경로를 덮어쓰지 않는다.
2. **기존 설정 적용 스크립트의 소유권을 먼저 정리한다.** 현재 `local/apply-config.py`는 `local/config/init.lua`를 `~/.config/nvim/init.lua`로 복사한다. LazyVim을 기본으로 전환하기 전 이 매핑을 제거하거나, 최소 구성과 LazyVim을 명시적으로 선택하는 방식으로 바꾼다. 기본 재실행이 LazyVim을 최소 설정으로 되돌리지 않도록 한다.
3. 비어 있는 별도 구성 경로에 공식 starter를 받는다. `~/.config/nvim-lazyvim`이 이미 있으면 내용부터 확인하고 자동 교체하지 않는다.

   ```sh
   # 향후 실행 예시: 목적지 미존재 확인 후
   git clone https://github.com/LazyVim/starter ~/.config/nvim-lazyvim
   env NVIM_APPNAME=nvim-lazyvim nvim
   ```

4. `NVIM_APPNAME`은 위 실행에만 지정한다. 기존 기본 `nvim`과 설정·플러그인 데이터·상태 경로를 분리한다. 첫 시작의 플러그인 다운로드는 실제 설치 단계이며 이번 문서 작성에서 실행하지 않는다.
5. starter에서 사용자 설정을 별도 파일로 관리하고 `lazy-lock.json`, `lazyvim.json`이 생성되면 함께 보관한다. starter의 Git 이력·출처를 기록한 뒤 사용자 dotfiles 관리 방식으로 편입한다. 플러그인 디렉터리 자체를 저장소에 넣지 않는다.

이 분리 도입 경로는 [공식 starter 설치](https://www.lazyvim.org/installation)와 Neovim의 `:help $NVIM_APPNAME`을 조합한 계획이다. 공식 기본 설치 경로를 그대로 실행해 기존 구성을 바로 교체하는 절차와는 구분한다.

## 5. 작업 C — LazyVim 내부 기능과 기존 도구 연결

### lazygit과 단축키

LazyVim이 제공하는 Git 연동을 먼저 사용한다. 과거 `kdheepak/lazygit.nvim`과 현재 최소 설정의 터미널 생성 callback은 자동 복사하지 않는다. 셸 `lg` alias는 유지한다.

현재 `<leader>lg`는 LazyVim의 `<leader>l` 플러그인 관리 키와 접두사가 겹친다. LazyVim 전환 시 기존 `<leader>lg`는 이관하지 않고 설치된 버전의 기본 Git 키를 사용하며, 키 도움말에 root 기준과 cwd 기준의 차이를 기록한다. worktree 기준은 13 문서를 유지한다. [공식 키맵](https://www.lazyvim.org/keymaps)

### fd·ripgrep·fzf

- `fd`: 파일명·디렉터리명 후보를 찾는다.
- `rg`: 파일 본문을 찾는다.
- `fzf`: 받은 후보를 대화형으로 좁힌다.
- LazyVim은 우선 기본 picker를 사용한다. 셸 fzf 설치를 편집기의 fzf-lua 활성화와 동일하게 취급하지 않는다. 편집기에서도 fzf 사용을 선택하면 공식 `editor.fzf` extra를 통해 전환하고 여러 picker의 중복 키 설정을 추가하지 않는다. [공식 Fzf extra](https://www.lazyvim.org/extras/editor/fzf)

기존 Zsh의 `fzf --zsh`와 Fish의 `fzf --fish` 초기화는 한 번만 유지한다. 검색은 기본 ignore 정책을 유지하고, 숨김 파일이나 무시된 파일이 필요할 때만 명시적인 옵션을 추가한다. 파일명을 셸 명령 문자열로 재해석하는 wrapper는 만들지 않는다. 향후 다중 파일 전달 wrapper를 추가한다면 NUL 구분과 취소 처리를 포함한다.

간단한 CLI 후보 선택 예시이며 전역 설정을 바꾸는 명령은 아니다.

```sh
fd --type f | fzf
rg --line-number --smart-case '검색어' .
```

근거: [fd](https://github.com/sharkdp/fd), [fzf](https://github.com/junegunn/fzf). 이 예시는 후보 목록 표시용이며 특수 파일명을 편집기에 전달하는 완성 wrapper는 아니다.

### Yazi와 Nerd Font

Yazi 기본 설정은 13 문서의 `nvim` opener·blocking 실행과 `y` wrapper를 유지한다. 분리 준비 단계에는 전역 `EDITOR`를 바꾸지 않는다. 기본 LazyVim 전환이 끝나면 같은 `nvim` 명령으로 새 구성이 열리므로 별도 Yazi 편집 플러그인을 추가할 필요가 없다.

Ghostty의 기존 JetBrainsMono Nerd Font 설정을 재사용한다. Herdr에서 아이콘·한글 표시가 다른 경우 외부 터미널 설정과 렌더링 경계를 확인한다. Nerd Font를 Node 패키지나 다른 cask 이름으로 다시 설치하지 않는다.

## 6. 작업 D — 구조화 문서·코드 검색 도구 사용 기준

새 설치를 반복하는 대신 도구별 사용법을 한 문서로 추가한다. 향후 산출물은 `local/cli-workflows.md`이며 각 프로젝트의 실제 파일을 예제로 사용한다.

| 도구 | 추가할 사용 기준 | 제외할 중복 구성 |
| --- | --- | --- |
| mdq | Markdown의 제목·목록·구조 선택에 사용; 설치된 버전의 selector 문법으로 예시 작성 | JSON용 jq 표현식을 그대로 적용하지 않음 |
| yq | Homebrew Mike Farah yq v4를 기준으로 YAML 조회·JSON 변환 | 동명 Python yq 전역 설치 제외 |
| jq | JSON 필터·형식 검사·yq 출력 처리 | YAML/Markdown 파서를 별도 jq 플러그인으로 구성하지 않음 |
| ast-grep | 지원 언어의 AST 패턴 검색; 프로젝트 공통 규칙이 생길 때만 `sgconfig.yml`·규칙 파일 추가 | Homebrew 설치본과 npm/Cargo 전역 설치 중복 제외 |
| ripgrep | 일반 텍스트·정규식 검색 | AST 패턴 검색과 혼동하지 않음 |

향후 문서에 사용할 최소 예시다. `config.yaml`, `data.json`, `src/`는 실제 대상 경로로 바꾼다.

```sh
yq -o=json '.' config.yaml | jq 'keys'
jq '.' data.json
ast-grep run --lang ts --pattern 'console.log($$$ARGS)' src/
```

`ast-grep`을 문서의 표준 실행 이름으로 써 `sg`의 다른 구현과 혼동을 줄인다. 조회 예시에 rewrite 옵션이나 yq의 in-place 옵션을 넣지 않는다. 전역 AST 규칙을 모든 저장소에 주입하거나 자동 수정 hook을 추가하는 일은 별도 범위다.

근거: [mdq 공식 저장소](https://github.com/yshavit/mdq), [Mike Farah yq](https://mikefarah.gitbook.io/yq/), [jq 매뉴얼](https://jqlang.org/manual/), [ast-grep 시작 안내](https://ast-grep.github.io/guide/quick-start.html).

## 7. 작업 E — 기본 구성 전환·기록·복구

선행: A → B → C·D. 실제 설치 작업에서 분리 구성이 준비된 뒤 진행한다.

1. 실행 중인 Neovim의 미저장 작업을 마친다. B에서 정한 백업과 설정 적용 스크립트 수정이 완료됐는지 확인한다.
2. 현재 기본 Neovim 구성과 데이터·상태를 시각별 경로로 보관하고 LazyVim 구성을 `~/.config/nvim`에 배치한다. 분리 환경의 앱 이름에 의존하는 절대경로가 없는지 확인한다.
3. `NVIM_APPNAME` 지정 없이 기본 `nvim`을 시작해 필요한 플러그인 데이터를 생성한다. 기본 편집기 `EDITOR=nvim`, `VISUAL=nvim`, Yazi opener는 유지한다.
4. `local/README.md`에 실제 LazyVim·플러그인 lock 상태, 적용 파일·백업, 기본 키와 선택한 extras를 기록한다. 기존 최소 Neovim 완료 기록은 새 상태와 구분한다.
5. 되돌릴 때는 새 LazyVim 구성도 별도 보관한 후 이전 기본 구성·해당 데이터 경로와 설정 적용 방식을 함께 복원한다. 분리 준비 경로와 이전 백업을 일괄 삭제하지 않는다.

## 8. 추가 작업 체크리스트와 완료 기준

- [x] A. 기존 설치 재사용 여부 확인, 누락된 `tree-sitter-cli`만 공통 Brewfile에 추가·설치.
- [x] B. 시각별 백업, `apply-config.py`의 Neovim 소유권 정리, 분리 LazyVim starter 설치.
- [x] C. lazygit 키 충돌 정리, 기본 picker 선택, 기존 셸 검색·Yazi·폰트 구성 연결.
- [x] D. `local/cli-workflows.md`에 mdq·yq·jq·ast-grep·fd·rg·fzf 역할과 실제 예시 작성.
- [x] E. 기본 `nvim`을 LazyVim으로 전환, 버전·lock·백업·복구 경로 기록.

완료 상태는 기본 `nvim`과 Yazi 편집 동작이 같은 LazyVim 구성을 사용하고, 설정 적용 스크립트가 이를 덮어쓰지 않으며, 기존 CLI·셸 초기화의 중복 설치·등록이 없는 것이다. 이 문서는 설치 계획만 추가한다. 신규 테스트 스위트나 OMO QA 단계는 만들지 않으며, 실제 설치·확인 결과를 현재 완료로 표시하지 않는다.
