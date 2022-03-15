"The Student Interface"
from abc import ABCMeta, abstractmethod


class IStudentBuilder(metaclass=ABCMeta):
    "The Student Builder Interface"

    @staticmethod
    @abstractmethod
    def calculate_cgpa() -> int:
        "Calculate student CGPA"