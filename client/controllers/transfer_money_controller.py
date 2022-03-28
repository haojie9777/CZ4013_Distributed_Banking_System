from controllers import BaseController

from communication import *


class CurrencyType(Enum):
    SGD = "SGD"
    USD = "USD"
    RMB = "RMB"


class TransferMoneyController(BaseController):
    """
    This is the controller to transfer money between bank accounts
    """

    def __init__(self):
        super().__init__()
        self.currency_list = []
        self.ctrl_list = ['Back to homepage', 'Transfer Money to another account']
        for currency in CurrencyType:
            self.currency_list.append(currency.name)

    @property
    def message(self):
        return 'Making sure you money goes to your recipient! Please provide more details:'

    @property
    def options(self):
        return self.currency_list

    def execute(self) -> int:
        account_name = get_string_input(f'Please indicate your name')
        account_number = get_int_input(f'Please indicate account number')
        account_password = get_string_input(f'Please indicate password')
        print_options(self.options, show_number=True)
        account_currencyType_choice = get_menu_option(max_choice=len(self.currency_list),
                                                      msg='Please indicate account currency')
        account_currencyType = CurrencyType[self.currency_list[account_currencyType_choice]]
        transfer_amount = get_float_input(f'Please indicate amount to withdraw')
        payee_account_name = get_string_input(f'Please indicate payee name')
        payee_account_number = get_int_input(f'Please indicate payee account number')
        self.handler(account_name, account_number, account_password, account_currencyType, transfer_amount,
                     payee_account_name, payee_account_number)
        print_options(self.ctrl_list)
        return get_menu_option(max_choice=len(self.ctrl_list))

    def handler(self, account_name: str, account_number: int, account_password: str, account_currencyType: CurrencyType,
                transfer_amount: float, payee_account_name: str, payee_account_number: int):
        """
        This handles the input from the client by logging hint information and make requests to the server
        :param transfer_amount: float amount to transfer to payee
        :param payee_account_number: account number of payee
        :param payee_account_name: account name of payee
        :param account_currencyType: currency type to transfer
        :param account_number: account number of payer
        :param account_password: account password of payer
        :param account_name: account name of payer
        :return:
        """
        try:
            print_message("Transferring money...")
            reply = self.transfer_money(account_name, account_number, account_password, account_currencyType,
                                        transfer_amount, payee_account_name, payee_account_number)
            print_message(msg=f'\nYour have transferred money from your account: {reply}')
        except Exception as e:
            print_error(f'Transfer money failed: {str(e)}')

    @staticmethod
    def transfer_money(account_name: str, account_number: int, account_password: str,
                       account_currencyType: CurrencyType,
                       transfer_amount: float, payee_account_name: str, payee_account_number: int) -> str:
        """
        This makes request to the server to transfer money
        :param transfer_amount: float amount to transfer to payee
        :param payee_account_number: account number of payee
        :param payee_account_name: account name of payee
        :param account_currencyType: currency type to transfer
        :param account_number: account number of payer
        :param account_password: account password of payer
        :param account_name: account name of payer
        :return: reply message from server
        """
        reply_msg = request(ServiceType.WITHDRAW_MONEY, account_name, str(account_number), account_password,
                            account_currencyType.value, '%.2f' % transfer_amount, payee_account_name,
                            str(payee_account_number))
        if reply_msg.msg_type == MessageType.EXCEPTION:
            raise Exception(reply_msg.error_msg)
        return reply_msg.data
