from models.person import Person
from data import tools


class Admin(Person):
    admins = []
    _file_name = 'csv/admins.csv'

    @classmethod
    def load_admins(cls):
        cls.admins = tools.get_data_from_file(cls._file_name, Admin)

    @classmethod
    def get_admins(cls):
        return cls.admins

    @classmethod
    def save_admins_data(cls):
        tools.save_data_to_file(cls.admins, cls._file_name, staff_members=True)
