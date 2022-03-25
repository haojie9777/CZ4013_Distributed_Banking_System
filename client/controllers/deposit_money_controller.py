from controllers import BaseController
from utils import *
from helpers import *


class CurrencyType(Enum):
    SGD = "SGD"
    USD = "USD"
    RMB = "RMB"


class DepositMoneyController(BaseController):
    """
    This is the controller to open bank account
    """

    def __init__(self):
        super().__init__()
        self.currency_list = []
        self.ctrl_list = ['Back To Homepage', 'Make Another Booking']
        for currency in CurrencyType:
            self.currency_list.append(currency.name)

    @property
    def message(self):
        return 'We welcome your money! Please provide more details:'

    @property
    def options(self):
        return self.currency_list

    @options.setter
    def options(self, val):
        pass

    def enter(self, *args, **kwargs) -> int:
        self.show_message()
        account_number = get_int_input(f'Please indicate account number')
        account_name = get_string_input(f'Please indicate name')
        account_password = get_string_input(f'Please indicate password')
        print_options(self.options, show_number=False)
        account_currencyType_choice = get_menu_option(max_choice=len(self.currency_list),
                                                      msg='Please indicate account currency',
                                                      min_choice=0)
        account_currencyType = CurrencyType[self.currency_list[account_currencyType_choice]]
        self.handler(account_number, account_name, account_password)
        print_options(self.ctrl_list)
        return get_menu_option(max_choice=len(self.ctrl_list))

    def handler(self, account_number: int, account_name: str, account_password: str):
        """
        This handles the input from the users by logging hint information and make requests to the server
        :param account_number: 
        :param account_password:
        :param account_name:
        :return:
        """
        try:
            print_message("Closing account...")
            account_number = self.close_account(account_number, account_name, account_password)
            print_message(msg=f'\nYour Have Successfully closed your account: {account_number}')
        except Exception as e:
            print_error(f'Open account failed: {str(e)}')

    @staticmethod
    def close_account(account_number: int, account_name: str, account_password: str) -> str:
        """
        This makes request to the server to book the facility
        :param account_number: 
        :param account_password:
        :param account_name:
        :return: 
        """
        reply_msg = request(ServiceType.OPEN_ACCOUNT, account_number, account_name, account_password)
        if reply_msg.msg_type == MessageType.EXCEPTION:
            raise Exception(reply_msg.error_msg)
        return reply_msg.data[0]
