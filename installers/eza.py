import subprocess
from .installer import Installer


class EzaInstaller(Installer):
    def __init__(self):
        super().__init__("eza")

    def ask_install(self) -> bool:
        return True

    def pre_install(self):
        self.info("Preparing to install eza...")

    def install(self):
        self.info("Installing eza...")
        subprocess.run(["sudo", "pacman", "-S", "--noconfirm", "--needed", "eza"], check=True)

    def post_install(self):
        pass
