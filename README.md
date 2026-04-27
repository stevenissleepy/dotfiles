# Steven's dotfiles

## ✨ 介绍

这是 Steven 的的个人代码环境自动化部署工具，为 Zsh + Neovim + Tmux workflow 而设计


## 🚀 Features

1. 简单配置 `bash` `git` `vim`
2. 安装 zsh 和插件 zsh-autosuggestions, zsh-syntax-highlighting
3. 安装 starship 并使用我的配置
4. 安装 neovim 并使用我的配置
5. 安装 conda，关闭 conda 的默认启动，禁止 conda 修改 prompt


## 📥 Usage

一行代码即可立即完成配置

```sh
python setup.py
```

如果有网络问题，例如连不上 github 等，该脚本可以自动开启代理

```sh
python setup.py --clash your_clash_subscription_url
```


## 🌐 关于 Clash

关于本脚本使用的 clash，你可能需要知道下面这些内容

- 如果你选择使用 `--clash`，本脚本会
    - 在 `/usr/local/bin` 下面安装 clash 的 `mihomo` 内核
    - 创建 `/etc/systemd/system/mihomo.service` 服务
- 你可以使用机场提供的 clash 订阅链接，直接放在 `--clash` 后面即可
- 你也可以选择使用本地的 `yaml` 文件，例如 `--clash file:///home/abc/config.yaml`
- 本脚本会将订阅文件放在 `/etc/mihomo/config.yaml`
- 本脚本会在结束后退出代理环境，并且关闭 `mihomo.service` 服务

如果你打算以后长期使用本脚本提供的 clash 服务，你可以将 `mihomo.service` 设为开机启动

```sh
sudo systemctl enable --now mihomo
```

将以下的内容保存为一个 `proxy.sh` 脚本  

```sh
export http_proxy=http://127.0.0.1:7890
export https_proxy=http://127.0.0.1:7890
export no_proxy=127.0.0.1,localhost
export HTTP_PROXY=http://127.0.0.1:7890
export HTTPS_PROXY=http://127.0.0.1:7890
export NO_PROXY=127.0.0.1,localhost
echo -e "\033[32m[√] 已开启代理\033[0m"
```

这样以后就可以通过 `source proxy.sh` 一键启动代理

更多关于 clash 的内容，请参见[mihomo wiki](https://wiki.metacubex.one/startup/)

