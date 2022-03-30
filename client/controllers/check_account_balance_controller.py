from controllers import BaseController
from communication import *


class CheckAccountBalanceController(BaseController):
    """
    This is the controller used to check account balance
    """

    def __init__(self):
        super().__init__()
        self.ctrl_list = ['Back to homepage', 'Check balance again']

    @property
    def message(self):
        return 'Lets take a look at your balance:'

    @property
    def options(self):
        return None

    def execute(self) -> int:
        account_name = get_string_input(f'Please indicate name')
        account_number = get_int_input(f'Please indicate account number')
        account_password = get_string_input(f'Please indicate password')
        self.handler(account_name, account_number, account_password)
        print_options(self.ctrl_list)
        return get_menu_option(max_choice=len(self.ctrl_list))

    def handler(self, account_name: str, account_number: int, account_password: str):
        """
        This takes user input and makes request to the server for checking account balance, printing out the reply
        :param account_number: account number of client
        :param account_name: account name of client
        :param account_password: account password of client
        :return:
        """
        print_message(f'Checking account balance...')
        try:
            current_balance = self.retrieve_account_balance(account_name, account_number, account_password)
            print_message(msg=f'\nYour current balance is: {current_balance}')
        except Exception as e:
            print_error(f"Bad request detected! {str(e)}")

    @staticmethod
    def retrieve_account_balance(account_name: str, account_number: int, account_password: str) -> str:
        """
        This makes request to the server for checking account balance
        :param account_number: account number of client
        :param account_name: account name of client
        :param account_password: account password of client
        :return: reply message from server
        """
        reply_msg = request(ServiceType.CHECK_BALANCE, account_name, str(account_number), account_password)
        if reply_msg.msg_type == MessageType.EXCEPTION:
            raise Exception(reply_msg.error_msg)
        return reply_msg.data
