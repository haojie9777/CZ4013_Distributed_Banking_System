from typing import List


class Colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def print_options(opts: List[str]) -> None:
    """
    Print a list of options
    :param opts: list of options
    :return:
    """
    for i, opt in enumerate(opts, 1):
        print(f"{Colors.OKCYAN}{f'{i} -'}{Colors.ENDC} {opt}")


def print_message(msg: str) -> None:
    """
    Print a normal message
    :param msg: message to be printed
    :return:
    """
    print(f"{Colors.OKCYAN}{msg}{Colors.ENDC}")


def print_warning(msg: str) -> None:
    """
    Print a warning message
    :param msg: message to be printed
    :return:
    """
    print(f"{Colors.WARNING}{msg}{Colors.ENDC}")


def print_error(msg: str) -> None:
    """
    Print a error message
    :param msg: message to be printed
    :return:
    """
    print(f"{Colors.FAIL}{msg}{Colors.ENDC}")


def input_message_format(msg: str) -> str:
    """
    Add a blue '>' before the message
    :param msg: message to be printed
    :return:
    """
    return f"{Colors.OKBLUE}>{Colors.ENDC} {msg}: "


def inline_important_message_decorator(msg: str) -> str:
    """
    Highlight some keywords from white messages
    :param msg: keywords to be highlighted
    :return:
    """
    return f"{Colors.OKGREEN}{msg}{Colors.ENDC}"