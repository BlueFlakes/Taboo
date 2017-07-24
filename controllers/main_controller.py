from controllers import login_controller
from controllers import registration_controller
from views import view

def start_controller():
    """Start main controller"""
    begin_communication_with_user()


def begin_communication_with_user():
    """Get inputs from user"""

    user_choice = None
    menu = ['Sign in', 'Register account']
    title = 'Main menu'

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
        login_controller.start_controller()

    elif user_choice == '2':
        registration_controller.start_controller()

    elif user_choice == '0':
        pass

    else:
        view.error_wrong_choice()
