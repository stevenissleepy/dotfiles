#!/usr/bin/env bash
set -e

source "$(dirname "$0")/env.sh"

sleep 2
clear
echo -e "\033[1;36m🔹 正在安装 shell, 请选择要进行的操作\033[0m"
echo "[1] 安装 zsh 并设为默认终端"
echo "[2] 安装 zsh 但依然使用 bash"
echo "[3] 不安装 zsh"
echo "[else] 跳过"

read -r shell_choice
case $shell_choice in
    1)
        sudo apt install -y zsh
        rm -rf "$HOME/.oh-my-zsh"
        sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)" "" --unattended

        ZSH_CUSTOM="$HOME/.oh-my-zsh/plugins"
        git clone https://github.com/zsh-users/zsh-syntax-highlighting.git "$ZSH_CUSTOM/zsh-syntax-highlighting"
        git clone https://github.com/zsh-users/zsh-autosuggestions.git "$ZSH_CUSTOM/zsh-autosuggestions"
        git clone https://github.com/jeffreytse/zsh-vi-mode.git "$ZSH_CUSTOM/zsh-vi-mode"

        rm -f ~/.zshrc
        rm -f ~/.bashrc
        stow -d "$DOTFILES_DIR" -t "$HOME" shell
        sudo chsh -s "$(command -v zsh)" "$USER"
        ;;
    2)
        sudo apt install -y zsh
        rm -rf "$HOME/.oh-my-zsh"
        sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)" "" --unattended

        ZSH_CUSTOM="$HOME/.oh-my-zsh/custom/plugins"
        git clone https://github.com/zsh-users/zsh-syntax-highlighting.git "$ZSH_CUSTOM/zsh-syntax-highlighting"
        git clone https://github.com/zsh-users/zsh-autosuggestions.git "$ZSH_CUSTOM/zsh-autosuggestions"
        git clone https://github.com/jeffreytse/zsh-vi-mode.git "$ZSH_CUSTOM/zsh-vi-mode"

        rm -f ~/.zshrc
        rm -f ~/.bashrc
        stow -d "$DOTFILES_DIR" -t "$HOME" shell
        echo "已安装 zsh，但继续使用 bash 作为默认终端。"
        ;;
    3)
        echo "不安装 zsh。"
        rm -f ~/.zshrc
        rm -f ~/.bashrc
        stow -d "$DOTFILES_DIR" -t "$HOME" shell
        ;;
    *)
        echo "跳过"
        ;;
esac