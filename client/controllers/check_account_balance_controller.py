from datetime import datetime

from controllers import BaseController
from utils import *
from helpers import *


class CheckAccountBalanceController(BaseController):
    """
    This is the controller used to check account balance
    """

    def __init__(self):
        super().__init__()
        self.ctrl_list = ['Back To Homepage', 'Other Services']

    @property
    def message(self):
        return None

    @property
    def options(self):
        return None

    def enter(self, *args, **kwargs) -> int:
        account_name = get_string_input(f'Please indicate name')
        account_number = get_int_input(f'Please indicate account number')
        account_password = get_string_input(f'Please indicate password')

        self.handler(account_name, account_number, account_password)
        print_options(self.ctrl_list)
        return get_menu_option(max_choice=len(self.ctrl_list))

    def handler(self, account_name: str, account_number: int, account_password: str):
        """
        This handles the input from the users by logging hint information and makes request to the server for
        the checking account balance
        :param account_number: account number of client
        :param account_name: account name of client
        :param account_password: account password of client
        :return:
        """
        print_message(f'Checking account balance...')
        try:
            balance = self.retrieve_account_balance(account_name, account_number, account_password)
            reply_string = "Account balance is: " + balance
            print_message(reply_string)
        except Exception as e:
            print_error(f"Bad Request Detected! {str(e)}")

    @staticmethod
    def retrieve_account_balance(account_name: str, account_number: int, account_password: str) -> str:
        """
        This makes request to the server for checking account balance
        :param account_number: account number of client
        :param account_name: account name of client
        :param account_password: account password of client
        :return: reply message from server
        """
        reply_msg = request(ServiceType.OPEN_ACCOUNT, account_name, str(account_number), account_password)
        return reply_msg.data

        # if facility_name == 'test error':
        #     raise Exception('Facility Is Not Included In The System!')
        # return ["00:00-13:10;14:50-21:00;21:00-23:59" for _ in chosen_days]
