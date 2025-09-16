from installers import CondaInstaller


def main():
    installers = [CondaInstaller()]

    for installer in installers:
        installer.install()

if __name__ == "__main__":
    main()