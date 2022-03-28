from enum import Enum
from typing import Tuple, Union
import struct
from uuid import uuid4 as uuid


class MessageType(Enum):
    REQUEST = "REQUEST"
    REPLY = "REPLY"
    ACK = "ACK"
    EXCEPTION = "EXCEPTION"


class ServiceType(Enum):
    OPEN_ACCOUNT = '0'
    CLOSE_ACCOUNT = '1'
    DEPOSIT_MONEY = '2'
    WITHDRAW_MONEY = '3'
    SUBSCRIBE_UPDATES = '4'
    CHECK_BALANCE = '5'
    TRANSFER_MONEY = '6'


type_to_hex = dict({
    int: b'\x00',
    float: b'\x01',
    str: b'\x02',
    bool: b'\x03',
    list: b'\x04'
})


class BaseMessage:
    """
    Super class for all kinds of messages expected from the server
    """

    def __init__(self, request_id: str):
        self.request_id = request_id


class RequestMessage(BaseMessage):
    """
    UDP message of type Request
    """

    def __init__(self, service: ServiceType, data: Tuple):
        super().__init__(str(uuid()))
        self.service = service
        self.data = data

    def marshall(self) -> bytearray:
        """
        Marshall the data part of the message
        :return: marshalled data in bytes
        """
        msg_in_bytes = bytearray(self.service.value.encode('ascii'))
        # msg_in_bytes += struct.pack('B', len(self.service.value))
        msg_in_bytes += bytes("|".encode('ascii')) + bytes(self.request_id.encode('ascii')) + bytes("|".encode('ascii'))
        for a in self.data:
            msg_in_bytes += bytes(a.encode('ascii')) + bytes("|".encode('ascii'))
        return msg_in_bytes


class ReplyMessage(BaseMessage):
    """
    UDP message of type REPLY
    """

    def __init__(self, request_id: str, data: str):
        super().__init__(request_id)
        self.msg_type = MessageType.REPLY
        self.data = data


class ExceptionMessage(BaseMessage):
    """
    UDP message of type EXCEPTION
    """

    def __init__(self, request_id: str, error_msg: str):
        super().__init__(request_id)
        self.msg_type = MessageType.EXCEPTION
        self.error_msg = error_msg


class AckMessage(ReplyMessage):
    """
    UDP message of type ACK (a.k.a NOTIFY)
    """

    def __init__(self, service: ServiceType, request_id: str, data: list):
        super().__init__(request_id, data)
        self.msg_type = MessageType.ACK
        self.service = service

    def marshall(self) -> bytearray:
        msg_in_bytes = bytearray(self.service.value.encode('ascii'))
        # msg_in_bytes += struct.pack('B', len(self.service.value))
        msg_in_bytes += bytes("|".encode('ascii')) + bytes(self.request_id.encode('ascii'))
        return msg_in_bytes


def unmarshall(data: bytes) -> Union[ReplyMessage, AckMessage, ExceptionMessage]:
    """
    Unmarshall a message in bytes to one of the predefined UDP mesage types
    :param data: raw data in bytes
    :return: A UDP message of type REPLY or EXCEPTION
    """
    decoded_data = data.decode('ascii')
    decoded_data_list = decoded_data.split('|')
    print(decoded_data_list)
    request_id = decoded_data_list[0]
    print(request_id)
    message_status = decoded_data_list[1]
    print(message_status)
    if message_status == '0':
        error_message = decoded_data_list[2]
        return ExceptionMessage(request_id=request_id, error_msg=error_message)
    elif message_status == '1':
        return ReplyMessage(request_id=request_id, data=decoded_data_list[2])
    else:
        raise TypeError(f"Unexpected Message Of Type {message_status} Received!")


if __name__ == '__main__':
    msg = RequestMessage(service=ServiceType.FACILITY_AVAIL_CHECKING, data=('North Hill Gym', ['Sun', 'Coming Mon']))
    bytes_msg = msg.marshall()
    from communication import UDPClientSocket

    UDPClientSocket.send_msg(msg=bytes_msg, request_id=msg.request_id)
