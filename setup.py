import os
import shutil
import subprocess
from getpass import getpass

from installers import (
    tmp_dir,
    Installer,
    ClashInstaller,
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
    ClashInstaller.install()
    ClashInstaller.start()
    ClashInstaller.proxy_on()

    # 安装 stow
    if shutil.which("stow") is None:
        Installer.info("Stow is not installed. Installing stow...")
        subprocess.run(["sudo", "apt-get", "install", "-y", "stow"], check=True)

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
    ClashInstaller.proxy_off()
    shutil.rmtree(tmp_dir)


if __name__ == "__main__":
    main()
