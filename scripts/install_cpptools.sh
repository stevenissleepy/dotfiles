install_vscode_cpptools() {
    sleep 2
    clear

    TOOLS_DIR="$HOME/tools"
    EXT_DIR="$TOOLS_DIR/vscode-cpptools"
    VSIX_FILE="$TOOLS_DIR/cpptools-linux-x64.vsix"
    DOWNLOAD_URL="https://github.com/microsoft/vscode-cpptools/releases/latest/download/cpptools-linux-x64.vsix"

    # 检查 OpenDebugAD7 是否已存在
    if [ -f "$EXT_DIR/extension/debugAdapters/bin/OpenDebugAD7" ]; then
        echo -e "\033[1;32m✅ vscode-cpptools 已安装，跳过...\033[0m"
        return
    fi

    echo -e "\033[1;36m🔹 正在下载并安装 vscode-cpptools ...\033[0m"

    mkdir -p "$TOOLS_DIR"
    cd "$TOOLS_DIR"

    wget -O "$VSIX_FILE" "$DOWNLOAD_URL"    # 下载 vscode-cpptools 扩展包
    unzip -o "$VSIX_FILE" -d "vscode-cpptools"  # 解压到 vscode-cpptools 文件夹
    rm "$VSIX_FILE"                         # 清理安装包
    chmod +x "$EXT_DIR/extension/debugAdapters/bin/OpenDebugAD7"

    echo -e "\033[1;32m✅ vscode-cpptools 安装完成！\033[0m"
}
