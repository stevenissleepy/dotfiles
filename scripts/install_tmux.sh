#!/usr/bin/env bash
set -e

source "$(dirname "$0")/env.sh"

sudo apt install -y tmux

# tpm 插件管理器
if [ ! -d "$HOME/.tmux/plugins/tpm" ]; then
    echo -e "\033[1;36m🔹 正在安装 tmux 插件管理器\033[0m"
    mkdir -p "$HOME/.tmux/plugins"
    git clone https://github.com/tmux-plugins/tpm "$HOME/.tmux/plugins/tpm"
fi

# catppuccin 主题
if [ ! -d "$HOME/.tmux/plugins/catppuccin" ]; then
    echo -e "\033[1;36m🔹 正在安装 tmux catppuccin 主题 tpm\033[0m"
    mkdir -p "$HOME/.tmux/plugins/catppuccin"
    git clone https://github.com/catppuccin/tmux.git ~/.tmux/plugins/catppuccin/tmux
fi

stow -d "$DOTFILES_DIR" -t "$HOME" tmux