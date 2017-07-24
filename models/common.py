from views import view
from models.student import Student
from models.mentor import Mentor
from models.registration_code import RegistrationCode
from datetime import date, datetime
import random

def show_people_data(people):
    """Present people data like name, surname and e mail in table

    Args:
        people (list of objects)

    """
    view.clear_window()
    titles = ['Name', 'Surname', 'Email']
    view.print_table(titles, people)
    if len(people) == 0:
        print('OOooops no records!')

    view.state_locker()


def print_mentors_data():
    """Get prepared mentors data to visualize and move it to the next step"""

    mentors = Mentor.prepare_mentors_data_to_visualize()
    show_people_data(mentors)


def print_students_data():
    """Get prepared students data to visualize and move it to the next step"""

    students = Student.prepare_students_data_to_visualize()
    show_people_data(students)


def generate_code():
    """Unique code generator for account registration

    Return:
        code (str)

    """

    CODE_LENGTH = 8
    code = ''

    special_signs = ['*', '/', '&', '%', '$', '#', '@']
    digits = list(range(0, 10))
    alpha = [chr(i) for i in range(65, 91)] + [chr(i) for i in range(97, 123)]
    signs_sum = special_signs + digits + alpha

    for i in range(CODE_LENGTH):
        code += str(random.choice(signs_sum))

    return code


def get_unique_code():
    """Filter out repeatable values from code generator and waiting for unique one

    Return:
        code (str): which is unique
    """

    existing_codes = RegistrationCode.get_registration_codes()
    is_code_unique = False
    code = None

    while not is_code_unique:
        code = generate_code()

        if code not in existing_codes:
            is_code_unique = True

    return code



def generate_mentor_code():
    """generate a code for user to create account on mentor rights"""

    prefix = 'MT'
    postfix = get_unique_code()
    code = prefix + postfix

    RegistrationCode.add_code([code, str(date.today())])
    view.print_result('Succesfully created a new mentor code: ' + prefix + postfix)
    view.print_result('Code will expire in the next day!')
    view.state_locker()


def generate_student_code():
    """generate a code for user to create account on student rights"""
    prefix = 'ST'
    postfix = get_unique_code()
    code = prefix + postfix

    RegistrationCode.add_code([code, str(date.today())])
    view.print_result('Succesfully created a new student code: ' + prefix + postfix)
    view.print_result('Code will expire in the next day!')
    view.state_locker()
