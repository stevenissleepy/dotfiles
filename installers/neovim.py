import shutil
import subprocess
from pathlib import Path

from .installer import Installer
from .config import (
    tmp_dir,
    neovim_glibc_min_version,
    neovim_url,
    neovim_appimage_dir,
    neovim_bin_dir,
)


class NeovimInstaller(Installer):
    def __init__(self):
        super().__init__("neovim")

    def ask_install(self) -> bool:
        # 检查 glibc 版本
        ldd_output = subprocess.run(["ldd", "--version"], capture_output=True, text=True, check=True)
        glibc_version = ldd_output.stdout.splitlines()[0].split()[-1]
        if glibc_version < neovim_glibc_min_version:
            self.info(f"Your glibc version ({glibc_version}) is lower than ({neovim_glibc_min_version}).")
            self.info("You may need to install Neovim from source")
            return False

        # 检查 Neovim 是否已安装
        if shutil.which("nvim") is not None:
            self.info("Neovim is already installed. Do you want to reinstall it? (y/N)")
            choice = input().strip().lower()
            return choice == "y"

        # 直接询问用户是否继续安装
        else:
            self.info("Neovim is not installed. Do you want to install it? (Y/n)")
            choice = input().strip().lower()
            return choice != "n"

    def pre_install(self):
        pass

    def install(self):
        self.info("Installing Neovim...")

        # 删除已有的 AppImage 文件
        subprocess.run(["sudo", "rm", "-rf", str(neovim_appimage_dir)], check=True)
        subprocess.run(["sudo", "mkdir", "-p", str(neovim_appimage_dir)], check=True)

        # 下载 Neovim AppImage
        appimage_tmp = tmp_dir / "nvim.appimage"
        appimage = neovim_appimage_dir / "nvim.appimage"
        subprocess.run(["curl", "-fL", neovim_url, "-o", str(appimage_tmp)], check=True)
        subprocess.run(["sudo", "mv", str(appimage_tmp), str(appimage)], check=True)
        subprocess.run(["sudo", "chmod", "755", str(appimage)], check=True)

        # 创建 symlink 到 /usr/local/bin
        neovim_bin = neovim_bin_dir / "nvim"
        subprocess.run(["sudo", "mkdir", "-p", str(neovim_bin_dir)], check=True)
        subprocess.run(["sudo", "ln", "-sf", str(appimage), str(neovim_bin)], check=True)

    def post_install(self):
        self.info("Configuring Neovim...")

        subprocess.run(["stow", "-d", "configs", "-t", str(Path.home()), "nvim"], check=True)
