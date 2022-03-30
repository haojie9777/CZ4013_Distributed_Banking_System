
from controllers import BaseController
from communication import *


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
        self.ctrl_list = ['Back to homepage', 'Open another account']
        for currency in CurrencyType:
            self.currency_list.append(currency.name)

    @property
    def message(self):
        return '\nThanks for signing up with our bank! Please proceed to provide your details:'

    @property
    def options(self):
        return self.currency_list

    def execute(self) -> int:
        account_name = get_string_input(f'Please indicate name')
        account_password = get_string_input(f'Please indicate password, only input 6 characters')
        print_options(self.options)
        account_currencyType_choice = get_menu_option(max_choice=len(self.currency_list),
                                                      msg='Please indicate account currency')
        account_currencyType = CurrencyType[self.currency_list[account_currencyType_choice]]
        account_balance = get_float_input(f'Please indicate starting balance')
        self.handler(account_name, account_password, account_currencyType, account_balance)
        print_options(self.ctrl_list)
        return get_menu_option(max_choice=len(self.ctrl_list))

    def handler(self, account_name: str, account_password: str, account_currencyType: CurrencyType,
                account_balance: float):
        """
        This takes user input and makes request to the server for opening account, printing out the reply
        :param account_balance: starting balance in client account
        :param account_currencyType: currency type of client account
        :param account_password: password to set for client account
        :param account_name: name to set for client account
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
        This checks if the password is alphanumeric
        :return: boolean
        """
        return password.isalnum()

    @staticmethod
    def open_account(account_name: str, account_password: str, account_currencyType: CurrencyType,
                     account_balance: float) -> str:
        """
        This makes request to the server to book the facility
        :param account_balance: starting balance in client account
        :param account_currencyType: currency type of client account
        :param account_password: password to set for client account
        :param account_name: name to set for client account
        :return: reply message from server
        """
        reply_msg = request(ServiceType.OPEN_ACCOUNT, account_name, account_password, account_currencyType.value,
                            '%.2f' % account_balance)
        if reply_msg.msg_type == MessageType.EXCEPTION:
            raise Exception(reply_msg.error_msg)
        return reply_msg.data
