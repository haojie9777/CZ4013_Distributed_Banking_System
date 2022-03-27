
from controllers import BaseController
from helpers import *


class CloseAccountController(BaseController):
    """
    This is the controller to close bank account
    """

    def __init__(self):
        super().__init__()
        self.ctrl_list = ['Back To Homepage', 'Close another account']

    @property
    def message(self):
        return 'We are sad to see you go, please input your details:'

    @property
    def options(self):
        return None

    @options.setter
    def options(self, val):
        pass

    def enter(self) -> int:
        account_name = get_string_input(f'Please indicate name')
        account_number = get_int_input(f'Please indicate account number')
        account_password = get_string_input(f'Please indicate password')
        self.handler(account_name, account_number, account_password)
        print_options(self.ctrl_list)
        return get_menu_option(max_choice=len(self.ctrl_list))

    def handler(self, account_name: str, account_number: int, account_password: str):
        """
        This handles the input from the users by logging hint information and make requests to the server
        :param account_number: account number of client
        :param account_password:account password of client
        :param account_name: account name of client
        :return:
        """
        try:
            print_message("Closing account...")
            account_number = self.close_account(account_name, account_number, account_password)
            print_message(msg=f'\nYou have Successfully closed your account: {account_number}')
        except Exception as e:
            print_error(f'Open account failed: {str(e)}')

    @staticmethod
    def close_account(account_name: str, account_number: int, account_password: str) -> str:
        """
        This makes request to the server to close stated account
        :param account_number: account number of client
        :param account_password:account password of client
        :param account_name: account name of client
        :return: reply message from server
        """
        reply_msg = request(ServiceType.CLOSE_ACCOUNT, account_name, str(account_number), account_password)
        if reply_msg.msg_type == MessageType.EXCEPTION:
            raise Exception(reply_msg.error_msg)
        return reply_msg.data
