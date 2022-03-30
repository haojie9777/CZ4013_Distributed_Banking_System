from enum import Enum
from typing import Tuple, Union
from uuid import uuid4 as uuid


class MessageType(Enum):
    REQUEST = "REQUEST"
    REPLY = "REPLY"
    EXCEPTION = "EXCEPTION"


class ServiceType(Enum):
    OPEN_ACCOUNT = '0'
    CLOSE_ACCOUNT = '1'
    DEPOSIT_MONEY = '2'
    WITHDRAW_MONEY = '3'
    SUBSCRIBE_UPDATES = '4'
    TRANSFER_MONEY = '5'
    CHECK_BALANCE = '6'


class BaseMessage:
    """
    Super class for all messages expected from the server
    """

    def __init__(self, request_id: str):
        self.request_id = request_id


class RequestMessage(BaseMessage):
    """
    UDP message of type REQUEST
    """

    def __init__(self, service: ServiceType, data: Tuple):
        super().__init__(str(uuid()))
        self.msg_type = MessageType.REQUEST
        self.service = service
        self.data = data

    def marshall(self) -> bytearray:
        """
        Marshall the data part of the message
        :return: marshalled data in bytes
        """
        msg_in_bytes = bytearray(self.service.value.encode('ascii'))
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


def unmarshall(data: bytes) -> Union[ReplyMessage, ExceptionMessage]:
    """
    Unmarshall a message in bytes to one of the predefined UDP message types
    :param data: raw data in bytes
    :return: A UDP message of type REPLY or EXCEPTION
    """
    decoded_data = data.decode('ascii')
    decoded_data_list = decoded_data.split('|')
    request_id = decoded_data_list[0]
    message_status = decoded_data_list[1]
    if message_status == '0':
        return ExceptionMessage(request_id=request_id, error_msg=decoded_data_list[2])
    elif message_status == '1':
        return ReplyMessage(request_id=request_id, data=decoded_data_list[2])
    else:
        raise Exception(f"Unexpected Message Of Type {message_status} Received!")
