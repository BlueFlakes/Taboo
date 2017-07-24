from models.registration_code import RegistrationCode
from models.codecool import Codecool
from models.mentor import Mentor
from models.student import Student
from views import view
from time import sleep

def start_controller():
    user_input = view.get_inputs(['Please give me unique code'])
    found_regr_obj = RegistrationCode.find_code(user_input)
    prefix_length = 2
    mentor_prefix = 'MT'
    student_prefix = 'ST'


    if found_regr_obj:
        prefix = found_regr_obj.code[:prefix_length]

        if prefix == mentor_prefix:
            create_mentor()

        elif prefix == student_prefix:
            create_student()

        Codecool.refresh_existing_codecoolers()

    else:
        view.print_error_message('Wrong code delivered!')
        sleep(1)


def get_user_details():
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
    valid_input = True

    if len(user_input) >= 1:
        if question == 'login':
            valid_input = validate_suggested_login(user_input)

    return valid_input


def validate_suggested_login(user_input):
    valid_input = False
    occupied_logins = [person.login.lower() for person in Codecool.get_codecoolers()]
    print(occupied_logins)

    if user_input.lower() not in occupied_logins:
        valid_input = True

    else:
        view.print_error_message('Already occupied, choose another login.')
        sleep(1.5)


    return valid_input


def create_mentor():
    user_details = get_user_details()
    Mentor.add_mentor(user_details)


def create_student():
    user_details = get_user_details()
    Student.add_student(user_details)
