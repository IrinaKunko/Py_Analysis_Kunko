class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

class Student(Person):
    def __init__(self, first_name, last_name, course):
        self.course = course
        # Выполнение инициализации родительского класса
        super().__init__(first_name, last_name)

