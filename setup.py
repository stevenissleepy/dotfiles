import os
import shutil
import argparse
import subprocess
from getpass import getpass

from installers import (
    tmp_dir,
    Installer,
    ClashInstaller,
    CommonInstaller,
    ZshInstaller,
    StarshipInstaller,
    NeovimInstaller,
    TmuxInstaller,
    CondaInstaller,
)


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--clash",
        metavar="URL",
        default=None,
        help="clash subscription url",
    )
    return parser.parse_args()


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
    args = parse_args()

    # get sudo password
    password = sudo_warmup()

    # 安装 clash 并启动
    if args.clash is not None:
        ClashInstaller.install()
        ClashInstaller.start(args.clash)
        ClashInstaller.proxy_on()

    # 安装 stow
    if shutil.which("stow") is None:
        Installer.info("Stow is not installed. Installing stow...")
        subprocess.run(["sudo", "pacman", "-S", "--noconfirm", "--needed", "stow"], check=True)

    # 运行各个 installer
    try:
        installers = [
            CommonInstaller(),
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
    if args.clash is not None:
        ClashInstaller.proxy_off()
        ClashInstaller.stop()
    shutil.rmtree(tmp_dir)


if __name__ == "__main__":
    main()
