ask_install() {
    sleep 2
    clear
    local package="$1"

    # 如果已安装，直接跳过
    if command -v "$package" &> /dev/null && ! $RE_INSTALL ; then
        echo -e "\033[1;32m✅ $package 已安装，跳过...\033[0m"
        return 1
    fi

    # 询问是否安装该模块
    read -p "👉 是否安装 $package? (y/N) " choice
    [[ "$choice" == [Yy] ]] && echo -e "\n\033[1;36m🔹 正在安装 $package...\033[0m" && return 0
    return 1
}

stow_module() {
    stow -d "$DOTFILES_DIR" -t "$HOME" "$1"
}