from models.registration_code import RegistrationCode
from models.codecool import Codecool
from models.mentor import Mentor
from models.student import Student
from views import view
from time import sleep

def start_controller():
    """Start registration controller"""
    begin_communication_with_user()


def begin_communication_with_user():
    """Get inputs from user"""

    RegistrationCode.refresh_available_codes()
    user_input = view.get_inputs(['Please give me unique code'])
    found_regr_obj = RegistrationCode.find_code(user_input)
    prefix_length = 2
    mentor_prefix = 'MT'
    student_prefix = 'ST'


    if found_regr_obj:
        view.print_result('Given key loaded properly!')
        sleep(1)
        view.clear_window()
        prefix = found_regr_obj.code[:prefix_length]

        if prefix == mentor_prefix:
            create_mentor()

        elif prefix == student_prefix:
            create_student()

        Codecool.refresh_existing_codecoolers()

    else:
        sleep(0.5)
        view.print_error_message('Wrong code delivered!')
        view.print_result('Only admin can create new unique code to register user.')
        view.error_state_locker('')


def get_user_details():
    """Get details about user personal data from user

    Return:
        user_data (list)

    """
    list_of_questions = ['login', 'password', 'name', 'surname', 'email']
    user_data = []

    for question in list_of_questions:
        user_input_is_valid = False
        user_input = None

        while user_input_is_valid is False:
            view.clear_window()
            user_input = view.get_inputs([question])
            user_input_is_valid = validate_user_personal_data(question, user_input)

        user_data.append(user_input)

    return user_data


def validate_user_personal_data(question, user_input):
    """Validate provided data by user

    Args:
        question (str)
        user_input (str)

    Return:
        valid_input (bool)

    """
    user_input = user_input.strip()
    min_input_length = 3
    max_input_length = 20
    valid_input = True

    if len(user_input) >= min_input_length and len(user_input) <= max_input_length:
        if question == 'login':
            valid_input = validate_suggested_login(user_input)

    else:
        if len(user_input) > max_input_length:
            view.error_state_locker('Too long!')

        elif len(user_input) < min_input_length:
            view.error_state_locker('Too short!')

        valid_input = False

    return valid_input


def validate_suggested_login(user_input):
    """validate login given by user, because login is unique id for every user.

    Args:
        user_input (str)

    Return:
        valid_input (bool)

    """
    valid_input = False
    occupied_logins = [person.login.lower() for person in Codecool.get_codecoolers()]

    if user_input.lower() not in occupied_logins:
        valid_input = True

    else:
        view.print_error_message('Already occupied, choose another login.')
        sleep(1.5)


    return valid_input


def create_mentor():
    """Create mentor"""
    user_details = get_user_details()
    Mentor.add_mentor(user_details)


def create_student():
    """Create student"""
    user_details = get_user_details()
    Student.add_student(user_details)
