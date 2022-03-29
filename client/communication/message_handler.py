from typing import Callable, Union

from communication import UDPClientSocket
from utils import ServiceType, RequestMessage, ReplyMessage, ExceptionMessage


def request(service: ServiceType, *args) -> Union[ReplyMessage, ExceptionMessage]:
    """
    This will send CALL request to the server and wait for a reply
    :param service: name of the service
    :param args: arguments to be passed for the service
    :return: Reply message from the server
    """
    msg = RequestMessage(service=service, data=args)
    marshalled_msg = msg.marshall()
    print(marshalled_msg)
    reply_msg = UDPClientSocket.send_msg(msg=marshalled_msg, request_id=msg.request_id)
    return reply_msg


def listen(func: Callable, subscribe_time: int):
    """
    This is block the user from input and listen for the message from server
    :param subscribe_time: time to listen in seconds
    :param func: call back functions to be executed upon receiving a valid message
    :return:
    """
    UDPClientSocket.listen_msg(call_back_function=func, subscribe_time=subscribe_time)
