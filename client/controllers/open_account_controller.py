from datetime import datetime

from controllers import BaseController
from utils import *
from helpers import *


class CurrencyType(Enum):
    SGD = "SGD"
    USD = "USD"
    RMB = "RMB"


class OpenAccountController(BaseController):
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
        return 'Thanks for signing up with our bank! Please proceed to provide your details:'

    @property
    def options(self):
        return self.currency_list

    @options.setter
    def options(self, val):
        pass

    def enter(self, *args, **kwargs) -> int:
        self.show_message()
        account_name = get_string_input(f'Please indicate name')
        account_password = get_string_input(f'Please indicate password, only input 6 characters')
        print_options(self.options, show_number=False)
        account_currencyType_choice = get_menu_option(max_choice=len(self.currency_list),
                                                      msg='Please indicate account currency',
                                                      min_choice=0)
        account_currencyType = CurrencyType[self.currency_list[account_currencyType_choice]]
        account_balance = get_float_input(f'Please indicate starting balance')
        self.handler(account_name, account_password, account_currencyType, account_balance)
        print_options(self.ctrl_list)
        return get_menu_option(max_choice=len(self.ctrl_list))

    def handler(self, account_name: str, account_password: str, account_currencyType: CurrencyType,
                account_balance: float):
        """
        This handles the input from the users by logging hint information and make requests to the server
        :param account_balance:
        :param account_password:
        :param account_name:
        :param account_currencyType:
        :return:
        """
        try:
            if not self._check_password_isalnum(account_password) or len(account_password) != 6:
                raise Exception('Password can only be alphanumeric characters, password must have 6 characters!')
            print_message("Opening account...")
            account_number = self.open_account(account_name, account_password, account_currencyType, account_balance)
            print_message(msg=f'\nYou have successfully opened an account: {account_number}')
        except Exception as e:
            print_error(f'Open account failed: {str(e)}')

    def _check_password_isalnum(self, password: str) -> bool:
        """
        This checks if the starting time and ending time are valid
        :return:
        """
        return password.isalnum()

    @staticmethod
    def open_account(account_name: str, account_password: str, account_currencyType: CurrencyType,
                     account_balance: float) -> str:
        """
        This makes request to the server to book the facility
        :param account_balance:
        :param account_currencyType:
        :param account_password:
        :param account_name:
        :return: an unique booking ID
        """
        reply_msg = request(ServiceType.OPEN_ACCOUNT, account_name, account_password, account_currencyType.value,
                            str(account_balance))
        if reply_msg.msg_type == MessageType.EXCEPTION:
            raise Exception(reply_msg.error_msg)
        return reply_msg.data
