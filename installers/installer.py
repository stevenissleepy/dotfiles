import os
from abc import ABC, abstractmethod


class Installer(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def ask_install(self) -> bool:
        """
        Ask the user whether to install the software.
        Returns True if the user wants to install, False otherwise.
        """
        pass

    @abstractmethod
    def pre_install(self):
        """
        Pre-installation steps.
        """
        pass

    @abstractmethod
    def install(self):
        """
        Installation steps.
        """
        pass

    @abstractmethod
    def post_install(self):
        """
        Post-installation steps.
        """
        pass

    # main method to run the installer
    def run(self):
        os.system("clear")
        if not self.ask_install():
            return
        self.pre_install()
        self.install()
        self.post_install()

    # utility method
    @staticmethod
    def info(str=""):
        print(f"\033[33m{str}\033[0m")
