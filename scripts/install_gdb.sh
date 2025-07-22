# Install gdb
install_gdb() {
    sleep 2
    clear

    # 检查是否已安装 GDB
    if ! command -v gdb &> /dev/null; then
        echo -e "\033[1;36m🔹 正在安装 gdb ...\033[0m"
        TARGET_GDB_VERSION="15.2"  # 可修改为其他新版本

        # 安装编译依赖
        sudo apt install -y texinfo libgmp3-dev libmpfr-dev libmpc-dev libncurses-dev

        # 下载并编译 GDB
        cd $TMP_DIR
        wget "http://ftp.gnu.org/gnu/gdb/gdb-${TARGET_GDB_VERSION}.tar.gz"
        tar -zxvf "gdb-${TARGET_GDB_VERSION}.tar.gz"
        cd "gdb-${TARGET_GDB_VERSION}"

        ./configure --enable-tui
        make -j$(nproc)
        sudo make install

        # 清理临时文件
        cd ..
        rm -rf "gdb-${TARGET_GDB_VERSION}"*
    else
        echo -e "\033[1;32m✅ gdb 已安装，跳过...\033[0m"
    fi
}

install_gdb