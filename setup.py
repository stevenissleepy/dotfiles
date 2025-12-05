import shutil
import subprocess

from installers import Installer, CondaInstaller, ZshInstaller, StarshipInstaller


def main():
    subprocess.run(["sudo", "-v"], check=True)

    # 安装 stow
    if shutil.which("stow") is None:
        Installer.info("Stow is not installed. Installing stow...")
        subprocess.run(["sudo", "apt-get", "install", "-y", "stow"], check=True)

    # 运行各个 installer
    installers = [
        # CondaInstaller(),
        # ZshInstaller(),
        StarshipInstaller(),
    ]
    for installer in installers:
        installer.run()


if __name__ == "__main__":
    main()
