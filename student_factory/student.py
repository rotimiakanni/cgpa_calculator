"Student builder class"

class Student():
    "Concrete Student class"

    def __init__(self, name) -> None:
        self.name = name
        self.courses = []
        self.cgpa = 0

    def add_course(self, course) -> None:
        "add course to student course list"
        self.courses.append(course)

    def get_cgpa(self) -> int:
        "return student cgpa"
        return self.cgpa

    def calculate_cgpa(self) -> str:
        "calculate student cgpa"
        total_gp = 0
        student_percentile = 0
        for course in self.courses:
            print(course.score, course.gp)
            student_percentile += ((course.score / 10) * course.gp)
            total_gp += course.gp

        return f'Student with name, {self.name}, has a CGPA of \
            {round(student_percentile/total_gp, 2)}' 