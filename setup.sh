#!/usr/bin/env bash

# 请求 sudo 权限
echo "🔐 Requesting sudo password..."
sudo -v

# 加载环境变量和工具函数
source "$(dirname "$0")/scripts/env.sh"
source "$(dirname "$0")/scripts/utils.sh"
cd "$DOTFILES_DIR"

# 安装工具集
chmod +x ./install_tools.sh && ./install_tools.sh
ask_install "stow" && sudo apt update && sudo apt install -y stow

ask_install "shell" && chmod +x ./scripts/install_shell.sh && ./scripts/install_shell.sh
ask_install "starship" && chmod +x ./scripts/install_starship.sh && ./scripts/install_starship.sh
ask_install "autojump" && chmod +x ./scripts/install_autojump.sh && ./scripts/install_autojump.sh
chmod +x ./scripts/stow_git_vim.sh && ./scripts/stow_git_vim.sh
ask_install "nvim" && chmod +x ./scripts/install_nvim.sh && ./scripts/install_nvim.sh && stow_module "nvim"
ask_install "tmux" && chmod +x ./scripts/install_tmux.sh && ./scripts/install_tmux.sh && stow_module "tmux"

sleep 2
clear
echo -e "\033[1;32m✅ Dotfiles 配置完成！\033[0m"