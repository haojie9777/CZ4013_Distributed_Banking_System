from controllers import BaseController
from communication import *


class CurrencyType(Enum):
    SGD = "SGD"
    USD = "USD"
    RMB = "RMB"


class DepositMoneyController(BaseController):
    """
    This is the controller to deposit money into account
    """

    def __init__(self):
        super().__init__()
        self.currency_list = []
        self.ctrl_list = ['Back to homepage', 'Deposit money again']
        for currency in CurrencyType:
            self.currency_list.append(currency.name)

    @property
    def message(self):
        return '\nWe welcome your money! Please provide more details:'

    @property
    def options(self):
        return self.currency_list

    def execute(self) -> int:
        account_name = get_string_input(f'Please indicate name')
        account_number = get_int_input(f'Please indicate account number')
        account_password = get_string_input(f'Please indicate password')
        print_options(self.options)
        account_currencyType_choice = get_menu_option(max_choice=len(self.currency_list),
                                                      msg='Please indicate account currency')
        account_currencyType = CurrencyType[self.currency_list[account_currencyType_choice]]
        deposit_amount = get_float_input(f'Please indicate amount to deposit')
        self.handler(account_name, account_number, account_password, account_currencyType, deposit_amount)
        print_options(self.ctrl_list)
        return get_menu_option(max_choice=len(self.ctrl_list))

    def handler(self, account_name: str, account_number: int, account_password: str, account_currencyType: CurrencyType,
                deposit_amount: float):
        """
        This takes user input and makes request to the server for depositing money, printing out the reply
        :param deposit_amount: amount to deposit into client account
        :param account_currencyType: currency type of money to deposit into client account
        :param account_number: account number of client
        :param account_password: account password of client
        :param account_name: account name of client
        :return:
        """
        try:
            print_message("Depositing money...")
            current_balance = self.deposit_money(account_name, account_number, account_password, account_currencyType, deposit_amount)
            print_message(msg=f'\nYou have successfully deposited, your new balance is: ${current_balance}')
        except Exception as e:
            print_error(f'Deposit money failed: {str(e)}')

    @staticmethod
    def deposit_money(account_name: str, account_number: int, account_password: str, account_currencyType: CurrencyType,
                      deposit_amount: float) -> str:
        """
        This makes request to the server to deposit money into stated account
        :param deposit_amount: amount to deposit into client account
        :param account_currencyType: currency type of money to deposit into client account
        :param account_number: account number of client
        :param account_password: account password of client
        :param account_name: account name of client
        :return: reply message from server
        """
        reply_msg = request(ServiceType.DEPOSIT_MONEY, account_name, str(account_number), account_password, account_currencyType.value, '%.2f' % deposit_amount)
        if reply_msg.msg_type == MessageType.EXCEPTION:
            raise Exception(reply_msg.error_msg)
        return reply_msg.data
