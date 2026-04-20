return {
	"nvim-treesitter/nvim-treesitter",
	lazy = false,
	main = "nvim-treesitter",
	build = ":TSUpdate",
	opts = {
		ensure_installed = { "lua", "cpp", "python", "c" },
		auto_install = true,
		highlight = { enable = true },
		indent = { enable = true },
	},
}
