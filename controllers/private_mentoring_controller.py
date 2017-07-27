from views import view
from time import sleep
from models import common
from controllers import public_events_controller
from models.mentor import Mentor
from datetime import datetime


def start_controller(status):
    """Start mentor controller"""
    if status == 'Student':
        run_student_side()

    elif status == 'Mentor':
        run_mentor_side()


def run_mentor_side():
    pass


def run_student_side():
    """Get inputs from user"""
    user_choice = None
    title = 'Private mentoring manager'
    menu = ['Sign up for private mentoring', 'Show score of my appeals']

    while user_choice != '0':
        view.clear_window()
        view.print_menu(title, menu)
        user_choice = view.get_inputs(['What do you want to do'])
        student_menu_options(user_choice)


def student_menu_options(user_choice):
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
    user_sign_up_details = get_sign_up_data()


def get_sign_up_data():
    list_of_questions = ['Choose preffered mentor', 'Set goal for mentoring',
                        'Date, format YYYY-MM-DD-HH']

    sign_up_data = []

    for i, question in enumerate(list_of_questions):
        user_input_is_valid = False
        user_input = None

        while user_input_is_valid is False:
            view.clear_window()
            print_explanations(i)
            user_input = view.get_inputs([question])
            user_input_is_valid = validate_inputs(i, user_input)

        sign_up_data.append(user_input)

        if user_input == '0':
            break

    return sign_up_data


def print_explanations(step):
    if step == 0:
        mentors_public_data = Mentor.get_mentors_names_and_surnames()
        view.print_menu('Mentors list', mentors_public_data)


def validate_inputs(step, user_input):
    valid_input = False

    if user_input == '0':
        # way to get out of sign up for private-mentoring mode
        valid_input = True

    elif step == 0:
        valid_input = validate_choosen_mentor(valid_input, user_input)

    elif step == 1:
        valid_input = validate_goal_informations(valid_input, user_input)

    elif step == 2:
        valid_input = validate_date_format(valid_input, user_input)


    return valid_input

def validate_choosen_mentor(valid_input, user_input):
    mentors_amount = Mentor.get_number_of_mentors()

    if user_input in [str(i) for i in range(1, mentors_amount + 1)]:
        valid_input = True

    else:
        view.error_state_locker('Wrong value!')

    return valid_input


def validate_goal_informations(valid_input, user_input):
    min_message_length = 3
    max_message_length = 30

    if len(user_input) >= min_message_length and len(user_input) <= max_message_length:
        valid_input = True

    else:
        view.error_state_locker('At least 3 characters and max 30 please provide.')

    return valid_input

def validate_date_format(valid_input, user_input):

    try:
        datetime.strptime(user_input, "%Y-%m-%d-%H")
        valid_input = True

    except ValueError:
        view.error_state_locker('Wrong data format.')

    return valid_input








#
