import os
import shutil
import subprocess
from pathlib import Path

from .installer import Installer
from .config import (
    omz_path,
    omz_plugins_path,
    omz_plugins_urls,
    omz_installer_url,
    omz_installer_path,
)


class ZshInstaller(Installer):
    def __init__(self, password: str = ""):
        super().__init__("zsh")
        self.password_ = password

    def ask_install(self):
        # 检查 zsh 是否已安装
        if shutil.which("zsh") is not None:
            self.info("zsh is already installed. Do you want to reinstall it? (Y/n)")

        # 直接询问用户是否继续安装
        else:
            self.info("zsh is not installed. Do you want to install it? (Y/n)")

        choice = input().strip().lower()
        if choice == "n":
            self.info("Skipping zsh installation.")
            return False

        return True

    def pre_install(self) -> bool:
        pass

    def install(self):
        self.info("Installing zsh...")
        subprocess.run(["sudo", "apt-get", "install", "-y", "zsh"], check=True)

        # 安装 oh-my-zsh
        self.info("Installing oh-my-zsh...")
        shutil.rmtree(omz_path, ignore_errors=True)
        os.remove(str(omz_installer_path)) if omz_installer_path.exists() else None
        subprocess.run(["curl", "-fsSL", omz_installer_url, "-o", str(omz_installer_path)], check=True)
        subprocess.run(["sh", str(omz_installer_path), "--unattended", "--keep-zshrc"], check=True)

        # 安装 oh-my-zsh 插件
        self.info("Installing oh-my-zsh plugins...")
        omz_plugins_path.mkdir(parents=True, exist_ok=True)
        for plugin, url in omz_plugins_urls.items():
            plugin_path = omz_plugins_path / plugin
            if not plugin_path.exists():
                subprocess.run(["git", "clone", url, str(plugin_path)], check=True)

    def post_install(self):
        self.info("Configuring zsh...")

        # 设置 zsh 为默认 shell
        username = os.environ["USER"]
        password = self.password_ + "\n"
        subprocess.run(["chsh", "-s", shutil.which("zsh"), username], input=password, text=True, check=True)

        # stow .zshrc
        zshrc_path = Path.home() / ".zshrc"
        if zshrc_path.exists() and not zshrc_path.is_symlink():
            backup_path = zshrc_path.with_suffix(".bak")
            zshrc_path.rename(backup_path)
        subprocess.run(["stow", "zsh"], check=True)
