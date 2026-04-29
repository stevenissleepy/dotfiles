import tempfile
import platform
from pathlib import Path

# 系统和架构
system = platform.system()
arch = platform.machine()

# 临时目录
tmp_dir = tempfile.mkdtemp(prefix="dotfiles-")
tmp_dir = Path(tmp_dir)

# clash
mihomo_config_dir = Path("/etc/mihomo/")
mihomo_service_dir = Path("/etc/systemd/system/")
mihomo_service_content = """[Unit]
Description=mihomo Daemon, Another Clash Kernel.
After=network.target NetworkManager.service systemd-networkd.service iwd.service

[Service]
Type=simple
LimitNPROC=500
LimitNOFILE=1000000
CapabilityBoundingSet=CAP_NET_ADMIN CAP_NET_RAW CAP_NET_BIND_SERVICE CAP_SYS_TIME CAP_SYS_PTRACE CAP_DAC_READ_SEARCH CAP_DAC_OVERRIDE
AmbientCapabilities=CAP_NET_ADMIN CAP_NET_RAW CAP_NET_BIND_SERVICE CAP_SYS_TIME CAP_SYS_PTRACE CAP_DAC_READ_SEARCH CAP_DAC_OVERRIDE
Restart=always
ExecStartPre=/usr/bin/sleep 1s
ExecStart=/usr/bin/mihomo -d /etc/mihomo
ExecReload=/bin/kill -HUP $MAINPID

[Install]
WantedBy=multi-user.target
"""


# miniconda
miniconda_installer_url = f"https://repo.anaconda.com/miniconda/Miniconda3-latest-{system}-{arch}.sh"
miniconda_installer_path = tmp_dir / "miniconda_installer.sh"
miniconda_path = Path.home() / "tools" / "miniconda3"

# zsh
zsh_plugins = {
    "zsh-autosuggestions",
    "zsh-syntax-highlighting",
}
zsh_tools = {
    "fastfetch",# fastfetch
    "eza",      # eza
    "zoxide",   # zoxide
    "fzf",      # fzf
    "yazi",     # yazi and its dependencies
    "ffmpeg",
    "7zip",
    "jq",
    "poppler",
    "fd",
    "ripgrep",
    "resvg",
    "imagemagick",
}

# tmux
tmux_tpm_url = "https://github.com/tmux-plugins/tpm"
tmux_tpm_path = Path.home() / ".config" / "tmux" / "plugins" / "tpm"
tmux_catppuccin_version = "v2.3.0"
tmux_catppuccin_url = "https://github.com/catppuccin/tmux.git"
tmux_catppuccin_path = Path.home() / ".config" / "tmux" / "plugins" / "catppuccin"
