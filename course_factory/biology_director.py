"Biology director class that aggregates the course builder"

from course_factory.course_builder import CourseBuilder


class BiologyDirector:
    "Biology Director class"
    
    @staticmethod
    def construct(score, gp):
        return CourseBuilder('Biology').\
            set_score(score).\
                set_gp(gp).\
                    get_course()