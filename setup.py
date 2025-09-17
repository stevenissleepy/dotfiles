import subprocess

from installers import CondaInstaller, ZshInstaller


def main():
    subprocess.run(["sudo", "-v"], check=True)

    installers = [
        # CondaInstaller(),
        ZshInstaller()
    ]

    for installer in installers:
        installer.install()

if __name__ == "__main__":
    main()