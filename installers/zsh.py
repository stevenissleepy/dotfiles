import shutil
import subprocess
from pathlib import Path

from .installer import Installer
from .config import zsh_plugins


class ZshInstaller(Installer):
    def __init__(self, password: str = ""):
        super().__init__("zsh")
        self.password_ = password

    def ask_install(self):
        # 检查 zsh 是否已安装
        if shutil.which("zsh") is not None:
            self.info("zsh is already installed. Do you want to reinstall it? (y/N)")
            choice = input().strip().lower()
            return choice == "y"

        # 直接询问用户是否继续安装
        else:
            self.info("zsh is not installed. Do you want to install it? (Y/n)")
            choice = input().strip().lower()
            return choice != "n"

    def pre_install(self) -> bool:
        pass

    def install(self):
        self.info("Installing zsh...")
        subprocess.run(["sudo", "apt-get", "install", "-y", "zsh"], check=True)

        # 安装 zsh 插件
        self.info("Installing zsh plugins...")
        subprocess.run(["sudo", "apt-get", "install", "-y"] + list(zsh_plugins), check=True)

    def post_install(self):
        self.info("Configuring zsh...")

        # 设置 zsh 为默认 shell
        password = self.password_ + "\n"
        subprocess.run(["chsh", "-s", shutil.which("zsh")], input=password + "\n", text=True, check=True)

        # stow .zshrc
        zshrc_path = Path.home() / ".zshrc"
        if zshrc_path.exists() and not zshrc_path.is_symlink():
            backup_path = zshrc_path.with_suffix(".bak")
            zshrc_path.rename(backup_path)
        subprocess.run(["stow", "zsh"], check=True)
