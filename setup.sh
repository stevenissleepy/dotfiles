#!/usr/bin/env bash

# 请求 sudo 权限
echo "🔐 Requesting sudo password..."
sudo -v

# 加载环境变量和工具函数
source "$(dirname "$0")/scripts/env.sh"
source "$(dirname "$0")/scripts/utils.sh"
cd "$DOTFILES_DIR"

# 安装前准备
sudo apt update
chmod +x ./scripts/*.sh
./scripts/install_tools.sh

# 安装各个模块
./scripts/install_vim.sh
./scripts/install_git.sh
ask_install "shell" && ./scripts/install_shell.sh
ask_install "starship" && ./scripts/install_starship.sh
ask_install "autojump" && ./scripts/install_autojump.sh
ask_install "nvim" && ./scripts/install_nvim.sh && stow_module "nvim"
ask_install "tmux" && ./scripts/install_tmux.sh && stow_module "tmux"

sleep 2
clear
echo -e "\033[1;32m✅ Dotfiles 配置完成！\033[0m"