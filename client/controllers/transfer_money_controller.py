from controllers import BaseController
from utils import *
from helpers import *


class CurrencyType(Enum):
    SGD = "SGD"
    USD = "USD"
    RMB = "RMB"


class TransferMoneyController(BaseController):
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
        return 'Making sure you money goes to your recipient! Please provide more details:'

    @property
    def options(self):
        return self.currency_list

    @options.setter
    def options(self, val):
        pass

    def enter(self, *args, **kwargs) -> int:
        self.show_message()
        account_name = get_string_input(f'Please indicate your name')
        account_number = get_int_input(f'Please indicate account number')
        account_password = get_string_input(f'Please indicate password')
        print_options(self.options, show_number=False)
        account_currencyType_choice = get_menu_option(max_choice=len(self.currency_list),
                                                      msg='Please indicate account currency',
                                                      min_choice=0)
        account_currencyType = CurrencyType[self.currency_list[account_currencyType_choice]]
        transfer_amount = get_float_input(f'Please indicate amount to withdraw')
        payee_account_name = get_string_input(f'Please indicate payee name')
        payee_account_number = get_int_input(f'Please indicate payee account number')
        self.handler(account_name, account_number, account_password, account_currencyType, transfer_amount, payee_account_name, payee_account_number)
        print_options(self.ctrl_list)
        return get_menu_option(max_choice=len(self.ctrl_list))

    def handler(self, account_name: str, account_number: int, account_password: str, account_currencyType: CurrencyType,
                transfer_amount: float, payee_account_name: str, payee_account_number: int):
        """
        This handles the input from the users by logging hint information and make requests to the server
        :param payee_account_number:
        :param payee_account_name:
        :param transfer_amount:
        :param account_currencyType:
        :param account_number:
        :param account_password:
        :param account_name:
        :return:
        """
        try:
            print_message("Withdrawing money...")
            account_number = self.withdraw_money(account_name, account_number, account_password, account_currencyType,
                                                 transfer_amount, payee_account_name, payee_account_number)
            print_message(msg=f'\nYour Have withdrawn money from your account: {account_number}')
        except Exception as e:
            print_error(f'Withdraw money failed: {str(e)}')

    @staticmethod
    def withdraw_money(account_name: str, account_number: int, account_password: str,
                       account_currencyType: CurrencyType,
                       transfer_amount: float, payee_account_name: str, payee_account_number: int) -> str:
        """
        This makes request to the server to book the facility
        :param transfer_amount:
        :param payee_account_number:
        :param payee_account_name:
        :param account_currencyType:
        :param account_number:
        :param account_password:
        :param account_name:
        :return: 
        """
        reply_msg = request(ServiceType.WITHDRAW_MONEY, account_name, str(account_number), account_password,
                            account_currencyType.value, str(transfer_amount), payee_account_name, str(payee_account_number))
        if reply_msg.msg_type == MessageType.EXCEPTION:
            raise Exception(reply_msg.error_msg)
        return reply_msg.data[0]
