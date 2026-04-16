import shutil
import subprocess
from pathlib import Path

from .installer import Installer


class StarshipInstaller(Installer):
    def __init__(self):
        super().__init__("starship")

    def ask_install(self):
        # 检查 starship 是否已安装
        if shutil.which("starship") is not None:
            self.info("starship is already installed. Do you want to reinstall it? (y/N)")
            choice = input().strip().lower()
            return choice == "y"

        # 直接询问用户是否继续安装
        else:
            self.info("starship is not installed. Do you want to install it? (Y/n)")
            choice = input().strip().lower()
            return choice != "n"

    def pre_install(self):
        pass

    def install(self):
        self.info("Installing Starship...")
        subprocess.run(["sudo", "pacman", "-S", "--noconfirm", "--needed", "starship"], check=True)

    def post_install(self):
        self.info("Configuring Starship...")

        # stow starship
        subprocess.run(["stow", "-d", "configs", "-t", str(Path.home()), "starship", ], check=True)
