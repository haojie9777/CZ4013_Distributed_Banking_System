from enum import Enum
from typing import Tuple, Union
import struct
from uuid import uuid4 as uuid



class ServiceType(Enum):
    OPEN_ACCOUNT = '0'
    CLOSE_ACCOUNT = '1'
    SUBSCRIBE_UPDATES = '2'
    DEPOSIT_MONEY = '3'
    WITHDRAW_MONEY = '4'
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


class CallMessage(BaseMessage):
    """
    UDP message of type CALL
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

    @classmethod
    def _serialize_data(cls, a) -> bytes:
        # Currently unused would normally be called in line 54
        """
        Marshall a field of data to bytes
        :param a: data to be serialized
        :return: serialized data in bytes
        """
        type_a = str
        serialized_form = type_to_hex[type_a]

        if type_a is int:
            serialized_form += struct.pack('<i', a)
        elif type_a is float:
            serialized_form += struct.pack('<f', a)
        elif type_a is bool:
            serialized_form += struct.pack('<b', a)
        elif type_a is str:
            serialized_form += bytes(a.encode('ascii'))
        elif type_a is list:
            inner_type = type(a[0])
            serialized_inner_data = bytearray()
            for inner_a in a:
                serialized_inner_data += cls._serialize_data(inner_a)[1:]  # type is not needed
            serialized_form += type_to_hex[inner_type] + struct.pack('<i', len(a)) + serialized_inner_data

        return serialized_form


class ReplyMessage(BaseMessage):
    """
    UDP message of type REPLY
    """
    def __init__(self, request_id: str, data: list):
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


class OneWayMessage(ReplyMessage):
    """
    UDP message of type ONEWAR (a.k.a NOTIFY)
    """
    def __init__(self, service: ServiceType, request_id: str, data: list):
        super().__init__(request_id, data)
        self.msg_type = MessageType.ONEWAY
        self.service = service

    def marshall(self) -> bytearray:
        msg_in_bytes = bytearray(self.msg_type.value)
        msg_in_bytes += bytes(self.request_id.encode('ascii'))
        msg_in_bytes += struct.pack('B', len(self.service.value))
        msg_in_bytes += bytes(self.service.value.encode('ascii'))
        return msg_in_bytes


def unmarshall(data: bytes) -> Union[ReplyMessage, OneWayMessage, ExceptionMessage]:
    """
    Unmarshall a message in bytes to one of the predefined UDP mesage types
    :param data: raw data in bytes
    :return: A UDP message of type REPLY, ONEWAY or EXCEPTION
    """
    ptr = 0
    request_id = data[ptr:ptr + 36].decode('ascii')
    ptr += 36
    message_status = data[ptr]
    ptr += 1
    if msg_type_id == 3:
        error_message = data[ptr+5:].decode('ascii')
        return ExceptionMessage(request_id=request_id, error_msg=error_message)
    elif msg_type_id == 1:
        return ReplyMessage(request_id=request_id, data=parse_data(data, ptr))
    elif msg_type_id == 2:
        return OneWayMessage(request_id=request_id, data=parse_data(data, ptr))
    else:
        raise TypeError('Unexpected Message Of Type CALL Received!')


def parse_data(data: bytes, ptr: int) -> list:
    """
    Method used to unmarshall the Argument part from bytes by forwarding pointers
    :param data: raw data in bytes
    :param ptr: starting position of the Argument part
    :return:
    """
    parsed_data = []
    while ptr <= len(data) - 2:
        data_type = data[ptr]
        ptr += 1
        if data_type == 4:  # TODO nested lists are not supported
            inner_type = data[ptr]
            ptr += 1
            length, ptr_shift = _parse_data_with_type(data, ptr, 0)
            ptr += ptr_shift
            list_data = []
            for i in range(length):
                parsed_field, ptr_shift = _parse_data_with_type(data, ptr, inner_type)
                list_data.append(parsed_field)
                ptr += ptr_shift
            parsed_data.append(list_data)
        else:
            parsed_field, ptr_shift = _parse_data_with_type(data, ptr, data_type)
            parsed_data.append(parsed_field)
            ptr += ptr_shift
    return parsed_data


def _parse_data_with_type(data, ptr, data_type):
    """
    Method used to parse one data field
    :param data: raw data in bytes
    :param ptr: current position of the pointer
    :param data_type: type of the data to be unmarshalled
    :return: unmarshalled data and pointer shift
    """
    if data_type == 0:
        return struct.unpack('<i', data[ptr:ptr + 4])[0], 4
    elif data_type == 1:
        return struct.unpack('<f', data[ptr:ptr + 4])[0], 4
    elif data_type == 2:
        length = struct.unpack('<i', data[ptr:ptr + 4])[0]
        return data[ptr + 4:ptr + 4 + length].decode('ascii'), 4 + length
    elif data_type == 3:
        return struct.unpack('<b', data[ptr:ptr + 1]), 1


if __name__ == '__main__':
    msg = CallMessage(service=ServiceType.FACILITY_AVAIL_CHECKING, data=('North Hill Gym', ['Sun', 'Coming Mon']))
    bytes_msg = msg.marshall()
    from helpers import UDPClientSocket
    UDPClientSocket.send_msg(msg=bytes_msg, request_id=msg.request_id)
