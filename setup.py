from installers import CondaInstaller


def main():
    installers = [CondaInstaller()]

    for installer in installers:
        installer.pre_install()
        installer.install()

if __name__ == "__main__":
    main()