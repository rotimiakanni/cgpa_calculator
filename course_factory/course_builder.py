"The Course Builder Class"

from course_factory.course import Course
from course_factory.course_interface import ICourseBuilder


class CourseBuilder(ICourseBuilder):
    "The Course Builder."

    def __init__(self, name: str) -> None:
        self.course = Course(name)

    def set_gp(self, gp: int) -> Course:
        "set student GP for the course"
        self.course.gp = gp
        return self

    def set_score(self, score: int) -> Course:
        "set student score for the course"
        self.course.score = score
        return self
    
    def get_course(self) -> Course:
        "get the instance of the built course"
        return self.course
