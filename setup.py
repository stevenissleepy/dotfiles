import os
import shutil
import subprocess
from getpass import getpass

from clash import install_clash, clash_start, proxy_on
from installers import (
    Installer,
    CommonInstaller,
    EzaInstaller,
    ZshInstaller,
    StarshipInstaller,
    NeovimInstaller,
    CondaInstaller,
)


def main():
    # get sudo password
    password = getpass(f"[sudo] password for {os.environ['USER']}:")
    subprocess.run(["sudo", "-v"], input=password + "\n", text=True, check=True)

    # 安装 clash 并启动
    install_clash()
    clash_start()
    proxy_on()

    # 安装 stow
    if shutil.which("stow") is None:
        Installer.info("Stow is not installed. Installing stow...")
        subprocess.run(["sudo", "apt-get", "install", "-y", "stow"], check=True)

    # 运行各个 installer
    installers = [
        CommonInstaller(),
        EzaInstaller(),
        ZshInstaller(password),
        StarshipInstaller(),
        NeovimInstaller(),
        CondaInstaller(),
    ]
    for installer in installers:
        installer.run()


if __name__ == "__main__":
    main()
