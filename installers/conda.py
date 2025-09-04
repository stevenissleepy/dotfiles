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

        # 检查 Conda 是否已安装
        print("Checking if Conda is already installed...")
        if self.is_installed():
            print("Conda is already installed.")
            return

        # 下载并安装 Miniconda
        print("Installing Miniconda...")
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

        print("Conda installation complete. Please restart your shell.")

    def pre_install(self):
        pass
