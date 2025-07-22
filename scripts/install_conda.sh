install_conda(){
    sleep 2
    clear

    if ! command -v conda &> /dev/null; then
        echo -e "\033[1;36m🔹 正在安装 Anaconda Dependencies ...\033[0m"
        sudo apt install -y curl bzip2

        sleep 2
        clear
        echo -e "\033[1;36m🔹 正在安装 Anaconda ...\033[0m"

        # 设置 Anaconda 安装目录和下载链接
        ANACONDA_VERSION="2024.10-1"
        INSTALL_DIR="$HOME/tools/anaconda3"
        INSTALLER="Anaconda3-$ANACONDA_VERSION-Linux-x86_64.sh"
        ANACONDA_URL="https://repo.anaconda.com/archive/$INSTALLER"


        # 下载 Anaconda 安装脚本
        cd $TMP_DIR
        curl -O $ANACONDA_URL

        # 运行安装脚本
        bash $INSTALLER -b -p $INSTALL_DIR

        echo -e "\033[1;32m✅ conda success\033[0m"
    else
        echo -e "\033[1;32m✅ conda 已安装，跳过...\033[0m"
    fi
}

install_conda