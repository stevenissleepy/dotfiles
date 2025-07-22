#!/usr/bin/env bash

# 请求 sudo 权限
echo "🔐 Requesting sudo password..."
sudo -v

# 定义 dotfiles 目录
source "$(dirname "$0")/scripts/env.sh"
cd "$DOTFILES_DIR"

# 解析参数
AUTO_INSTALL=false
RE_INSTALL=false
[[ "$1" == "-a" ]] && AUTO_INSTALL=true
[[ "$1" == "-r" ]] && RE_INSTALL=true

# 询问是否安装（如果未启用 -a）
ask_install() {
    sleep 2
    clear
    local package="$1"

    # 如果已安装，直接跳过
    if command -v "$package" &> /dev/null && ! $RE_INSTALL ; then
        echo -e "\033[1;32m✅ $package 已安装，跳过...\033[0m"
        return 1
    fi

    # 如果有 -a 则不询问
    if $AUTO_INSTALL; then
        echo -e "\033[1;36m🔹 正在安装 $package...\033[0m"
        return 0
    fi

    # 询问是否安装该模块
    read -p "👉 是否安装 $package? (y/N) " choice
    [[ "$choice" == [Yy] ]] && echo -e "\n\033[1;36m🔹 正在安装 $package...\033[0m" && return 0
    return 1
}

# Stow 配置文件
stow_module() {
    stow -d "$DOTFILES_DIR" -t "$HOME" "$1"
}

# 安装工具集
chmod +x ./install_tools.sh && ./install_tools.sh
ask_install "stow" && sudo apt update && sudo apt install -y stow

ask_install "shell" && chmod +x ./scripts/install_shell.sh && ./scripts/install_shell.sh
ask_install "starship" && chmod +x ./scripts/install_starship.sh && ./scripts/install_starship.sh
ask_install "autojump" && chmod +x ./scripts/install_autojump.sh && ./scripts/install_autojump.sh
chmod +x ./scripts/stow_git_vim.sh && ./scripts/stow_git_vim.sh

if ask_install "nvim"; then
    chmod +x ./scripts/install_nvim.sh && ./scripts/install_nvim.sh
    stow_module "nvim"
fi

ask_install "tmux" && chmod +x ./scripts/install_tmux.sh && ./scripts/install_tmux.sh

sleep 2
clear
echo -e "\033[1;32m✅ Dotfiles 配置完成！\033[0m"