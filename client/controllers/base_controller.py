from abc import ABC, abstractmethod
from utils import print_message, print_options


class BaseController(ABC):
    def __init__(self):
        pass

    @property
    def message(self):
        """
        :return: menu for the user to choose
        """
        raise NotImplementedError

    @property
    def options(self):
        """
        :return: options for the user to choose
        """
        raise NotImplementedError

    def show_options(self):
        """
        print the menu to screen for the user to choose
        :return:
        """
        print_options(self.options)

    def start(self, *args, **kwargs):
        """
        Start an controller
        :param args:
        :param kwargs:
        :return:
        """
        while True:
            print_message(self.message)
            i = self.enter(*args, **kwargs)
            if i == 0:
                return

    @abstractmethod
    def enter(self, *args, **kwargs):
        """
        Enter the business logic once from start
        :param args:
        :param kwargs:
        :return:
        """
        raise NotImplementedError



