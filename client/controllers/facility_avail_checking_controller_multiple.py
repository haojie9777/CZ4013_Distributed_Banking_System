from datetime import datetime

from controllers import BaseController
from utils import *
from helpers import *


class FacilityAvailCheckingControllerMultiple(BaseController):
    """
    This is the controller used to check mutual available slots of multiple facilities on particular days
    """
    day_list = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

    def __init__(self, facility_name_list):
        super().__init__()
        self._options = facility_name_list
        self.ctrl_list = ['Back To Homepage', 'Make Another Query']

    @property
    def message(self):
        return 'All Facilities Are Listed Below For Your Reference:'

    @property
    def options(self):
        return self._options

    @options.setter
    def options(self, val):
        pass

    def enter(self, *args, **kwargs) -> int:
        self.show_message()
        print_options(self.options, show_number=False)
        facility_name = get_string_input(f'Please Indicate the Target Facility by Typing '
                                         f'{inline_important_message_decorator("Full Name")} '
                                         f'Separated By {inline_important_message_decorator("Comma")}'
                                         )
        facility_name_list = facility_name.strip().split(',')
        current_day = datetime.today().weekday()
        day_list = self.day_list[current_day:] + [f'Coming {d}' for d in self.day_list[:current_day]]
        print_options(day_list, show_number=False)
        chosed_days = get_string_options(list_of_vals=day_list, msg='Please Indicate Day(s) to Check')
        self.handler(facility_name_list, chosed_days)
        print_options(self.ctrl_list)
        return get_menu_option(max_choice=len(self.ctrl_list))

    def handler(self, facility_name: List[str], chosen_days: List[str]):
        """
        This handles the input from the users by logging hint information and make requests to the server
        :param facility_name: name of the chosen facility
        :param chosen_days: chosen days as list of strings
        :return:
        """
        if len(chosen_days) == 1:
            displayed_days = chosen_days[0]
        else:
            displayed_days = f'{",".join(chosen_days[:-1])} and {chosen_days[-1]}'
        print_message(f'Checking the Concurrent Availability of {facility_name} on {displayed_days}...')
        try:
            avail_by_days = self.retrieve_facility_avail_by_days(facility_name, chosen_days)
            print_timetable(facility_name=facility_name,
                            days=chosen_days,
                            avail_by_days=avail_by_days)
        except Exception as e:
            print_error(f"Bad Request Detected! {str(e)}")

    @staticmethod
    def retrieve_facility_avail_by_days(facility_name: List[str], chosen_days: List[str]) -> List[str]:
        """
        This makes request to the server for the mutual facility availability
        :param facility_name: name of the chosen facilities
        :param chosen_days: chosen days as list of strings
        :return: the corresponding mutual available slots of the facilities by days in sequence
        """
        facility_name_striped = []
        for i in facility_name:
            facility_name_striped.append(i.strip())

        reply_msg = request(ServiceType.FACILITY_AVAIL_CHECKING_MULTIPLE, facility_name_striped, chosen_days)
        if reply_msg.msg_type == MessageType.REPLY:
            return reply_msg.data[0]
        else:
            raise Exception(reply_msg.error_msg)

        # # TODO
        # if facility_name == 'test error':
        #     raise Exception('Facility Is Not Included In The System!')
        # return ["00:00-13:10;14:50-21:00;21:00-23:59" for _ in chosen_days]
