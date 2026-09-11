# 테마·Fish 연동 출처

2026-09-11에 내려받은 원본을 고정 Git tree revision으로 보관했다. 각 저장소의 LICENSE를 같은 디렉터리에 포함한다. 실행 시 원격 다운로드를 하지 않는다.

| 파일 | 공식 저장소 | Git tree revision |
| --- | --- | --- |
| [lsd-colors.yaml](lsd-colors.yaml) | [lsd](https://github.com/catppuccin/lsd) | `7085155432c7fe53a7acd7b0c004955368aa0fba` |
| [yazi-theme.toml](yazi-theme.toml) | [yazi](https://github.com/catppuccin/yazi) | `d62802be39210ea10e54b3e3b09735c6cb9e57c1` |
| [fzf-catppuccin.fish](fzf-catppuccin.fish) | [fzf](https://github.com/catppuccin/fzf) | `7508f8141286fb95249100a2b5325960320dcf32` |
| [atuin-mocha.toml](atuin-mocha.toml) | [atuin](https://github.com/catppuccin/atuin) | `68aa64b77573c235044b614e752a781701af4eec` |
| [lazygit-mocha.yml](lazygit-mocha.yml) | [lazygit](https://github.com/catppuccin/lazygit) | `798ad2e75a11766e9ba50e76e59aea6a81eb4866` |
| [catppuccin-mocha.tmTheme](catppuccin-mocha.tmTheme) | [bat](https://github.com/catppuccin/bat) | `6810349b28055dce54076712fc05fc68da4b8ec0` |
| [catppuccin-mocha.terminal](catppuccin-mocha.terminal) | [Terminal](https://github.com/catppuccin/terminal.app) | `671f4e176c6223e66995a1d30d7ddd4e736721af` |
| [bass.fish](bass.fish) | [bass](https://github.com/edc/bass) | `79b62958ecf4e87334f24d6743e5766475bcf4d0` |
| [__bass.py](__bass.py) | [bass-python](https://github.com/edc/bass) | `79b62958ecf4e87334f24d6743e5766475bcf4d0` |
| [eza-theme.yml](eza-theme.yml) | [eza](https://github.com/catppuccin/eza) | `70f805f6cc27fa5b91750b75afb4296a0ec7fec9` |

로컬 변경: `local/config/bass.fish`는 system Python 사용·실패 시 임시 파일 정리를 추가했다. `local/config/fzf-catppuccin.fish`는 universal 대신 global export를 사용한다. Terminal 적용본은 원본에 Fish 명령·Nerd Font를 추가했다. eza 테마는 내용 변경 없이 파일 끝의 중복 빈 줄만 정리했다. 나머지 원본 파일은 그대로 보관한다.

Fish·Ghostty·Oh My Posh·Herdr·OpenCode는 설치본의 내장 테마를 선택한다. LazyVim의 Catppuccin은 기존 lockfile 버전을 사용한다. lnav는 공식 schema에 Mocha 색상을 매핑한 로컬 설정이며 Catppuccin 공식 포트로 표시하지 않는다.
