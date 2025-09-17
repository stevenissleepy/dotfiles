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

    def is_installed(self):
        return shutil.which("zsh") is not None

    def install(self):
        os.system("clear")

        # 是否需要安装 Zsh
        if not self.pre_install():
            return

        # 安装 Zsh
        self.info("Installing Zsh...")
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

        # 配置 Zsh
        self.post_install()

    def pre_install(self) -> bool:
        # 检查并询问用户是否继续安装
        if self.is_installed():
            self.info("Zsh is already installed. Do you want to reinstall it? (Y/n)")
        else:
            self.info("Zsh is not installed. Do you want to install it? (Y/n)")

        choice = input().strip().lower()
        if choice == "n":
            self.info("Skipping Zsh installation.")
            return False

        return True

    def post_install(self):
        self.info("Configuring Zsh...")

        # 设置 Zsh 为默认 shell
        subprocess.run(["sudo", "chsh", "-s", shutil.which("zsh")], check=True)

        # 检查 stow 是否安装
        if shutil.which("stow") is None:
            self.info("Stow is not installed. Installing stow...")
            subprocess.run(["sudo", "apt-get", "install", "-y", "stow"], check=True)

        # stow .zshrc
        os.remove(str(zshrc_path)) if zshrc_path.exists() else None
        os.remove(str(zsh_alias_path)) if zsh_alias_path.exists() else None
        os.remove(str(zsh_path_path)) if zsh_path_path.exists() else None
        subprocess.run(["stow", "zsh"], check=True)
