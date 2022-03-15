"The Course Interface"
from abc import ABCMeta, abstractmethod

from course_factory.course import Course


class ICourseBuilder(metaclass=ABCMeta):
    "The Course Builder Interface"

    @staticmethod
    @abstractmethod
    def set_gp() -> int:
        "Set student Gp for the course"

    @staticmethod
    @abstractmethod
    def set_score() -> int:
        "Set student score for the course"

    def get_course() -> Course:
        "Get the course object"