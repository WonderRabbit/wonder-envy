# LazyVim 플러그인과 보조 실행 파일

플러그인은 LazyVim 안에서 사용한다. `:Lazy`에서 이름으로 찾으면 로딩 상태·설정·공식 저장소를 볼 수 있다. 기능 선택은 `:LazyExtras`, 키 배치는 [LazyVim 사용법](lazyvim.md)을 따른다. 다음 목록은 설치된 구성과 lockfile에서 수집했다.

| 플러그인 | 고정 revision | 공식 저장소 |
| --- | --- | --- |
| LazyVim | `999700997f72` | [upstream](https://github.com/LazyVim/LazyVim) |
| blink.cmp | `78336bc89ee5` | [upstream](https://github.com/saghen/blink.cmp) |
| bufferline.nvim | `655133c3b4c3` | [upstream](https://github.com/akinsho/bufferline.nvim) |
| catppuccin | `edefef779ab0` | [upstream](https://github.com/catppuccin/nvim) |
| conform.nvim | `016802de4025` | [upstream](https://github.com/stevearc/conform.nvim) |
| flash.nvim | `5f0f270fdc7c` | [upstream](https://github.com/folke/flash.nvim) |
| friendly-snippets | `b4d01b0fdf3c` | [upstream](https://github.com/rafamadriz/friendly-snippets) |
| gitsigns.nvim | `f2421c550618` | [upstream](https://github.com/lewis6991/gitsigns.nvim) |
| grug-far.nvim | `11595bf747ed` | [upstream](https://github.com/MagicDuck/grug-far.nvim) |
| lazy.nvim | `85c7ff3711b7` | [upstream](https://github.com/folke/lazy.nvim) |
| lazydev.nvim | `ff2cbcba459b` | [upstream](https://github.com/folke/lazydev.nvim) |
| lualine.nvim | `221ce6b2d999` | [upstream](https://github.com/nvim-lualine/lualine.nvim) |
| mason-lspconfig.nvim | `b5576cd62899` | [upstream](https://github.com/mason-org/mason-lspconfig.nvim) |
| mason.nvim | `2a6940af8037` | [upstream](https://github.com/mason-org/mason.nvim) |
| mini.ai | `cb02c5444613` | [upstream](https://github.com/nvim-mini/mini.ai) |
| mini.icons | `98faae31e9be` | [upstream](https://github.com/nvim-mini/mini.icons) |
| mini.pairs | `b1c5a726921b` | [upstream](https://github.com/nvim-mini/mini.pairs) |
| noice.nvim | `7bfd942445fb` | [upstream](https://github.com/folke/noice.nvim) |
| nui.nvim | `10fc361835c8` | [upstream](https://github.com/MunifTanjim/nui.nvim) |
| nvim-lint | `3d55c8f67c6a` | [upstream](https://github.com/mfussenegger/nvim-lint) |
| nvim-lspconfig | `ac9d2f7c4757` | [upstream](https://github.com/neovim/nvim-lspconfig) |
| nvim-treesitter | `d4d59cb369da` | [upstream](https://github.com/nvim-treesitter/nvim-treesitter) |
| nvim-treesitter-textobjects | `5c7b0263797d` | [upstream](https://github.com/nvim-treesitter/nvim-treesitter-textobjects) |
| nvim-ts-autotag | `88c1453db4ba` | [upstream](https://github.com/windwp/nvim-ts-autotag) |
| persistence.nvim | `b20b2a7887bd` | [upstream](https://github.com/folke/persistence.nvim) |
| plenary.nvim | `74b06c6c75e4` | [upstream](https://github.com/nvim-lua/plenary.nvim) |
| snacks.nvim | `882c996cf281` | [upstream](https://github.com/folke/snacks.nvim) |
| todo-comments.nvim | `31e3c38ce9b2` | [upstream](https://github.com/folke/todo-comments.nvim) |
| tokyonight.nvim | `cdc07ac78467` | [upstream](https://github.com/folke/tokyonight.nvim) |
| trouble.nvim | `bd67efe408d4` | [upstream](https://github.com/folke/trouble.nvim) |
| ts-comments.nvim | `a59d60922134` | [upstream](https://github.com/folke/ts-comments.nvim) |
| which-key.nvim | `3aab2147e748` | [upstream](https://github.com/folke/which-key.nvim) |

## Mason이 설치한 formatter

- StyLua: Lua 형식 검사 `stylua --check file.lua`. 포맷 적용은 `stylua file.lua`. [공식 저장소](https://github.com/JohnnyMorganz/StyLua).
- shfmt: 셸 스크립트의 변경 예정 diff 확인 `shfmt -d script.sh`. 파일 수정은 `shfmt -w script.sh`. [공식 저장소](https://github.com/mvdan/sh).

둘은 `~/.local/share/nvim/mason/bin`에 있으며 Neovim에서 사용한다. 독립 셸에서는 이 경로의 실행 파일을 명시한다. Homebrew에 중복 설치하지 않았다.

## OMO 관리 실행 파일

다음은 독립 제품이 아니라 OMO 플러그인의 기능별 진입점이다. 평소에는 Codex 안의 플러그인 명령·스킬로 사용하고, 설치자가 관리하는 링크를 직접 바꾸지 않는다.

- `lazycodex-executor-verify`
- `omo`
- `omo-codegraph`
- `omo-comment-checker`
- `omo-git-bash-hook`
- `omo-lsp`
- `omo-rules`
- `omo-start-work-continuation`
- `omo-telemetry`
- `omo-ultrawork`
- `omo-ulw-loop`
- `ulw`
- `ulw-loop`

사용·업데이트 절차는 [공식 LazyCodex 문서](https://github.com/code-yeongyu/lazycodex)를 따른다. 이 설정 작업에서는 OMO QA·doctor·에이전트 작업을 실행하지 않았다.
