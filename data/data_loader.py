from models.mentor import Mentor
from models.student import Student
from models.codecool import Codecool
from models.admin import Admin
from models.registration_code import RegistrationCode
from models.public_event import PublicEvent

def load_data_from_files():
    """Load data from csv files to application"""

    Mentor.load_mentors()
    Student.load_students()
    Admin.load_admins()
    RegistrationCode.load_registration_codes()
    PublicEvent.load_public_events()
    Codecool._compile_codecoolers()

def save_data_to_files():
    """Save data to csv files from application"""

    Mentor.save_mentors_data()
    Student.save_students_data()
    Admin.save_admins_data()
    RegistrationCode.save_registration_codes()
    PublicEvent.save_public_events()
