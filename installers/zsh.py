import os
import shutil
import subprocess

from .installer import Installer
from .config import (
    zshrc_path,
    zsh_alias_path,
    zsh_path_path,
    omz_url,
    omz_path,
    omz_plugins_path,
    omz_plugins_urls,
    omz_installer_url,
    omz_installer_path,
)


class ZshInstaller(Installer):
    def __init__(self):
        super().__init__("zsh")

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
        subprocess.run(
            ["bash", str(omz_installer_path), "--unattended", "--keep-zshrc"],
            env={**os.environ, "REMOTE": omz_url},
            check=True,
        )

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
        subprocess.run(["sudo", "chsh", "-s", shutil.which("zsh")], check=True)

        # stow .zshrc
        os.remove(str(zshrc_path)) if zshrc_path.exists() else None
        os.remove(str(zsh_alias_path)) if zsh_alias_path.exists() else None
        os.remove(str(zsh_path_path)) if zsh_path_path.exists() else None
        subprocess.run(["stow", "zsh"], check=True)
