import shutil
import subprocess

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
    subprocess.run(["sudo", "-v"], check=True)

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
        ZshInstaller(),
        StarshipInstaller(),
        NeovimInstaller(),
        CondaInstaller(),
    ]
    for installer in installers:
        installer.run()


if __name__ == "__main__":
    main()
