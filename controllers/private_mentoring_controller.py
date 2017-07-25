from views import view
from time import sleep
from models import common
from controllers import public_events_controller
from models.mentor import Mentor


def start_controller(status):
    """Start mentor controller"""

    student_side(status)


def student_side():
    """Get inputs from user"""
    user_choice = None
    title = 'Private mentoring manager'
    menu = ['Sign up for private mentoring', 'Show score of my appeals']

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
        sign_up_for_private_mentoring()

    elif user_choice == '2':
        pass



    elif user_choice == '0':
        pass

    else:
        view.error_wrong_choice()

def sign_up_for_private_mentoring():
    sign_up_details = get_sign_up_data()




def get_sign_up_data():
    list_of_questions = ['Choose preffered mentor', 'Set goal for mentoring',
                        'Date, format YYYY-MM-DD-HH']

    sign_up_data = []

    for i, question in enumerate(list_of_questions):
        user_input_is_valid = False
        user_input = None

        while user_input_is_valid is False:
            view.clear_window()
            additional_conditions(i)
            user_input = view.get_inputs([question])
            user_input_is_valid = validate_user_personal_data(question, user_input)

        sign_up_data.append(user_input)

    return sign_up_data

def additional_conditions(step):
    if step == 0:

        view.print_menu('Mentors list', )











#
