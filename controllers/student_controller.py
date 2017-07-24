from views import view
from time import sleep
from models import common


def start_controller(person_details):
    user_choice = None
    title = 'Hello ' + person_details.title()
    menu = ['Show mentors', 'Show students', 'Generate code for new employee']

    while user_choice != '0':
        view.clear_window()
        view.print_menu(title, menu)
        user_choice = view.get_inputs(['What do you want to do'])
        switch_between_menu_options(user_choice)


def switch_between_menu_options(user_choice):
    if user_choice == '1':
        pass

    elif user_choice == '2':
        pass

    elif user_choice == '3':
        pass

    elif user_choice == '0':
        pass

    else:
        view.error_state_locker()
