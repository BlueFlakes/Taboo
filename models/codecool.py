from models.mentor import Mentor
from models.student import Student
from models.admin import Admin


class Codecool:
    codecoolers = []

    @classmethod
    def _compile_codecoolers(cls):
        """Compile every codecool member to one collection"""
        cls.codecoolers = Student.get_students() + Mentor.get_mentors() + Admin.get_admins()

    @classmethod
    def get_codecoolers(cls):
        """Give back a collection with all memebers of codecool

        Return:
            cls.codecoolers (list)

        """
        return cls.codecoolers

    @classmethod
    def refresh_existing_codecoolers(cls):
        """Refresh members list"""
        cls._compile_codecoolers()

    @classmethod
    def find_expected_person(cls, provided_login, provided_password):
        """Look for a object which login and password matches with provided ones.

        Args:
            provided_login (str)
            provided_password (str)

        Return:
            temp (object)
        """
        temp = None

        for person in cls.codecoolers:
            if person.login == provided_login and person.password == provided_password:
                temp = person
                break

        return temp
