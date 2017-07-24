from models.mentor import Mentor
from models.student import Student
from models.codecool import Codecool
from models.admin import Admin

def load_data_from_files():
    Mentor.load_mentors()
    Student.load_students()
    Admin.load_admins()
    Codecool._compile_codecoolers()

def save_data_to_files():
    Mentor.save_mentors_data()
    Student.save_students_data()
    Admin.save_admins_data()
