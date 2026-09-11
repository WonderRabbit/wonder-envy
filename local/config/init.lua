-- Minimal local configuration until the original dotfiles are available.
vim.g.mapleader = " "
vim.opt.number = true
vim.opt.relativenumber = true
vim.opt.termguicolors = true
vim.opt.expandtab = true
vim.opt.shiftwidth = 2
vim.opt.tabstop = 2
vim.opt.ignorecase = true
vim.opt.smartcase = true
vim.opt.clipboard = "unnamedplus"
vim.keymap.set("n", "<leader>lg", function()
  vim.cmd("tabnew")
  vim.fn.jobstart({ "lazygit" }, { term = true })
  vim.cmd("startinsert")
end, { desc = "Open lazygit in current worktree" })
vim.keymap.set("t", "<Esc><Esc>", [[<C-\><C-n>]], { desc = "Leave terminal mode" })
