from datetime import datetime

from controllers import BaseController
from utils import *
from helpers import *


class CheckAccountBalanceController(BaseController):
    """
    This is the controller used to check the availability of an facility on particular days
    """

    def __init__(self):
        super().__init__()
        self.ctrl_list = ['Back To Homepage', 'Make Another Query']

    @property
    def message(self):
        return None

    @property
    def options(self):
        return None

    def enter(self, *args, **kwargs) -> int:
        account_number = get_int_input(f'Please indicate account number')
        account_name = get_string_input(f'Please indicate name')
        account_password = get_string_input(f'Please indicate password')

        self.handler(account_number, account_name, account_password)
        print_options(self.ctrl_list)
        return get_menu_option(max_choice=len(self.ctrl_list))

    def handler(self, account_number: int, account_name: str, account_password: str):
        """
        This handles the input from the users by logging hint information and makes request to the server for
        the availability check
        :param account_password:
        :param account_name:
        :param account_number:
        :return:
        """
        print_message(f'Checking account balance...')
        try:
            balance = self.retrieve_account_balance(account_number, account_name, account_password)
            reply_string = "Account balance is: " + balance
            print_message(reply_string)
        except Exception as e:
            print_error(f"Bad Request Detected! {str(e)}")

    @staticmethod
    def retrieve_account_balance(account_number: int, account_name: str, account_password: str) -> str:
        """
        This makes request to the server for the facility availability
        :param account_number:
        :param account_name:
        :param account_password:
        :return:
        """
        reply_msg = request(ServiceType.OPEN_ACCOUNT, account_number, account_name, account_password)
        return reply_msg.data[0]

        # if facility_name == 'test error':
        #     raise Exception('Facility Is Not Included In The System!')
        # return ["00:00-13:10;14:50-21:00;21:00-23:59" for _ in chosen_days]