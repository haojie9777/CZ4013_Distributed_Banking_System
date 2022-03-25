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
        account_name = get_string_input(f'Please indicate name')
        account_number = get_int_input(f'Please indicate account number')
        account_password = get_string_input(f'Please indicate password')
        print_options(self.options, show_number=False)
        account_currencyType_choice = get_menu_option(max_choice=len(self.currency_list),
                                                      msg='Please indicate account currency',
                                                      min_choice=0)
        account_currencyType = CurrencyType[self.currency_list[account_currencyType_choice]]
        deposit_amount = get_float_input(f'Please indicate amount to deposit')
        self.handler(account_name, account_number, account_password, account_currencyType, deposit_amount)
        print_options(self.ctrl_list)
        return get_menu_option(max_choice=len(self.ctrl_list))

    def handler(self, account_name: str, account_number: int, account_password: str, account_currencyType: CurrencyType,
                deposit_amount: float):
        """
        This handles the input from the users by logging hint information and make requests to the server
        :param deposit_amount:
        :param account_currencyType:
        :param account_number:
        :param account_password:
        :param account_name:
        :return:
        """
        try:
            print_message("Deposting money...")
            account_number = self.deposit_money(account_name, account_number, account_password, account_currencyType, deposit_amount)
            print_message(msg=f'\nYour Have deposited money into your account: {account_number}')
        except Exception as e:
            print_error(f'Deposit money failed: {str(e)}')

    @staticmethod
    def deposit_money(account_name: str, account_number: int, account_password: str, account_currencyType: CurrencyType,
                      deposit_amount: float) -> str:
        """
        This makes request to the server to book the facility
        :param deposit_amount:
        :param account_currencyType:
        :param account_number:
        :param account_password:
        :param account_name:
        :return: 
        """
        reply_msg = request(ServiceType.DEPOSIT_MONEY, account_name, str(account_number), account_password, account_currencyType.value, str(deposit_amount))
        if reply_msg.msg_type == MessageType.EXCEPTION:
            raise Exception(reply_msg.error_msg)
        return reply_msg.data
