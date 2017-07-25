from views import view
from time import sleep
from models import common
from controllers import public_events_controller

def start_controller(person_details):
    """Start mentor controller"""
    begin_communication_with_user(person_details)


def begin_communication_with_user(person_details):
    """Get inputs from user"""

    user_choice = None
    title = 'Hello ' + person_details.title()
    menu = ['Show students', 'Show public events', 'Manage public events','Private mentoring']

    while user_choice != '0':
        view.clear_window()
        view.print_menu(title, menu)
        user_choice = view.get_inputs(['What do you want to do'])
        switch_between_menu_options(user_choice)


def switch_between_menu_options(user_choice):
    """Switching between available options, choice depend on user input

    Args:
        user_choice (str)

    """
    if user_choice == '1':
        common.manage_students_data_displaying()

    elif user_choice == '2':
        common.show_public_events(lock_state=True)

    elif user_choice == '3':
        public_events_controller.start_controller()

    elif user_choice == '4':
        pass

    elif user_choice == '0':
        pass

    else:
        view.error_wrong_choice()
