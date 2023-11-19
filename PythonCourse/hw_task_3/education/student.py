from hw_task_3.education.person import Person
import random


class Student(Person):
    def __init__(self, first_name, last_name, surname, age, gender):
        super().__init__(first_name, last_name, surname, age, gender)
        self.knowledge = []

    def take(self, topic):
        self.knowledge.append(topic)

    def __len__(self):
        return len(self.knowledge)

    def forget(self):
        self.knowledge.pop(random.choice(range(len(self.knowledge))))