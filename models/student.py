from models.person import Person
from data import tools


class Student(Person):
    students = []
    _file_name = 'csv/students.csv'

    @classmethod
    def add_student(cls, personal_data):
        """Add new student object to collection"""
        cls.students.append(Student(*personal_data))

    @classmethod
    def load_students(cls):
        """Load students data from file"""
        cls.students = tools.get_data_from_file(cls._file_name, Student)

    @classmethod
    def get_students(cls):
        """Give back a collection with student objects

        Return:
            cls.students (list)

        """
        return cls.students

    @classmethod
    def save_students_data(cls):
        """save students to file"""
        tools.save_data_to_file(cls.students, cls._file_name, staff_members=True)

    @classmethod
    def prepare_students_data_to_visualize(cls, add_details=False):
        """Prepare objects to format which can be interpreted
        by a table function and visualized.

        Return:
            temp (list)
        """
        temp = []

        for person in cls.students:
            if add_details:
                record = [person.login, person.password, person.name, person.surname, person.email]

            elif not add_details:
                record = [person.name, person.surname, person.email]

            temp.append(record)

        return temp
