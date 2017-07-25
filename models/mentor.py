from models.person import Person
from data import tools
from collections import OrderedDict


class Mentor(Person):
    mentors = []
    _file_name = 'csv/mentors.csv'


    @classmethod
    def add_mentor(cls, personal_data):
        """Add new mentor to collection"""
        cls.mentors.append(Mentor(*personal_data))

    @classmethod
    def load_mentors(cls):
        """Load mentors from file"""
        cls.mentors = tools.get_data_from_file(cls._file_name, Mentor)

    @classmethod
    def get_mentors(cls):
        """Give back a collection with mentor objects

        Return:
            cls.mentors (list)

        """
        return cls.mentors

    @classmethod
    def save_mentors_data(cls):
        """Save mentors data to file"""
        tools.save_data_to_file(cls.mentors, cls._file_name, staff_members=True)

    @classmethod
    def get_mentors_alphabetically_sorted(cls):
        return OrderedDict([[mentor.login, mentor] for mentor in cls.mentors])



    @classmethod
    def prepare_mentors_data_to_visualize(cls, add_details=False):
        """Prepare objects to format which can be interpreted
        by a table function and visualized.

        Return:
            temp (list)
        """
        temp = []

        for person in cls.mentors:
            if add_details:
                record = [person.login, person.password, person.name, person.surname, person.email]

            elif not add_details:
                record = [person.name, person.surname, person.email]

            temp.append(record)

        return temp
