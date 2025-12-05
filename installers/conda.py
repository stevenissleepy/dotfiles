import os
import shutil
import subprocess

from .installer import Installer
from .config import tmp_dir, miniconda_path, miniconda_installer_url, miniconda_installer_path


class CondaInstaller(Installer):
    def __init__(self):
        super().__init__("conda")

    def ask_install(self) -> bool:
        # 检查 Conda 是否已安装
        if shutil.which("conda") is not None:
            self.info("Conda is already installed. Do you want to reinstall it? (y/N)")
            choice = input().strip().lower()
            return choice == "y"

        # 直接询问用户是否继续安装
        else:
            self.info("Conda is not installed. Do you want to install it? (Y/n)")
            choice = input().strip().lower()
            return choice != "n"

    def pre_install(self):
        pass

    def install(self):
        self.info("Installing Miniconda...")
        installer_url = miniconda_installer_url
        installer_path = miniconda_installer_path
        subprocess.run(["curl", "-o", str(installer_path), installer_url], check=True)
        subprocess.run(["bash", str(installer_path), "-b", "-u", "-p", str(miniconda_path)], check=True)

    def post_install(self):
        self.info("Configuring Miniconda...")

        # 禁用自动激活 base 环境
        # 禁止 conda 修改提示信息
        conda_path = miniconda_path / "bin" / "conda"
        subprocess.run([str(conda_path), "config", "--set", "auto_activate", "false"], check=True)
        subprocess.run([str(conda_path), "config", "--set", "changeps1", "false"], check=True)

        self.info("Conda installation complete.")
        pass
