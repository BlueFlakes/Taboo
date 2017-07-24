from views import view
from time import sleep
from models.mentor import Mentor
from models.student import Student
from models import common


def start_controller(person_details):
    """Start admin controller"""
    begin_communication_with_user(person_details)


def begin_communication_with_user(person_details):
    """Get inputs from user"""

    user_choice = None
    title = 'Hello ' + person_details.title()
    menu = ['Show mentors', 'Show students', 'Generate code for mentor', 'Generate code for student']

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
        common.print_mentors_data()

    elif user_choice == '2':
        common.print_students_data()

    elif user_choice == '3':
        common.generate_mentor_code()

    elif user_choice == '4':
        common.generate_student_code()

    elif user_choice == '0':
        pass

    else:
        view.error_wrong_choice()
