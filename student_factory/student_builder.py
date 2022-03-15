"The Builder Class"

from student_factory.student import Student
from student_factory.student_interface import IStudentBuilder


class StudentBuilder(IStudentBuilder):
    "The Student Builder."

    def __init__(self, name):
        self.student = Student(name)

    def calculate_cgpa(self) -> int:
        return self.student.calculate_cgpa()
    
    def get_result(self):
        return self.student
