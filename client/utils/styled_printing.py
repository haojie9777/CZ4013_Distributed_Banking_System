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


class SpecialCharacters:
    DOT = '\u2022'


def print_options(opts: List[str], show_number: bool = True, new_line_at_end: bool = False) -> None:
    """
    Print a list of options to console
    :param opts: list of options
    :param show_number: use number as prefix when printing options
    :param new_line_at_end: print a new line at the end of options
    :return:
    """
    for i, opt in enumerate(opts, 1):
        print(f"{Colors.OKCYAN}{f'{i} -' if show_number else SpecialCharacters.DOT}{Colors.ENDC} {opt}")
    if new_line_at_end:
        print()


def print_message(msg: str) -> None:
    """
    Print a normal message
    :param msg: message to be printed
    :return:
    """
    print(f"{Colors.OKBLUE}{msg}{Colors.ENDC}")


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


def prompt_message_decorator(msg: str) -> str:
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


def print_timetable(days: List[str], avail_by_days: List[str],
                    new_line_at_top: bool = True, new_line_at_end: bool = True,
                    facility_name: str = None) -> None:
    """
    Print a timetable
    :param days: days in sequence
    :param avail_by_days: facility availability by days
    :param new_line_at_top: extra new line before printing the timetable
    :param new_line_at_end: extra new line after printing the timetable
    :param facility_name: name of the facilities/facility
    :return:
    """
    assert len(days) == len(avail_by_days)
    if new_line_at_top:
        print()
    if facility_name is not None:
        print_message(f'Available Periods of {facility_name} on the Queried Days')
    max_len_str = max(days, key=len)
    content = []
    for i, v in enumerate(days):
        content.append(f'{v + " " * (len(max_len_str) - len(v))}: '
                       f'{" | ".join(avail_by_days[i].split(";")) if len(avail_by_days[i]) > 0 else "No Available Slots"}')
    print_options(content, show_number=False)
    if new_line_at_end:
        print()

