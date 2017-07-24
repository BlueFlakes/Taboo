from models.codecool import Codecool
from controllers import mentor_controller
from controllers import student_controller
from controllers import admin_controller
from views import view
from time import sleep


def start_controller():
    login()


def login():
    login_questions = ['Login', 'Password']
    user_choice = view.get_inputs(login_questions)
    person = validate_login(user_choice)

    if person:
        run_appropriate_controller(person)


def validate_login(user_input):
    person = Codecool.find_expected_person(*user_input)

    if not person:
        sleep(0.75)
        view.print_error_message('Access Denied: Wrong login or password\n')
        sleep(1.5)

    return person


def run_appropriate_controller(person):
    controller_type = person.__class__.__name__
    person_details = person.name + ' ' + person.surname
    sleep(1)

    if controller_type == 'Mentor':
        mentor_controller.start_controller(person_details)

    elif controller_type == 'Student':
        student_controller.start_controller(person_details)

    elif controller_type == 'Admin':
        admin_controller.start_controller(person_details)
