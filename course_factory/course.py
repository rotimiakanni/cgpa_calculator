"Concrete course class"

class Course():
    "Concrete course class"

    def __init__(self, name, score=0, gp=0) -> None:
        self.name = name
        self.score = score
        self.gp = gp

    def get_course(self) -> str:
        "get name of course"
        return self.name
