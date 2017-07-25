from views import view
from models.student import Student
from models.mentor import Mentor
from models.public_event import PublicEvent
from models.registration_code import RegistrationCode
from time import sleep


def show_public_events(lock_state=False):
    events_data = PublicEvent.prepare_events_data_to_visualize()
    titles = ['idx', 'Date', 'Title', 'Description']

    view.clear_window()
    view.print_table(titles, events_data, enumerate_table=True)
    if not PublicEvent.get_number_of_events():
        view.print_result('No records at all.')

    if lock_state:
        view.state_locker()


def show_people_data(people, detailed=False):
    """Present people data like name, surname and e mail in table

    Args:
        people (list of objects)

    """
    sleep(0.5)
    view.clear_window()

    if detailed:
        titles = ['login', 'password', 'Name', 'Surname', 'Email']
        view.print_table(titles, people)
        display_info_about_people_amount(people)
        view.state_locker()

    elif not detailed:
        titles = ['Name', 'Surname', 'Email']
        view.print_table(titles, people)
        display_info_about_people_amount(people)


def display_info_about_people_amount(people):
    if len(people) == 0:
        print('OOooops no records!')
        sleep(0.75)


def manage_mentors_data_displaying():
    print_mentors_data()
    question = 'Type "yes" to see detailed mentors data, otherwise type anything'
    user_choice = view.get_inputs([question])

    if user_choice.lower() == 'yes':
        print_mentors_data(detailed=True)


def manage_students_data_displaying():
    print_students_data()
    question = 'Type "yes" to see detailed mentors data, otherwise type anything'
    user_choice = view.get_inputs([question])

    if user_choice.lower() == 'yes':
        print_students_data(detailed=True)


def print_mentors_data(detailed=False):
    """Get prepared mentors data to visualize and move it to the next step"""

    mentors = Mentor.prepare_mentors_data_to_visualize(detailed)
    show_people_data(mentors, detailed)


def print_students_data(detailed=False):
    """Get prepared students data to visualize and move it to the next step"""

    students = Student.prepare_students_data_to_visualize(detailed)
    show_people_data(students, detailed)
