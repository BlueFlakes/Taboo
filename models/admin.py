from models.person import Person
from data import tools


class Admin(Person):
    """class admin, pattern to create user with administrator rights"""

    admins = []
    _file_name = 'csv/admins.csv'

    @classmethod
    def load_admins(cls):
        """Load admins from database"""
        cls.admins = tools.get_data_from_file(cls._file_name, Admin)

    @classmethod
    def get_admins(cls):
        """Give back a collection with admin objects

        Return:
            cls.admins (list)
        """
        return cls.admins

    @classmethod
    def save_admins_data(cls):
        """Load admins to database"""
        tools.save_data_to_file(cls.admins, cls._file_name, staff_members=True)
