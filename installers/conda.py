import os
import shutil
import subprocess

from .installer import Installer
from .config import tmp_dir, miniconda_path, miniconda_url


class CondaInstaller(Installer):
    def __init__(self):
        super().__init__("conda")
        self.url = miniconda_url
        self.installer_path = tmp_dir / "miniconda_installer.sh"
        self.install_path = miniconda_path

    def is_installed(self):
        return shutil.which("conda") is not None

    def install(self):
        os.system("clear")

        # 是否需要安装 Conda
        if not self.pre_install():
            return

        # 下载并安装 Miniconda
        self.info("Installing Miniconda...")
        subprocess.run(["curl", "-o", str(self.installer_path), self.url], check=True)
        subprocess.run(
            [
                "bash",
                str(self.installer_path),
                "-b",
                "-u",
                "-p",
                str(self.install_path),
            ],
            check=True,
        )
        subprocess.run([str(self.install_path / "bin" / "conda"), "init"], check=True)

        self.info("Conda installation complete. Please restart your shell.")

    def pre_install(self) -> bool:
        # 检查 Conda 是否已安装
        if self.is_installed():
            self.info("Conda is already installed. Do you want to reinstall it? (Y/n)")

        # 直接询问用户是否继续安装
        else:
            self.info("Conda is not installed. Do you want to install it? (Y/n)")

        choice = input().strip().lower()
        if choice == "n":
            self.info("Skipping Conda installation.")
            return False

        return True
