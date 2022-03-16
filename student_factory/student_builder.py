"The Builder Class"

from .student import Student
from .student_interface import IStudentBuilder


class StudentBuilder(IStudentBuilder):
    "The Student Builder."

    def __init__(self, name):
        self.student = Student(name)

    def calculate_cgpa(self) -> int:
        "calculate student cgpa"
        return self.student.calculate_cgpa()

    def get_result(self):
        "Get student result"
        return self.student
