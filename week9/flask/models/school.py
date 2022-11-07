import json

from models.student import Student


class School:
    def __init__(self, filename) -> None:
        self.filename = filename
        self._students = []
        self.name = ""
        self.load_from_json()

    def load_from_json(self):
        with open(self.filename, "r") as f:
            json_data = json.load(f)
            self.name = json_data["name"]
            for student in json_data["students"]:
                instance = Student(student["name"], student["student_id"], student["grades"])
                self._students.append(instance)

    def get_students(self, sorted_by):
        if sorted_by == "name":
            return sorted(self._students, key=lambda x: x.name)
        elif sorted_by == "gpa":
            return sorted(self._students, key=lambda x: x.student_id)

    def get_student(self, student_id):
        student = None
        for stu in self._students:
            if student_id == stu.student_id:
                student = stu
                break
        return student

    def to_dict(self):
        return {
            "name": self.name,
            "students": [ s.to_dict() for s in self._students ]
        }

    def save(self):
        with open(self.filename, "w") as file:
            json.dump(self.to_dict(), file)

    def __len__(self):
        return len(self._students)

    def add_student(self, name, student_id):
        if not isinstance(name, str) or not isinstance(student_id, str):
            raise ValueError
        if len(name) == 0 or len(student_id) == 0:
            raise ValueError

        if self.get_student(student_id) is not None:
            return False

        self._students.append(Student(name, student_id))

        return True