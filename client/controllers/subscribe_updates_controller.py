from controllers import BaseController

from communication import *


class SubscribeUpdatesController(BaseController):
    """
    This is the controller to subscribe to server events
    """

    def __init__(self):
        super().__init__()
        self.ctrl_list = ['Back to homepage', 'Subscribe again']

    @property
    def message(self):
        return '\nWanna hear about whats going on in our bank? Please provide your details:'

    @property
    def options(self):
        return None

    def execute(self) -> int:
        monitor_interval = get_int_input(f'Please indicate how long to monitor updates (in seconds)')
        self.handler(monitor_interval)
        print_options(self.ctrl_list)
        return get_menu_option(max_choice=len(self.ctrl_list))

    def handler(self, monitor_interval: int) -> None:
        """
        This takes user input and makes request to the server for subscribing, printing out the updates
        for subscription, and starts the blocking listening.
        :param monitor_interval: amount of time to receive updates for
        :return:
        """
        print_message(f'Subscribing to all bank events...')
        try:
            reply = self.request_to_subscription(monitor_interval=monitor_interval)
            print_message(f'\nYou have successfully subscribed to events!')
            print_message('If you would like to unsubscribe: Please exit the client program')
            try:
                listen(func=self.display_events, subscribe_time=monitor_interval)
            except KeyboardInterrupt:
                return
        except Exception as e:
            print_error(f"Subscription Failed: {str(e)}")

    @staticmethod
    def request_to_subscription(monitor_interval: int) -> str:
        """
        This makes request to the server to subscribe to server events for a period of time.
        :param monitor_interval: amount of time to receive updates for
        :return: reply message from server
        """
        reply_msg = request(ServiceType.SUBSCRIBE_UPDATES, str(monitor_interval))
        if reply_msg.msg_type == MessageType.EXCEPTION:
            raise Exception(reply_msg.error_msg)
        return reply_msg.data

    @classmethod
    def display_events(cls, msg: Union[ReplyMessage, ExceptionMessage]):
        """
        This is the callback method on received of the server events. It prints out the event.
        :param msg: event message received from the server
        :return:
        """
        if type(msg) is ExceptionMessage:
            print_error(f'Exception received From Server: {msg.error_msg}')
        else:
            print_message(msg.data)


