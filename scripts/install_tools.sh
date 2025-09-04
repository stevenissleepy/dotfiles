#!/usr/bin/env bash
set -e  # 在出现错误时停止脚本

source "$(dirname "$0")/env.sh"

# 安装 build-essential
install_build_essential() {
    sleep 2
    clear
    echo -e "\033[1;36m🔹 正在安装 build_essential ...\033[0m"
    sudo apt install -y build-essential libssl-dev
}

# 安装 Python 3
install_python() {
    sleep 2
    clear
    if ! command -v python3 &> /dev/null; then
      echo -e "\033[1;36m🔹 正在安装 python3 ...\033[0m"
      sudo apt install -y python3 python3-pip
    else
      echo -e "\033[1;32m✅ python3 已安装，跳过...\033[0m"
    fi
}

# 安装 CMake
install_cmake() {
    sleep 2
    clear
    if ! command -v cmake &> /dev/null; then
        echo -e "\033[1;36m🔹 正在安装 cmake 与 Ninja ...\033[0m"
        sudo apt install -y cmake ninja-build
    else
        echo -e "\033[1;32m✅ cmake 已安装，跳过...\033[0m"
    fi
}

# 安装 stow
install_stow() {
    sleep 2
    clear
    if ! command -v stow &> /dev/null; then
        echo -e "\033[1;36m🔹 正在安装 stow ...\033[0m"
        sudo apt install -y stow
    else
        echo -e "\033[1;32m✅ stow 已安装，跳过...\033[0m"
    fi
}

# 主执行流程
mkdir -p $TMP_DIR

install_build_essential
install_python
install_cmake
install_stow

rm -rf $TMP_DIR
