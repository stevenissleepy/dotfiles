from pathlib import Path
import shutil
import subprocess
from .installer import Installer
from .config import neovim_appimage_url, neovim_appimage_path, neovim_glibc_min_version


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
        appimage_url = neovim_appimage_url
        appimage_path = Path(neovim_appimage_path)

        # 删除已有的 AppImage 文件
        subprocess.run(["sudo", "rm", "-rf", str(appimage_path.parent)], check=True)
        subprocess.run(["sudo", "mkdir", "-p", str(appimage_path.parent)], check=True)

        # 下载 Neovim AppImage
        subprocess.run(["sudo", "curl", "-L", "-o", str(appimage_path), appimage_url], check=True)
        subprocess.run(["sudo", "chmod", "755", str(appimage_path)], check=True)

        # 创建 symlink 到 /usr/local/bin
        symlink_path = Path("/usr/local/bin/nvim")
        subprocess.run(["sudo", "ln", "-sf", str(appimage_path), str(symlink_path)], check=True)

    def post_install(self):
        self.info("Configuring Neovim...")

        subprocess.run(["stow", "nvim"], check=True)
