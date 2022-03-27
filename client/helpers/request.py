from typing import Callable, Union

from helpers import UDPClientSocket
from utils import ServiceType, CallMessage, ReplyMessage, OneWayMessage, ExceptionMessage


def request(service: ServiceType, *args, **kwargs) -> Union[ReplyMessage, OneWayMessage, ExceptionMessage]:
    """
    This will send CALL request to the server and wait for a reply
    :param service: name of the service
    :param args: arguments to be passed for the service
    :param kwargs:
    :return: Reply message from the server
    """
    msg = CallMessage(service=service, data=args)
    marshalled_msg = msg.marshall()
    # marshalled_msg = struct.pack('<I', create_validation_code(marshalled_msg)) + marshalled_msg
    print(marshalled_msg)
    reply_msg = UDPClientSocket.send_msg(msg=marshalled_msg, request_id=msg.request_id, **kwargs)
    return reply_msg


def notify(service: ServiceType, request_id: str, *args, **kwargs):
    """
    This will send an ONEWAY message to the server and do not wait for any reply
    :param service: name of the service
    :param request_id: ID of the request
    :param args: arguments to be passed for the service
    :param kwargs:
    :return:
    """
    msg = OneWayMessage(service=service, request_id=request_id, data=args)
    marshalled_msg = msg.marshall()
    # marshalled_msg = struct.pack('<I', create_validation_code(marshalled_msg)) + marshalled_msg
    print(marshalled_msg)
    UDPClientSocket.send_msg(msg=marshalled_msg, request_id=msg.request_id, wait_for_response=False, **kwargs)


def listen(func: Callable, **kwargs):
    """
    This is block the user from input and listen for the message from server
    :param func: call back functions to be executed upon receiving a valid message
    :param kwargs:
    :return:
    """
    UDPClientSocket.listen_msg(call_back_function=func, **kwargs)
