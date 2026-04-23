import shutil
import subprocess
from pathlib import Path

from .installer import Installer
from .config import (
    tmux_tpm_url,
    tmux_tpm_path,
    tmux_catppuccin_version,
    tmux_catppuccin_url,
    tmux_catppuccin_path,
)


class TmuxInstaller(Installer):
    def __init__(self):
        super().__init__("tmux")

    def ask_install(self):
        # 检查 tmux 是否已安装
        if shutil.which("tmux") is not None:
            self.info("Tmux is already installed. Do you want to reinstall it? (y/N)")
            choice = input().strip().lower()
            return choice == "y"

        # 直接询问用户是否继续安装
        else:
            self.info("Tmux is not installed. Do you want to install it? (Y/n)")
            choice = input().strip().lower()
            return choice != "n"

    def pre_install(self):
        pass

    def install(self):
        # 安装 tmux
        subprocess.run(["sudo", "pacman", "-S", "--noconfirm", "--needed", "tmux"], check=True)

    def post_install(self):
        self.info("Configuring tmux...")

        # tpm
        tpm_url = tmux_tpm_url
        tpm_path = tmux_tpm_path
        subprocess.run(["git", "clone", tpm_url, str(tpm_path)], check=True)

        # catppuccin
        cpc_ver = tmux_catppuccin_version
        cpc_url = tmux_catppuccin_url
        cpc_path = tmux_catppuccin_path
        subprocess.run(["git", "clone", "-b", cpc_ver, cpc_url, str(cpc_path)], check=True)

        # stow tmux
        subprocess.run(["stow", "-d", "configs", "-t", str(Path.home()), "tmux"], check=True)
