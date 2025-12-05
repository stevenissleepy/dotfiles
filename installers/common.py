import subprocess
from pathlib import Path

from .installer import Installer


class CommonInstaller(Installer):
    def __init__(self, name: str = "common"):
        super().__init__(name)

    def ask_install(self) -> bool:
        return True

    def pre_install(self):
        pass

    def install(self):
        self.info("Installing common components...")
        subprocess.run(["sudo", "apt", "install", "-y", "git"], check=True)
        subprocess.run(["sudo", "apt", "install", "-y", "vim"], check=True)

    def post_install(self):
        self.info("configuring bash git vim...")

        # stow dotfiles in ./common
        self.backup_dotfiles_()
        subprocess.run(["stow", "common"], check=True)

    def backup_dotfiles_(self):
        files = [p.name for p in Path("common").iterdir() if p.is_file()]
        home_files = [Path.home() / file for file in files]
        for file in home_files:
            if file.exists() and not file.is_symlink():
                backup_path = file.with_suffix(file.suffix + ".backup")
                file.rename(backup_path)
