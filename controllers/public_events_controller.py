from views import view
from time import sleep
from datetime import datetime, timedelta
from models.public_event import PublicEvent
from models import common

def start_controller():
    """Start mentor controller"""
    begin_communication_with_user()


def begin_communication_with_user():
    """Get inputs from user"""

    user_choice = None
    title = 'Public events manager menu'
    menu = ['Add public event', 'Delete public event',
            'Archive out dated public events']

    while user_choice != '0':
        view.clear_window()
        common.show_public_events()
        view.print_menu(title, menu)
        user_choice = view.get_inputs(['What do you want to do'])
        switch_between_menu_options(user_choice)


def switch_between_menu_options(user_choice):
    """Switching between available options, choice depend on user input

    Args:
        user_choice (str)

    """
    if user_choice == '1':
        add_new_public_event()

    elif user_choice == '2':
        delete_choosen_event()

    elif user_choice == '3':
        archive_old_events()

    elif user_choice == '0':
        pass

    else:
        view.error_wrong_choice()


def delete_choosen_event():
    """Delete one of choosen public events"""

    public_events_number = PublicEvent.get_number_of_events()
    user_input = view.get_inputs(['Which record delete, please provide index'])

    try:
        user_input = int(user_input)

    except ValueError:
        view.print_error_message('Wrong input!')
        sleep(0.75)

    else:
        start_index = 1

        if user_input in range(start_index, public_events_number + start_index):
            PublicEvent.delete_event(int(user_input) - start_index)

        else:
            view.print_error_message('Out of range!')
            sleep(0.75)


def archive_old_events():
    """Archive out dated entries"""

    PublicEvent.archive_old_entries()
    view.print_result('Succesfully deleted old entries.')
    sleep(1)



def add_new_public_event():
    """Add new public event"""
    event_data = get_new_public_event_data()
    PublicEvent.add_event(PublicEvent(*event_data))


def get_new_public_event_data():
    """Collect needed information and delegate validation to another function

    Return:
        temp (list)

    """
    list_of_questions = ['Public event title', 'Public event Desctription',
                         'Date, at least more than 24 hours from current time (' +
                          str(datetime.now())[:13] + ').\nformat YYYY-MM-DD-HH']
    temp = []

    for i, question in enumerate(list_of_questions):
        user_input_is_valid = False
        user_input = None

        while user_input_is_valid is False:
            view.clear_window()
            user_input = view.get_inputs([question])
            user_input_is_valid = validate_provided_inputs(i, user_input)

        temp.append(user_input)

    return temp


def validate_provided_inputs(step, user_input):
    """Check the correctness of provided inputs with expected ones
    Args:
        step (int): loop step
        user_input (str)

    Return:
        valid_input (bool)

    """
    user_input = user_input.strip()
    min_input_length = 3
    max_input_length = 70
    valid_input = True

    if len(user_input) >= min_input_length and len(user_input) <= max_input_length:
        if step == 2:
            valid_input = validate_provided_date(user_input)

    else:
        if len(user_input) > max_input_length:
            view.error_state_locker('Too long!')

        elif len(user_input) < min_input_length:
            view.error_state_locker('Too short!')

        valid_input = False

    return valid_input


def validate_provided_date(date):
    """Specific validation section for date

    Args:
        date (str)

    Return:
        valid_input (bool)
    """
    valid_input = False

    try:
        date = datetime.strptime(date, "%Y-%m-%d-%H")

    except ValueError:
        view.error_state_locker('Wrong date format')

    else:
        current_date_plus_24h = datetime.now() + timedelta(hours=24)

        if date > current_date_plus_24h:
            valid_input = True

        else:
            view.error_state_locker('Too early, nobody will be on time.')


    return valid_input
