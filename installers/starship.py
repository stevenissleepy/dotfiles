import os
import shutil
import subprocess

from .installer import Installer
from .config import starship_installer_url, starship_installer_path


class StarshipInstaller(Installer):
    def __init__(self):
        super().__init__("starship")

    def ask_install(self):
        # 检查 starship 是否已安装
        if shutil.which("starship") is not None:
            self.info("starship is already installed. Do you want to reinstall it? (Y/n)")

        # 直接询问用户是否继续安装
        else:
            self.info("starship is not installed. Do you want to install it? (Y/n)")

        choice = input().strip().lower()
        if choice == "n":
            self.info("Skipping starship installation.")
            return False

        return True

    def pre_install(self):
        pass

    def install(self):
        # 安装 Starship
        self.info("Installing Starship...")
        installer_url = starship_installer_url
        installer_path = starship_installer_path
        subprocess.run(["curl", "-sS", installer_url, "-o", installer_path], check=True)
        subprocess.run(["sh", installer_path, "-y"], check=True)

    def post_install(self):
        self.info("Configuring Starship...")

        # stow starship
        subprocess.run(["stow", "starship"], check=True)
