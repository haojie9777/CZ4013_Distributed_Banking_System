import sys

from controllers import BaseController, CheckAccountBalanceController, CloseAccountController, \
    OpenAccountController, SubscribeUpdatesController, TransferMoneyController, DepositMoneyController, WithdrawMoneyController

from communication import *


class MainPageController(BaseController):
    """
    This is the controller of the main page that the user see on launching. All other controllers are accessed here.
    """

    @property
    def message(self):
        return 'Welcome to iDamnNerd Bank!'

    @property
    def options(self):
        return [
            "Open a new account",
            "Close an account",
            "Deposit Money",
            "Withdraw Money",
            "Subscribe to updates",
            "Transfer Money to another account",
            "Check account balance",
            "Exit"
        ]

    def execute(self):
        self.show_options()
        self.handler(get_menu_option(max_choice=len(self.options)))

    def handler(self, user_choice):
        """
        This forwards the user to subsequent controllers
        :param user_choice: choice of service
        :return:
        """
        if user_choice == 0:
            OpenAccountController().start()
        elif user_choice == 1:
            CloseAccountController().start()
        elif user_choice == 2:
            DepositMoneyController().start()
        elif user_choice == 3:
            WithdrawMoneyController().start()
        elif user_choice == 4:
            SubscribeUpdatesController().start()
        elif user_choice == 5:
            TransferMoneyController().start()
        elif user_choice == 6:
            CheckAccountBalanceController().start()
        else:
            self.exit()

    @staticmethod
    def exit():
        """
        Terminate the program
        :return:
        """
        print_message("Thank You for Using iDamnNerdBank.")
        sys.exit()
