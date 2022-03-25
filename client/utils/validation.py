import zlib


def create_validation_code(payload: bytes) -> int:
    """
    Hash the payload using Adler32
    :param payload: bytes to be hashed
    :return: hashed result
    """
    return zlib.adler32(payload)


def verify_validation_code(stated_validation_code: int, payload: bytes) -> bool:
    """
    Check if the validation code (CheckSum) is correct
    :param stated_validation_code: stated hashed result
    :param payload: bytes to be hashed
    :return: True if the stated validation code is correct
    """
    return stated_validation_code == zlib.adler32(payload)
