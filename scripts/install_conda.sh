install_conda(){
    sleep 2
    clear

    if ! command -v conda &> /dev/null; then
        echo -e "\033[1;36m🔹 正在安装 Miniconda Dependencies ...\033[0m"
        sudo apt install -y curl bzip2

        sleep 2
        clear
        echo -e "\033[1;36m🔹 正在安装 Miniconda ...\033[0m"

        # 设置 Miniconda 安装目录和下载链接
        MINICONDA_VERSION="latest"
        INSTALL_DIR="$HOME/tools/miniconda3"
        INSTALLER="Miniconda3-$MINICONDA_VERSION-Linux-x86_64.sh"
        MINICONDA_URL="https://repo.anaconda.com/archive/$INSTALLER"


        # 下载 Miniconda 安装脚本
        cd $TMP_DIR
        curl -O $MINICONDA_URL

        # 运行安装脚本
        bash $INSTALLER -b -p $INSTALL_DIR

        echo -e "\033[1;32m✅ conda success\033[0m"
    else
        echo -e "\033[1;32m✅ conda 已安装，跳过...\033[0m"
    fi
}

install_conda