"Student director class"

from course_factory.biology_director import BiologyDirector
from course_factory.chemistry_director import ChemistryDirector
from course_factory.maths_director import MathsDirector
from student_factory.student_builder import StudentBuilder


class StudentDirector:
    "Student Director class"
    
    @staticmethod
    def construct(name):
        stud = StudentBuilder(name).get_result()
        stud.add_course(BiologyDirector.construct(70, 5))
        stud.add_course(ChemistryDirector.construct(60, 8))
        stud.add_course(MathsDirector.construct(60, 4))
        return stud.calculate_cgpa()