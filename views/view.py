import sys
import tty
import termios
import os
from prettytable import PrettyTable, ALL

def get_inputs(provided_questions, title=''):
    """Get inputs from user

    Args:
        provided_questions (str): questions to user
        title (str): Title of the activity performed

    Return:
        delivered_data_by_user (str, list): Depends on amount of delivered data.

    """
    temp = []

    if title:
        print(title + ':', end=2*'\n')

    for question in provided_questions:
        user_input = input(question + ': ')
        temp.append(user_input)

    delivered_data_by_user = choose_data_type_for_input(temp)

    return delivered_data_by_user


def choose_data_type_for_input(array):
    """Modify provided data because getting what we should get is always better
    than what we don't expected like input always return string, but in this case
    it would be list with one string. We need a list just while we need to store
    more than one input somewhere.

    Args:
        array (list)

    Return:
        temp (str, list): Depends on amount of delivered data

    """
    temp = None

    if len(array) in [0, 1]:
        temp = array[0]

    elif len(array) > 1:
        temp = array

    return temp


def clear_window():
    """Clear main window"""
    os.system("clear")




def print_message(message):
    """Prints to user a information.

    Args:
        message (str)
    """
    print(message)

def error_state_locker(message):
    """Print provided message and lock actual state"""
    print_error_message('\n' + message)
    locker()

def error_wrong_choice():
    """Lock state of application until user press a key"""

    print_error_message("\nWarning: this action doesn't exist! Press any key.")
    locker()


def state_locker():
    """Lock state of application until user press a key"""

    print('\033[93m' + '\nPress any key to exit this state' + '\033[0m')
    locker()


def locker():
    """Lock the state of app"""
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)

    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)

    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)


def print_error_message(error_msg):
    """
    Print error message

    Args:
        error_msg (str):

    """
    print('\033[91m' + error_msg + '\033[0m', end=2*'\n')

def print_menu(title, available_options, exit_message='Exit'):
    """Print out menu to user

    Args:
        title (str): menu title
        provided_questions (list):
        exit_message (str):

    """
    compilated_message = available_options + [exit_message]

    print(title + ':')

    for i, option in enumerate(compilated_message):
        print('{}{}. {}'.format('\t', (i+1) % len(compilated_message), option))

    print()

def print_result(message):
    """Prints result to the user"""
    print('\033[94m' + message + '\033[0m')


def print_table(titles, data, enumerate_table=False):
    """

    Args:
        titles (list)
        data (list): its list with nested list (records) for rows

    """
    prettytable = PrettyTable(titles, hrules=ALL)

    for i, record in enumerate(data):
        if enumerate_table:
            prettytable.add_row([str(i+1)] + record)

        elif not enumerate_table:
            prettytable.add_row(record)

    print(prettytable)



def print_all_events(events):
    for event in events:
        print(event)

def print_main_menu():
    print("""Choose Option
             1. Book Private Mentoring
             2. Book checkpoint
             3. Show all my events
    """)

def print_goodbye():
    print('Bye Bye!')

def get_choice():
    return input('Choose option: ')

def get_checkpoint_details():
    return self.get_event_date()

def get_event_date():
    return input('Enter the date dd-mm-yyyy: ')

def get_preffered_mentor(self):
    return input('Enter preffered mentor: ')

def get_goal(self):
    return input('Enter your goal: ')
