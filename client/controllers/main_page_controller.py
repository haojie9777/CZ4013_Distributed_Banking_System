import sys

from controllers import BaseController, CheckAccountBalanceController, CloseAccountController, \
    OpenAccountController, FacilityBookingChangingController, FacilityAvailSubscribingController, DepositMoneyController, WithdrawMoneyController
from utils import *
from helpers import *


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
            "Subscribe to updates",
            "Deposit Money",
            "Withdraw Money",
            "Check account balance",
            "Transfer Money to another account",
            "Exit"
        ]

    def enter(self, *args, **kwargs):
        self.show_message()
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
            CloseAccountController.start()
        elif user_choice == 2:
            FacilityBookingController(facility_name_list=self.retrieve_facility_name_list()).start()
        elif user_choice == 3:
            DepositMoneyController.start()
        elif user_choice == 4:
            WithdrawMoneyController().start()
        elif user_choice == 5:
            CheckAccountBalanceController.start()
        elif user_choice == 6:
            FacilityAvailSubscribingController(facility_name_list=self.retrieve_facility_name_list()).start()
        else:
            self.exit()

    @staticmethod
    def retrieve_facility_name_list():
        """
        This retrieves the name list of all facilities from the server
        :return: list of facility names
        """
        try:
            reply_msg = request(service=ServiceType.FACILITY_NAMELIST_CHECKING)
            if reply_msg.msg_type == MessageType.REPLY:
                return reply_msg.data[0]
            else:
                raise Exception(reply_msg.error_msg)
        except Exception as e:
            print_error(f"Server Unavailable: {str(e)}. Please Try Again Later.")
            sys.exit()

    @staticmethod
    def exit():
        """
        Terminate the program
        :return:
        """
        print_message("Thank You for Using iDamnNerdBank.")
        sys.exit()
