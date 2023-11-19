from hw_task_3.education.person import Person


class Teacher(Person):
    def __init__(self, first_name, last_name, surname, age,  gender):
        super().__init__(first_name, last_name, surname, age, gender)
        self.students = 0

    def teach(self, topic, *stud):
        students = [item for item in stud]
        # map(lambda x: x.take(topic), students) не работает
        for s in students:
            s.take(topic)
        self.students = self.students + 1
