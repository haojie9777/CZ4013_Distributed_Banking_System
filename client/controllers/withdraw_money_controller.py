from controllers import BaseController
from utils import *
from helpers import *


class CurrencyType(Enum):
    SGD = "SGD"
    USD = "USD"
    RMB = "RMB"


class WithdrawMoneyController(BaseController):
    """
    This is the controller to withdraw money from bank account
    """

    def __init__(self):
        super().__init__()
        self.currency_list = []
        self.ctrl_list = ['Back To Homepage', 'Other Services']
        for currency in CurrencyType:
            self.currency_list.append(currency.name)

    @property
    def message(self):
        return 'We hate to see your money leave! Please provide more details:'

    @property
    def options(self):
        return self.currency_list

    @options.setter
    def options(self, val):
        pass

    def enter(self, *args, **kwargs) -> int:
        self.show_message()
        account_name = get_string_input(f'Please indicate name')
        account_number = get_int_input(f'Please indicate account number')
        account_password = get_string_input(f'Please indicate password')
        print_options(self.options, show_number=True)
        account_currencyType_choice = get_menu_option(max_choice=len(self.currency_list),
                                                      msg='Please indicate account currency',
                                                      min_choice=0)
        account_currencyType = CurrencyType[self.currency_list[account_currencyType_choice]]
        withdraw_amount = get_float_input(f'Please indicate amount to withdraw')
        self.handler(account_name, account_number, account_password, account_currencyType, withdraw_amount)
        print_options(self.ctrl_list)
        return get_menu_option(max_choice=len(self.ctrl_list))

    def handler(self, account_name: str, account_number: int, account_password: str, account_currencyType: CurrencyType,
                withdraw_amount: float):
        """
        This handles the input from the users by logging hint information and make requests to the server
        :param withdraw_amount: amount of money to withdraw from client account
        :param account_currencyType: currency type of money
        :param account_number: account number of client
        :param account_password: account password of client
        :param account_name: account name of client
        :return:
        """
        try:
            print_message("Withdrawing money...")
            account_number = self.withdraw_money(account_name, account_number, account_password, account_currencyType,
                                                 withdraw_amount)
            print_message(msg=f'\nYour have withdrawn money from your account: {account_number}')
        except Exception as e:
            print_error(f'Withdraw money failed: {str(e)}')

    @staticmethod
    def withdraw_money(account_name: str, account_number: int, account_password: str,
                       account_currencyType: CurrencyType,
                       withdraw_amount: float) -> str:
        """
        This makes request to the server to withdraw money
        :param withdraw_amount: amount of money to withdraw from client account
        :param account_currencyType: currency type of money
        :param account_number: account number of client
        :param account_password: account password of client
        :param account_name: account name of client
        :return: reply message from server
        """
        reply_msg = request(ServiceType.WITHDRAW_MONEY, account_name, str(account_number), account_password,
                            account_currencyType.value, str(withdraw_amount))
        if reply_msg.msg_type == MessageType.EXCEPTION:
            raise Exception(reply_msg.error_msg)
        return reply_msg.data
