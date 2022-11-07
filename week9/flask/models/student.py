from multiprocessing.sharedctypes import Value


class Student:
    def __init__(self, name, student_id, grades=None) -> None:
        self.name = name
        self.student_id = student_id
        if grades is None:
            grades = []
        self.grades = grades

    @property
    def gpa(self):
        if len(self.grades) == 0:
            return 0
        return round(sum(self.grades) / len(self.grades), 2)

    def to_dict(self):
        return {
            "name": self.name,
            "student_id": self.student_id,
            "grades": self.grades
        }

    def add_grade(self, grade):
        num_grade = int(grade)
        if num_grade > 100 or num_grade < 0:
            raise ValueError
        
        self.grades.append(num_grade)
