import subprocess

from installers import CondaInstaller, ZshInstaller, StarshipInstaller


def main():
    subprocess.run(["sudo", "-v"], check=True)

    installers = [
        CondaInstaller(),
        ZshInstaller(),
        StarshipInstaller(),
    ]

    for installer in installers:
        installer.install()

if __name__ == "__main__":
    main()