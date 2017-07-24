from models.mentor import Mentor
from models.student import Student
from models.admin import Admin


class Codecool:
    codecoolers = []

    @classmethod
    def _compile_codecoolers(cls):
        cls.codecoolers = Student.get_students() + Mentor.get_mentors() + Admin.get_admins()

    @classmethod
    def get_codecoolers(cls):
        return cls.codecoolers

    @classmethod
    def refresh_existing_codecoolers(cls):
        cls._compile_codecoolers()

    @classmethod
    def find_expected_person(cls, provided_login, provided_password):
        temp = None

        for person in cls.codecoolers:
            if person.login == provided_login and person.password == provided_password:
                temp = person
                break

        return temp
