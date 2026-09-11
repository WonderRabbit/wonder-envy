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
- [x] `menual/`에 Homebrew 104개와 런타임·AI·앱·플러그인 사용법·공식 링크 작성.
- [x] 계획 14·15에 실제 차이와 완료 상태 반영.
- [x] GitHub SSH 계정 확인 및 이 저장소에만 noreply commit identity 설정.

확인 명령: `zsh -lic 'python local/checks/additions.py'`. 임시 Git 저장소·로컬 서버를 사용하고 정리한다. [최근 결과](checks/latest-results.json). 운영 API·사용자 작업 branch·OMO QA는 실행하지 않았다.

## 남은 사항

- [ ] Herdr의 실제 pane 화면에서 cwd·아이콘·키 입력 확인. 현재 Codex 작업은 Herdr pane 밖에서 실행 중이며 해당 UI는 제어하지 않았다. CLI의 worktree 분리는 통과했다.
- [ ] 실제 프로젝트 API에 Hurl 명세 연결. 현재 확인은 격리된 로컬 응답 기준이다.
- [ ] Claude·GitHub CLI 및 필요한 공급자 로그인. SSH 원격 접근과 gh 로그인은 별도다.
- [ ] Docker Desktop 최초 실행·사용자 권한 안내.
- [ ] 이전 장치의 키·모델·DB·대화·사용자 dotfiles 자료 복원.

커밋·푸시는 Git 이력과 원격 branch를 기준으로 확인한다. 이 문서에는 자기 자신의 commit hash를 중복 기록하지 않는다.
