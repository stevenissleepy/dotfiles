import shutil
import subprocess
from pathlib import Path

from .installer import Installer


class NeovimInstaller(Installer):
    def __init__(self):
        super().__init__("neovim")

    def ask_install(self) -> bool:
        # 检查 Neovim 是否已安装
        if shutil.which("nvim") is not None:
            self.info("Neovim is already installed. Do you want to reinstall it? (y/N)")
            choice = input().strip().lower()
            return choice == "y"

        # 直接询问用户是否继续安装
        else:
            self.info("Neovim is not installed. Do you want to install it? (Y/n)")
            choice = input().strip().lower()
            return choice != "n"

    def pre_install(self):
        pass

    def install(self):
        self.info("Installing Neovim...")
        subprocess.run(["sudo", "pacman", "-S", "--noconfirm", "--needed", "neovim"], check=True)

    def post_install(self):
        self.info("Configuring Neovim...")

        subprocess.run(["stow", "-d", "configs", "-t", str(Path.home()), "nvim"], check=True)
