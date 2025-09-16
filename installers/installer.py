from abc import ABC, abstractmethod


class Installer(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def is_installed(self):
        pass

    @abstractmethod
    def install(self):
        pass

    @abstractmethod
    def pre_install(self):
        pass

    def info(self, str = ""):
        print(f"\033[33m{str}\033[0m")