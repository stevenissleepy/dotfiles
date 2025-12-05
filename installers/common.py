import subprocess
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
        subprocess.run(["sudo", "apt", "install", "-y", "eza"], check=True)

    def post_install(self):
        self.info("configuring bash git vim...")
        subprocess.run(["stow", "common"], check=True)
