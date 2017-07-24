from models.person import Person
from data import tools


class Student(Person):
    students = []
    _file_name = 'csv/students.csv'

    @classmethod
    def add_student(cls, personal_data):
        cls.students.append(Student(*personal_data))

    @classmethod
    def load_students(cls):
        cls.mentors = tools.get_data_from_file(cls._file_name, Student)

    @classmethod
    def get_students(cls):
        return cls.students

    @classmethod
    def save_students_data(cls):
        tools.save_data_to_file(cls.students, cls._file_name, staff_members=True)

    @classmethod
    def prepare_students_data_to_visualize(cls):
        temp = []

        for person in cls.students:
            record = [person.name, person.surname, person.email]
            temp.append(record)

        return temp
