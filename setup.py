import os
import shutil
import subprocess
from getpass import getpass

from clash import install_clash, clash_start, proxy_on, proxy_off
from installers import (
    tmp_dir,
    Installer,
    CommonInstaller,
    EzaInstaller,
    ZshInstaller,
    StarshipInstaller,
    NeovimInstaller,
    TmuxInstaller,
    CondaInstaller,
)


def sudo_warmup() -> str:
    password = getpass(f"[sudo] password for {os.environ['USER']}: ")
    try:
        subprocess.run(
            ["sudo", "-S", "-v"],
            input=password + "\n",
            text=True,
            check=True,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )
    except subprocess.CalledProcessError:
        print("Sorry, try again.")
        return sudo_warmup()
    return password


def main():
    # get sudo password
    password = sudo_warmup()

    # 安装 clash 并启动
    install_clash()
    clash_start()
    proxy_on()

    # 安装 stow
    if shutil.which("stow") is None:
        Installer.info("Stow is not installed. Installing stow...")
        subprocess.run(["sudo", "pacman", "-S", "--noconfirm", "--needed", "stow"], check=True)

    # 运行各个 installer
    try:
        installers = [
            CommonInstaller(),
            EzaInstaller(),
            ZshInstaller(password),
            StarshipInstaller(),
            NeovimInstaller(),
            TmuxInstaller(),
            CondaInstaller(),
        ]
        for installer in installers:
            installer.run()
    except Exception as e:
        print(f"Error occurred: {e}")

    # 关闭 clash 并清理临时文件
    proxy_off()
    shutil.rmtree(tmp_dir)


if __name__ == "__main__":
    main()
