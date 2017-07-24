from models.person import Person
from data import tools


class Mentor(Person):
    mentors = []
    _file_name = 'csv/mentors.csv'


    @classmethod
    def add_mentor(cls, personal_data):
        cls.mentors.append(Mentor(*personal_data))

    @classmethod
    def load_mentors(cls):
        cls.mentors = tools.get_data_from_file(cls._file_name, Mentor)

    @classmethod
    def get_mentors(cls):
        return cls.mentors

    @classmethod
    def save_mentors_data(cls):
        tools.save_data_to_file(cls.mentors, cls._file_name, staff_members=True)

    @classmethod
    def prepare_mentors_data_to_visualize(cls):
        temp = []

        for person in cls.mentors:
            record = [person.name, person.surname, person.email]
            temp.append(record)

        return temp
