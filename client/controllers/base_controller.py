from abc import ABC, abstractmethod
from utils import print_message, print_options


class BaseController(ABC):
    def __init__(self):
        pass

    @property
    def message(self):
        """
        :return: greeting message of controller
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
        print the list of options on screen for the user to choose
        :return:
        """
        print_options(self.options)

    def start(self):
        """
        Start a controller
        :return:
        """
        while True:
            print_message(self.message)
            i = self.execute()
            if i == 0:
                return

    @abstractmethod
    def execute(self):
        """
        Execute the business logic once from start
        :return:
        """
        raise NotImplementedError



