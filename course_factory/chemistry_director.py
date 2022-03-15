"Chemistry director class that aggregates the course builder"

from course_factory.course_builder import CourseBuilder


class ChemistryDirector:
    "CHemistry Director class"
    
    @staticmethod
    def construct(score, gp):
        return CourseBuilder('Chemistry').\
            set_score(score).\
                set_gp(gp).\
                    get_course()