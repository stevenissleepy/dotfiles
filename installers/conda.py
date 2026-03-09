import sys
import shutil
import subprocess
from pathlib import Path

from .installer import Installer
from .config import miniconda_path, miniconda_installer_url, miniconda_installer_path


class CondaInstaller(Installer):
    def __init__(self):
        super().__init__("conda")

    def ask_install(self) -> bool:
        # 防止用 conda 的 Python 重装 conda, 导致正在运行的 Python 解释器被覆盖而崩溃 
        running_exe = Path(sys.executable).resolve()
        miniconda_prefix = miniconda_path.resolve()
        if miniconda_prefix in running_exe.parents:
            self.info("Error: 你正在使用 conda 中的 python 来重装 conda，这会覆盖正在运行的 python 解释器，导致崩溃。")
            self.info("如果想要安装 conda，请使用系统 python 来重新运行该脚本。e.g. /usr/bin/python3 setup.py")
            self.info("按任意键继续...")
            choice = input().strip().lower()
            return False

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
        installer_path = str(miniconda_installer_path)
        subprocess.run(["curl", "-fL", installer_url, "-o", installer_path], check=True)
        subprocess.run(["bash", installer_path, "-b", "-u", "-p", str(miniconda_path)], check=True)

    def post_install(self):
        self.info("Configuring Miniconda...")

        condarc_path = Path.home() / ".condarc"
        if condarc_path.exists() and not condarc_path.is_symlink():
            backup_path = condarc_path.with_suffix(".bak")
            condarc_path.rename(backup_path)

        subprocess.run(["stow", "-d", "configs", "-t", str(Path.home()), "conda"], check=True)

