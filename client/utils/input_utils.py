from utils import input_message_format, print_warning


def get_menu_option(max_choice, msg='Please Indicate Your Choice') -> int:
    """
    Get a valid option from the menu
    :param max_choice: max possible value to be chosen
    :param msg: message to be prompted for inputting
    :return: a user chosen index
    """
    while True:
        user_input = input(input_message_format(msg))
        try:
            idx = int(user_input)
            if not (1 <= idx <= max_choice):
                raise ValueError
            return idx - 1
        except ValueError:
            print_warning("Invalid Input! Please Try Again.")


def get_string_input(msg=None) -> str:
    """
    Get an arbitrary non-empty string input
    :param msg: message to be displayed
    :return: user input string
    """
    while True:
        try:
            user_input = input(input_message_format(msg)).strip()
            if len(user_input) != 0:
                return user_input
            else:
                raise ValueError
        except ValueError:
            print_warning("Input cannot be empty! Please Try Again.")


def get_int_input(msg=None) -> int:
    """
    Get an integer within certain range
    :param msg: message to be displayed
    :param min_val: min possible value (included)
    :param max_val: max possible value (included)
    :return: user input integer
    """
    while True:
        user_input = input(input_message_format(msg))
        try:
            idx = int(user_input)
            return idx
        except:
            print_warning(f"Invalid Input! Please Try Again.")


def get_float_input(msg=None) -> float:
    """
    Get an integer within certain range
    :param msg: message to be displayed
    :return: user input integer
    """
    while True:
        user_input = input(input_message_format(msg))
        try:
            val = float(user_input)
            return val
        except:
            print_warning(f"Invalid Input! Please Try Again.")
