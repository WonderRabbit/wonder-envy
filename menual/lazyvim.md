# Neovim / LazyVim

기본 `nvim`은 LazyVim 구성을 사용한다. 실행 파일은 Homebrew Neovim, 설정은 `~/.config/nvim`, 재현용 사본은 `local/nvim/`이다. `local/apply-config.py`는 이제 Neovim 파일을 덮어쓰지 않는다.

```sh
nvim README.md
```

| 조작 | 의미 |
| --- | --- |
| `i`, `Esc` | 입력 모드 시작 / 일반 모드 복귀 |
| `:w`, `:q`, `:wq` | 저장 / 닫기 / 저장하고 닫기 |
| `Space` | 현재 LazyVim 단축키 안내 |
| `Space f f` | 파일 찾기 |
| `Space /` | 프로젝트 내용 검색 |
| `Space g g` | 프로젝트 root 기준 lazygit |
| `Space g G` | 현재 디렉터리 기준 lazygit |
| `:Lazy` | 플러그인 관리 |
| `:LazyExtras` | 필요한 언어·기능 extras 선택 |
| `:Mason` | 언어 도구 설치 관리 |

키는 [공식 키맵](https://www.lazyvim.org/keymaps)과 설치된 버전의 안내를 기준으로 한다. 이전 최소 설정의 `Space l g`는 Lazy 관리 키와 겹쳐 이관하지 않았다. 별도 `lazygit.nvim`을 중복 설치하지 않았고 기본 picker를 사용한다. 셸 `lg`는 계속 사용할 수 있다.

Yazi에서 텍스트를 열면 blocking opener로 같은 `nvim`을 실행한다. 저장하고 종료하면 Yazi로 돌아온다. `EDITOR`와 `VISUAL`도 `nvim`이다. Node·Java 기반 개발도 Fish에서 직접 실행한다. 테마는 `catppuccin-mocha`이며 [Fish·테마 문서](fish-and-themes.md)에 설정 위치를 정리했다.

플러그인 버전은 `local/nvim/lazy-lock.json`에 기록한다. 업데이트 후에는 실제 lockfile을 이 사본에도 반영한다. LazyVim starter의 LICENSE와 출처 commit은 `local/nvim/`에 보존했다. 이력과 소스만 보관하며 다운로드된 플러그인 전체는 Git에 넣지 않는다.

기존 기본 설정·데이터는 `~/.local/state/wonder-envy/backups/lazyvim-20260911-130603/`에 있다. 되돌릴 때 현재 작업을 저장하고 현재 LazyVim 구성도 보관한 뒤 필요한 이전 경로를 복원한다. 분리 준비용 `~/.config/nvim-lazyvim`은 기본 실행에 사용하지 않는다.

- [LazyVim 공식 설치](https://www.lazyvim.org/installation)
- [Neovim 공식 문서](https://neovim.io/doc/user/)
- [LazyVim starter](https://github.com/LazyVim/starter)
