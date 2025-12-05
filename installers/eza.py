import subprocess
from .installer import Installer


class EzaInstaller(Installer):
    def __init__(self):
        super().__init__("eza")

    def ask_install(self) -> bool:
        return True

    def pre_install(self):
        self.info("Preparing to install eza...")

        # check eza repository
        result = subprocess.run(["apt-cache", "search", "^eza$"], capture_output=True, text=True)
        has_eza = "eza" in result.stdout
        if has_eza:
            return

        # add eza repository
        keyring_path = "/etc/apt/keyrings/gierens.gpg"
        list_path = "/etc/apt/sources.list.d/gierens.list"
        subprocess.run(["sudo", "apt", "install", "-y", "gpg"], check=True)
        subprocess.run(["sudo", "mkdir", "-p", "/etc/apt/keyrings"], check=True)
        deb_url = "https://raw.githubusercontent.com/eza-community/eza/main/deb.asc"
        result = subprocess.run(["wget", "-qO-", deb_url], check=True, capture_output=True)
        subprocess.run(["sudo", "gpg", "--dearmor", "-o", keyring_path], input=result.stdout, check=True)
        repo_line = f"deb [signed-by={keyring_path}] http://deb.gierens.de stable main\n"
        subprocess.run(["sudo", "tee", list_path], input=repo_line, text=True, check=True)
        subprocess.run(["sudo", "chmod", "644", keyring_path, list_path], check=True)
        subprocess.run(["sudo", "apt", "update"], check=True)

    def install(self):
        self.info("Installing eza...")
        subprocess.run(["sudo", "apt", "install", "-y", "eza"], check=True)

    def post_install(self):
        pass
