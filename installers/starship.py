import os
import shutil
import subprocess

from .installer import Installer
from .config import starship_url, starship_installer_url, starship_installer_path


class StarshipInstaller(Installer):
    def __init__(self):
        super().__init__("starship")

    def is_installed(self):
        return shutil.which("starship") is not None

    def install(self):
        os.system("clear")

        # 是否需要安装 Starship
        if not self.pre_install():
            return

        # 安装 Starship
        self.info("Installing Starship...")
        installer_url = starship_installer_url
        installer_path = starship_installer_path
        subprocess.run(["curl", "-fsSL", installer_url, "-o", installer_path], check=True)
        subprocess.run(
            [
                "sh",
                str(installer_path),
                "-y",
                "-B",
                str(starship_url),
            ],
            check=True,
        )

        # 配置 Starship
        self.post_install()

    def pre_install(self) -> bool:
        # 检查并询问用户是否继续安装
        if self.is_installed():
            self.info("Starship is already installed. Do you want to reinstall it? (Y/n): ")
        else:
            self.info("Starship is not installed. Do you want to install it? (Y/n): ")

        choice = input().strip().lower()
        return choice not in ("no", "n")

    def post_install(self):
        self.info("Configuring Starship...")

        # 检查 stow 是否安装
        if shutil.which("stow") is None:
            self.info("Stow is not installed. Installing stow...")
            subprocess.run(["sudo", "apt-get", "install", "-y", "stow"], check=True)

        # stow starship
        subprocess.run(["stow", "starship"], check=True)
