from models.codecool import Codecool
from controllers import mentor_controller
from controllers import student_controller
from controllers import admin_controller
from views import view
from time import sleep


def start_controller():
    """Start login controller"""
    login()


def login():
    """Get inputs from user"""
    login_questions = ['Login', 'Password']
    user_choice = view.get_inputs(login_questions)
    person = validate_login(user_choice)

    if person:
        run_appropriate_controller(person)


def validate_login(user_input):
    """Validate given login and password

    Args:
        user_input (list): login and password

    Return:
        person (object/none): finding score

    """

    person = Codecool.find_expected_person(*user_input)

    if not person:
        sleep(0.5)
        view.print_error_message('Access Denied: Wrong login or password\n')
        sleep(1.25)

    return person


def run_appropriate_controller(person):
    """Passes person object to run adequate controller

    Args:
        person (object)

    """
    controller_type = person.__class__.__name__
    sleep(0.5)

    if controller_type == 'Mentor':
        person_details = person.name + ' ' + person.surname + ' (Status Mentor)'
        mentor_controller.start_controller(person_details)

    elif controller_type == 'Student':
        person_details = person.name + ' ' + person.surname + ' (Status Student)'
        student_controller.start_controller(person_details)

    elif controller_type == 'Admin':
        person_details = person.name + ' ' + person.surname + ' (Status Admin)'
        admin_controller.start_controller(person_details)
