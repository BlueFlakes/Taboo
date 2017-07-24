from controllers import login_controller
from controllers import registration_controller
from views import view

def start_controller():
    user_choice = None
    menu = ['Sign in', 'Register account']
    title = 'Hello dear user'

    while user_choice != '0':
        view.clear_window()
        view.print_menu(title, menu)
        user_choice = view.get_inputs(['What do you want to do'])

        switch_between_menu_options(user_choice)


def switch_between_menu_options(user_choice):
    if user_choice == '1':
        login_controller.start_controller()

    elif user_choice == '2':
        registration_controller.start_controller()

    elif user_choice == '0':
        pass

    else:
        view.error_state_locker()
