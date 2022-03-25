from controllers import BaseController
from utils import *
from helpers import *


class SubscribeUpdatesController(BaseController):
    """
    This is the controller to open bank account
    """

    def __init__(self):
        super().__init__()
        self.ctrl_list = ['Back To Homepage', 'Other Services']

    @property
    def message(self):
        return 'Wanna hear about whats going on in our bank? Please provide your details:'

    @property
    def options(self):
        return None

    @options.setter
    def options(self, val):
        pass

    def enter(self, *args, **kwargs) -> int:
        self.show_message()
        account_name = get_string_input(f'Please indicate name')
        account_number = get_int_input(f'Please indicate account number')
        account_password = get_string_input(f'Please indicate password')
        monitor_interval = get_int_input(f'Please indicate how long to monitor updates (in seconds)')
        self.handler(account_name, account_number, account_password, monitor_interval)
        print_options(self.ctrl_list)
        return get_menu_option(max_choice=len(self.ctrl_list))

    def handler(self, account_name: str, account_number: int, account_password: str, monitor_interval:int) -> None:
        """
        This handles the input from the users by logging hint information, make requests to the server
        for subscription, and starts the blocking listening.
        :param monitor_interval:
        :param account_password:
        :param account_number:
        :param account_name:
        :return:
        """
        print_message(f'Subscribing to all bank events...')
        try:
            subscription_id = self.request_to_subscrption(account_name, account_number, account_password, monitor_interval=monitor_interval)
            print_message(f'\nYou Have Just Successfully Subscribed to events!')
            print_message(f'If You Would Like To Unsubscribe: Press {inline_important_message_decorator("Ctrl + C")} ')
            try:
                listen(func=self.display_events, subscribe_time=monitor_interval,
                       subscription_id=subscription_id)
            except KeyboardInterrupt:
                return
        except Exception as e:
            print_error(f"Subscription Failed: {str(e)}")

    @staticmethod
    def request_to_subscrption(account_name: str, account_number: int, account_password: str, monitor_interval:int) -> str:
        """
        This makes request to the server to subscribe for the availability for a period of time.
        :param monitor_interval:
        :param account_password:
        :param account_number:
        :param account_name:
        :return: subscription id
        """
        reply_msg = request(ServiceType.SUBSCRIBE_UPDATES, account_name, str(account_number), account_password, str(monitor_interval))
        if reply_msg.msg_type == MessageType.EXCEPTION:
            raise Exception(reply_msg.error_msg)
        return reply_msg.data[0]

    @classmethod
    def display_events(cls, msg: Union[CallMessage, OneWayMessage, ExceptionMessage]):
        """
        This is the callback method on received of the server posted availability update. It prints out the time table
        and sends ACK to the server
        :param msg: message received from the server
        :return:
        """
        if type(msg) is ExceptionMessage:
            print_error(f'Exception Received From Server: {msg.error_msg}')
        else:
            prompt_message_decorator(msg.data[0])

        notify(service=ServiceType.SUBSCRIBE_UPDATES, request_id=msg.request_id)

