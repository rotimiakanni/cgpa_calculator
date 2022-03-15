"maths director class that aggregates the course builder"

from course_factory.course_builder import CourseBuilder


class MathsDirector:
    "maths director class"
    
    @staticmethod
    def construct(score, gp):
        return CourseBuilder('Maths').\
            set_score(score).\
                set_gp(gp).\
                    get_course()