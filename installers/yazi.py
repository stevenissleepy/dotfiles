import shutil
import subprocess
from pathlib import Path

from .installer import Installer
from .config import tmp_dir, yazi_deps, yazi_url, yazi_release, yazi_bin_dir


class YaziInstaller(Installer):
    def __init__(self):
        super().__init__("yazi")

    def ask_install(self) -> bool:
        # 检查 yazi 是否已安装
        if shutil.which("yazi") is not None:
            self.info("yazi is already installed. Do you want to reinstall it? (y/N)")
            choice = input().strip().lower()
            return choice == "y"
        
        # 直接询问用户是否继续安装
        else:
            self.info("yazi is not installed. Do you want to install it? (Y/n)")
            choice = input().strip().lower()
            return choice != "n"

    def pre_install(self):
        self.info("Preparing to install yazi...")

        deps = list(yazi_deps)
        subprocess.run(["sudo", "apt", "install", "-y"] + deps, check=True)

    def install(self):
        self.info("Installing yazi...")

        # download and extract yazi
        zip_path = tmp_dir / "yazi.zip"
        subprocess.run(["curl", "-L", yazi_url, "-o", str(zip_path)], check=True)
        subprocess.run(["unzip", "-o", str(zip_path), "-d", str(tmp_dir)], check=True)

        # install yazi and ya
        yazi_bin_tmp = tmp_dir / yazi_release / "yazi"
        ya_bin_tmp = tmp_dir / yazi_release / "ya"
        yazi_bin = yazi_bin_dir / "yazi"
        ya_bin = yazi_bin_dir / "ya"
        subprocess.run(["sudo", "mkdir", "-p", str(yazi_bin_dir)], check=True)
        subprocess.run(["sudo", "install", "-Dm755", str(yazi_bin_tmp), str(yazi_bin)], check=True)
        subprocess.run(["sudo", "install", "-Dm755", str(ya_bin_tmp), str(ya_bin)], check=True)

    def post_install(self):
        self.info("Configuring yazi...")

        # stow yazi
        subprocess.run(["stow", "-d", "configs", "-t", str(Path.home()), "yazi"], check=True)
