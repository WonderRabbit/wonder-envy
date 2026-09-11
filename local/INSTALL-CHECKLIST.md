# 로컬 설치 체크리스트

갱신일: 2026-09-11. 현재 설치 상태의 단일 기준이다. 14·15 계획과 기존 `local/README.md`를 대조했다. `[x]`는 실제 적용, `[ ]`는 미완료 또는 사용자 작업이다.

## 추가 설치

| 완료 | 항목 | 버전·상태 | 확인 근거 |
| --- | --- | --- | --- |
| [x] | LazyVim | stable commit `999700997f72`, plugin 32개 lock | 기본 nvim 시작·모듈 로드 |
| [x] | tree-sitter-cli | 0.27.0 | 영수증·parser 빌드 |
| [x] | Worktrunk | 0.77.0 | Zsh/Fish 전환·2개 worktree 수정 분리·branch 보존 정리 |
| [x] | Atuin | 18.22.0 | PTY 이력 추가·검색, Zsh/Fish Ctrl-R |
| [x] | mise | 2026.9.4 | task 실행에서 nvm·pyenv·SDKMAN 경로 유지 |
| [x] | Hurl | 8.0.1 | 임시 loopback HTTP 성공·의도한 실패 응답 |
| [x] | lnav | 0.14.1 | access log 인식·SQL 건수 조회 |
| [x] | difftastic | 0.70.0 | JavaScript diff·기존 git diff 유지 |
| [x] | Mason 도구 | StyLua·shfmt | receipt·실행 파일 존재 |

## 기존 설치 재사용

- [x] Ghostty·Herdr·Fish·Oh My Posh·JetBrainsMono Nerd Font.
- [x] Neovim·lazygit·Yazi·fd·fzf·ripgrep·ast-grep·mdq·yq·jq.
- [x] nvm / Node 26.8.2, pyenv / Python 3.14.7, uv 0.12.13, SDKMAN / Java 26.0.2.
- [x] Codex·Claude Code·OpenCode·OMO·OMC·Antigravity CLI 및 Herdr integration.
- [x] Aside·Orca·Paseo·VS Code·Docker와 사용자 CLI 링크.
- [x] Poetry·IPython·Pygments 및 기존 Homebrew 의존성.

## 설정·문서·검증

- [x] Neovim 설정·데이터 백업 후 분리 LazyVim을 기본 구성으로 전환.
- [x] `local/nvim/`에 starter 출처·LICENSE·lockfile 보관.
- [x] `apply-config.py`의 최소 Neovim 덮어쓰기 매핑 제거.
- [x] Atuin Ctrl-R, fzf Ctrl-T·Alt-C, 기존 방향키·프롬프트 유지.
- [x] Atuin 로컬 이력만 사용, AI 키 제외, 선택 명령 편집 유지.
- [x] Fish의 mise 자동 activation 차단; task 전용으로 사용.
- [x] 중첩 로그인 Zsh의 Java PATH 순서 보완.
- [x] Worktrunk Fish 공식 autoload·completion 및 저장소 템플릿 반영.
- [x] `brew bundle check`, 셸 구문·초기화, 재적용 무변경 확인.
- [x] `menual/`에 Homebrew 105개와 런타임·AI·앱·플러그인 사용법·공식 링크 작성.
- [x] 계획 14·15에 실제 차이와 완료 상태 반영.
- [x] GitHub SSH 계정 확인 및 이 저장소에만 noreply commit identity 설정.

확인 명령: `fish -lc 'python local/checks/additions.py'`. 임시 Git 저장소·로컬 서버를 사용하고 정리한다. [최근 결과](checks/latest-results.json). 운영 API·사용자 작업 branch·OMO QA는 실행하지 않았다.

## 남은 사항

- [ ] Herdr의 실제 pane 화면에서 cwd·아이콘·키 입력 확인. 현재 Codex 작업은 Herdr pane 밖에서 실행 중이며 해당 UI는 제어하지 않았다. CLI의 worktree 분리는 통과했다.
- [ ] 실제 프로젝트 API에 Hurl 명세 연결. 현재 확인은 격리된 로컬 응답 기준이다.
- [ ] Claude·GitHub CLI 및 필요한 공급자 로그인. SSH 원격 접근과 gh 로그인은 별도다.
- [ ] Docker Desktop 최초 실행·사용자 권한 안내.
- [ ] 이전 장치의 키·모델·DB·대화·사용자 dotfiles 자료 복원.

커밋·푸시는 Git 이력과 원격 branch를 기준으로 확인한다. 이 문서에는 자기 자신의 commit hash를 중복 기록하지 않는다.

## 17. 옵시디언 도구 관리

계획: [Obsidian 설치·Volt 구성](../.omo/plans/mac-mini-migration/17-obsidian-volt.md). 사용법: [프로젝트·카테고리 운영 매뉴얼](../menual/obsidian.md). 2026-09-11 기준. 준비된 설정 파일과 앱 런타임 검증을 구분한다. 공유 가능한 확인 요약은 [Obsidian 결과](checks/obsidian-results.json)에 기록한다.

- [x] Obsidian 1.13.7 설치. `/Applications/Obsidian.app/Contents/Info.plist`와 `brew list --cask --versions obsidian` 일치.
- [x] `local/Brewfile`에 `cask "obsidian"` 추가.
- [x] 신규 `~/Volt`에 9개 상위 폴더와 `.obsidian` 설정 준비.
- [x] 기본 노트·첨부 위치, 링크 자동 갱신, Templates·Daily notes·코어 플러그인 설정 파일 작성.
- [x] Home·분류 사전·OBS 프로젝트·샘플 작업·4종 템플릿·Work.base 3개 뷰 작성.
- [x] 설치·설정 계획과 Jira식 카테고리·속성·상태·일일/주간 운영 매뉴얼 작성.
- [x] Tasks·QuickAdd·Templater·Omnisearch·Dataview·Excalidraw·Git 추천 순서와 Kanban 유지보수 유의사항 기록. 후속 설치는 아래 참조.
- [x] JSON·Bases YAML·템플릿 날짜 치환 후 frontmatter 구문·고유 ID·필수 폴더 확인.
- [x] `~/Volt`를 앱 설정에 등록하고 Home을 열어 북마크한 뒤, 앱 재시작 뒤에도 Home이 활성 파일로 유지되는 것을 확인.
- [x] `OBS-001 보관함 검증`의 `doing`·`blocked` 변경이 Work.base의 Doing·Blocked 결과에 반영되고, `todo`·`false` 복원 후 두 결과가 비는 것을 확인.
- [x] 기본 Task 템플릿으로 날짜·제목이 치환된 노트를 만들고, 첨부가 `99-Attachments`에 저장되며, Obsidian 내 이름 변경 뒤 링크가 갱신되는 것을 확인.
- [x] 보관함과 `.obsidian`을 포함한 사전 설치 스냅샷을 별도 임시 폴더에 복원해 파일·경로를 확인. 같은 디스크 스냅샷이므로 독립 백업은 아직 설정하지 않았다.
- [x] Tasks 8.4.0과 QuickAdd 2.25.0 설치·활성화. Tasks global filter는 `#task`; QuickAdd는 Inbox task capture와 New task note 두 명령으로 최소 구성.
- [x] QuickAdd가 Inbox에 `#task` 항목을 추가하고 Tasks가 이를 조회하며, QuickAdd 템플릿 명령이 `00-Inbox`에 새 Task 노트를 생성하는 것을 확인.
- [x] 속성 자료형·기본 설정·Home 북마크를 앱 런타임에서 확인하고, 재시작 뒤 Tasks·QuickAdd·`#task` filter·QuickAdd 명령이 유지되는 것을 확인. 최종 `OBS-001 보관함 검증`은 `done`·`blocked: false`다.
- [ ] 실제 프로젝트 등록, 1주 운영 후 카테고리·WIP·플러그인 재검토.
- [ ] 여러 기기가 필요할 경우 동기화 수단 선택 및 충돌·복원 확인.

| 플러그인 | 설치 버전 | 목적·설정 | 검증일·결과 |
| --- | --- | --- | --- |
| Tasks | 8.4.0 | `#task` global filter, 프로젝트 체크박스 조회 | 2026-09-11: 공식 release 자산 hash·활성화·runtime query·재시작 유지 확인 |
| QuickAdd | 2.25.0 | Inbox task capture, New task note | 2026-09-11: 공식 release 자산 hash·capture·Task 템플릿 생성·재시작 유지 확인 |
| Templater·Omnisearch·Dataview·Git | — | 필요해질 때 도입; 기준은 매뉴얼 참조 | 미도입 |

## 16. Fish·Catppuccin·lsd 후속 작업

- [x] 계획 16 커밋·원격 main 푸시.
- [x] lsd 설치 및 Fish 목록 별칭.
- [x] Bass 연동과 nvm·Node·npm, SDKMAN·Java의 Fish 동작.
- [x] pyenv·Python·uv 및 mise task의 Fish 경로 검증.
- [x] macOS 로그인 셸을 Fish로 등록·변경.
- [x] Terminal·Ghostty·Herdr의 새 셸을 Fish로 변경.
- [x] Catppuccin Mocha 테마 적용 및 설정 로드 검증.
- [x] menual 사용법·테마 출처·실제 차이 기록.
- [x] 설치 결과 커밋·원격 main 푸시.

### 계획 16 검증 근거

- 계획 선행 커밋 `7598005`의 원격 반영을 확인한 뒤 설치했다.
- lsd 1.2.0, Fish 4.9.3. `dscl` 계정 셸과 `/etc/shells` 모두 `/opt/homebrew/bin/fish` 확인.
- 관리자 인증 완료. Terminal 기본·시작 프로필, Ghostty 설정, Herdr 설정에 Fish 반영.
- 깨끗한 환경의 로그인 Fish에서 Node·Python·Java 프로그램 실행과 npm, `nvm use`, `sdk use/current`, `pyenv shell`, uv 가상환경 활성화·해제 통과.
- `python` 경로가 pyenv shim을 유지하도록 Bass helper의 Python 경로를 고정했다.
- Yazi·lazygit·Atuin의 별도 PTY 세션 시작·종료 및 truecolor 출력 확인. LazyVim `catppuccin-mocha` 로드, Ghostty 설정 검사, lnav 테마 로드 통과.
- Fish Ctrl-R=Atuin, Ctrl-T=fzf 유지. mise task는 Fish 환경의 런타임 경로 유지.
- `brew bundle check --no-upgrade` 통과. 일반 check는 새 mise 배포 업데이트를 요구하므로 설치 검증과 구분한다.
- Herdr 기본 서버는 실행 중이 아니어서 재시작하지 않았다. 다음 실행부터 새 설정 적용; 기존 UI 수동 확인 항목은 유지.
- 설정·Terminal 프로필 재적용 변경 없음. [Fish 검증 결과](checks/fish-results.json), [운영 문서](../menual/fish-and-themes.md).

## 18. 옵시디언 Kanban 도구 관리

- [x] Kanban 2.0.51·Tasks Kanban 0.10.3·Excalidraw 2.27.3 설치·활성화.
- [x] Tasks에 backlog B·review R 상태 추가, 6열 보드 구성.
- [x] 기본 OBS Kanban 보드 및 CLI 생성·조회·수정·이동·완료·동기화 구현.
- [x] OpenCode·Claude Code 공용 skill과 각각의 `/kanban` command 설치.
- [x] OpenCode skill 검색, 경로 검사 포함 기본 테스트 18개 통과, 별도 실앱 검사 5개 통과. 기본 테스트의 실앱 항목 1개는 opt-in으로 skip.
- [x] 잘못된 ID 오류 처리 수정, 독립 실행에서 한글·셸 문법 보존과 review→done 확인.
- [x] [사용 매뉴얼](../menual/obsidian-kanban.md)과 [설치 기록](checks/obsidian-kanban-results.json) 추가.
- [ ] Claude Code·OpenCode의 새 모델 대화에서 사용자 프로젝트 작업으로 `/kanban` 활용.
