import student, teacher, topics

topic1 = topics.Topic('Python', 'Version Control Systems', 'Relational Databases', 'NoSQL databases', 'Message Brokers')
teacher1 = teacher.Teacher('Ирина', 'Игнатик', 'Александровна', 43, 'f')
st1 = student.Student('Ярослав', 'Гайдуков', 'Эдуардович', 16, 'm')
st2 = student.Student('Максим', 'Трандин', 'Александрович',17, 'm')
st3 = student.Student('Диана', 'Волкова', 'Николаевна', 18, 'f')
st4 = student.Student('Елена', 'Гусева', 'Игоревна', 15, 'f')

teacher1.teach(topic1.topic[0], st4, st3, st1)
teacher1.teach(topic1.topic[1], st4)
teacher1.teach(topic1.topic[2], st3, st2, st1)
teacher1.teach(topic1.topic[3], st4, st3, st1, st2)
teacher1.teach(topic1.topic[4], st2, st3, st4)

print(st1.knowledge)
print(st2.knowledge)
print(st3.knowledge)
print(st4.knowledge)