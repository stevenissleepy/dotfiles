import os
import shutil
import subprocess
from pathlib import Path

from .installer import Installer
from .config import tmp_dir, miniconda_path


class CondaInstaller(Installer):
    def __init__(self):
        super().__init__("conda")
        self.url = "https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86.sh"
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
        self.install_path.mkdir(parents=True, exist_ok=True)
        subprocess.run(["curl", "-o", str(self.installer_path), self.url], check=True)
        subprocess.run(["bash", str(self.installer_path), "-b", "-p", str(self.install_path)], check=True)
        subprocess.run([str(self.install_path / "bin" / "conda"), "init"], check=True)

        print("Conda installation complete. Please restart your shell.")

    def install_dependencies(self):
        pass

