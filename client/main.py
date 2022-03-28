from controllers import MainPageController

from utils import print_message

if __name__ == '__main__':
    """
    Entrance of the Program
    """
    try:
        MainPageController().start()
    except KeyboardInterrupt:
        print_message(msg='\nShutting Down...')
        print_message(msg='Thank you for using our banking system.')
