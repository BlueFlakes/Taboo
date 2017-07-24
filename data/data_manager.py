import csv
from views import view

def read_file(file_name):
    temp = []

    with open(file_name, 'r') as csvfile:
        data_reader = csv.reader(csvfile)

        for record in data_reader:
            temp.append(record)

    return temp

def secure_data_loading(file_name):
    temp = []

    try:
        temp = read_file(file_name)

    except FileNotFoundError:
        message = file_name[4:]
        view.print_error_message(message + ' not found in csv folder.')
        view.state_locker()

    return temp

def load_data(file_name):
    loaded_data = secure_data_loading(file_name)

    return loaded_data


def save_data_to_file(file_name, data):

    with open(file_name, 'w') as csvfile:
        data_writer = csv.writer(csvfile)

        for record in data:
            data_writer.writerow(record)
