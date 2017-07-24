from data import data_manager


def get_data_from_file(file_name, object_type):
    """
    Convert data from csv file to SubmitAssignment object and add it to list

    Args:
        file_name (string): name of file to open
        return_type (:class:): indicate what class return will be

    Returns:
        list of :obj:: temporary list of objects
    """

    temp_list_of_records = data_manager.load_data(file_name)
    temp_list_of_objects = []

    for record in temp_list_of_records:
        to_append = object_type(*record)

        temp_list_of_objects.append(to_append)

    return temp_list_of_objects


def prepare_people_data(list_of_persons):
    temp = []

    for person in list_of_persons:
        record = [person.login, person.password, person.name, person.surname,
                  person.email]

        temp.append(record)

    return temp

def save_data_to_file(data, file_name, staff_members=False):
    if staff_members:
        data = prepare_people_data(data)

    data_manager.save_data_to_file(file_name, data)
