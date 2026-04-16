# Steven's dotfiles

## ✨ 介绍

这是 Steven 的的个人代码环境自动化部署工具，为 Zsh + Neovim + Tmux workflow 而设计


## 🚀 Features

1. 安装 clash
2. 简单配置 `bash` `git` `vim`
3. 安装 zsh 和插件 zsh-autosuggestions, zsh-syntax-highlighting
4. 安装 starship 并使用我的配置
5. 安装 neovim 并使用我的配置
6. 安装 conda，关闭 conda 的默认启动，禁止 conda 修改 prompt


## 📥 Usage

一键安装

```sh
python setup.py
```
 
如果连不上 github 或是网络环境有其它问题，脚本也提供了自动开启 clash 的功能。
```sh
echo "export CLASH_URL='your_clash_subscribe_url_here'" > .env
python setup.py --clash on
```
