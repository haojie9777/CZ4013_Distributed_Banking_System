import socket
from typing import Callable
import random
from configs import *
from utils import *


def get_port():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("", 0))
    s.listen(1)
    port = s.getsockname()[1]
    s.close()
    return port


class UDPClientSocket:
    """
    This is a UDP client that the program uses to send and listen messages
    """
    UDPSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
    UDPSocket.bind((CLIENT_IP, CLIENT_PORT if CLIENT_PORT is not None else get_port()))
    serverAddressPort = (SERVER_IP, SERVER_PORT)

    @classmethod
    def send_msg(cls, msg: bytes, request_id: str, wait_for_response: bool = True, time_out: int = 2,
                 max_attempt: int = float('inf'), buffer_size: int = 1024,
                 simulate_comm_omission_fail=False) -> Union[ReplyMessage, ExceptionMessage, None]:
        """
        This will forward a message to the server
        :param msg: message to be included in the UDP message data part
        :param request_id: ID of the request
        :param wait_for_response: True if a reply from the server is needed
        :param time_out: timeout interval for retransmitting a message
        :param max_attempt: maximum attempts for trying to get a reply
        :param buffer_size: maximum size of the message to be received
        :param simulate_comm_omission_fail: True to create intended possible omission failure
        by not sending out the request
        :return: message from the server
        """
        if wait_for_response:
            attempt = 0
            while attempt <= max_attempt:
                cls.UDPSocket.settimeout(time_out)
                attempt += 1
                try:
                    if not simulate_comm_omission_fail or\
                            simulate_comm_omission_fail and random.randint(0, 9) != 0:
                        cls.UDPSocket.sendto(msg, cls.serverAddressPort)
                    else:
                        print_warning("Simulated Request Failure")

                    while True:
                        data, addr = cls.UDPSocket.recvfrom(buffer_size)

                        if addr == cls.serverAddressPort:

                            reply_message = unmarshall(data)
                            if reply_message.request_id == request_id:
                                return reply_message
                            else:
                                print_warning('Unexpected message from server detected! Discarding...')

                        else:
                            print_warning(f'Unexpected external message from {addr} detected! Discarding...')
                except socket.timeout:
                    print_warning(msg=f'Did not receive any message from server within {time_out} seconds. Resending...')

            print_error(msg=f'Maximum {max_attempt} attempts reached. '
                            f'Please check your internet connection and try again later.')
        else:
            cls.UDPSocket.sendto(msg, cls.serverAddressPort)

    @classmethod
    def listen_msg(cls, subscribe_time: int, call_back_function: Callable, buffer_size: int = 1024) -> None:
        """
        This will listen message from the server for a certain period of time
        :param subscribe_time: time to listen in seconds
        :param call_back_function: function to execute upon receiving a valid message
        :param buffer_size: maximum size of the expected reply
        :return: 
        """
        cls.UDPSocket.settimeout(subscribe_time)

        try:
            while True:
                data, addr = cls.UDPSocket.recvfrom(buffer_size)

                if addr == cls.serverAddressPort:
                    reply_message = unmarshall(data)
                    call_back_function(reply_message)

                else:
                    print_warning(f'Unexpected message from {addr} detected! Discarding...')

        except (socket.timeout, ValueError, KeyboardInterrupt):
            print_message("\nYour subscription has expired. Thanks for listening!")
            return


if __name__ == '__main__':
    UDPClientSocket.send_msg(msg=b'test', request_id='123')
