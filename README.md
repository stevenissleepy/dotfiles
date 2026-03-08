# Steven's dotfiles

## ✨ 介绍

这是 Steven 的的个人代码环境自动化部署工具，为 Zsh + Noevim + Tmux workflow 而设计


## 🚀 Features

1. 自动安装并启用 clash，为后续安装做准备
2. 简单配置 `bash` `git` `vim`
3. 安装 zsh 和插件 zsh-autosuggestions, zsh-syntax-highlighting
4. 安装 starship 并使用我的配置
5. 安装 neovim 并使用我的配置
6. 安装 conda，关闭 conda 的默认启动，禁止 conda 修改 prompt


## 📥 Usage

将 `.env` 下的 `CLASH_URL` 改为你自己的订阅链接，然后运行

```sh
python setup.py
```
 

