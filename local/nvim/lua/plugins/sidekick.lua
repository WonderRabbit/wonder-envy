return {
  {
    "folke/sidekick.nvim",
    version = "v2.3.0",
    opts = {
      -- This setup is for the embedded CLI terminal only. It does not require Copilot.
      nes = { enabled = false },
      cli = {
        -- CLI processes live only while their Sidekick terminal remains open.
        mux = { enabled = false },
      },
    },
    keys = {
      {
        "<leader>aa",
        function()
          require("sidekick.cli").select({ filter = { installed = true }, focus = true })
        end,
        desc = "Sidekick: Select Installed CLI",
      },
      {
        "<leader>aC",
        function()
          require("sidekick.cli").toggle({ name = "codex", focus = true })
        end,
        desc = "Sidekick: Toggle Codex",
      },
      {
        "<leader>af",
        function()
          require("sidekick.cli").send({ msg = "{file}", submit = false })
        end,
        desc = "Sidekick: Insert File Context",
      },
      {
        "<leader>av",
        function()
          require("sidekick.cli").send({ msg = "{selection}", submit = false })
        end,
        mode = "x",
        desc = "Sidekick: Insert Selection Context",
      },
    },
  },
}
