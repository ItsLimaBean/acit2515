class Person:
    def __init__(self, name, age):
        if not isinstance(name, str) or len(name) < 3:
            raise AttributeError("name needs to be type string and length >= 3")
        if not isinstance(age, int) or age < 1:
            raise AttributeError("age needs to be type int and value > 0") 

        self.name = name
        self.age = age
    
    def get_name(self):
        return f"{self.name.upper()} / {self.age}"