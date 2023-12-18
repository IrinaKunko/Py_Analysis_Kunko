# 6.	Постройте класс для анализа файла с данными:
# a.	Класс принимает путь к файлу при инициализации
# b.	Создайте метод для чтения файла - метод считывает массив из файла и сохраняет в атрибут класса.
# Файл состоит из строк с произвольным текстом, элементами массива должны быть строки.
# c.	Создайте метод поиска по тексту. Метод принимает паттерн поиска и возвращает список всех найденных совпадений.

import io
import re
import numpy as np

class ParseText:
    def __init__(self, path):
        self.path = path

    def getText(self):
        with open(self.path, 'r') as f_input:
            list_data = f_input.read().split() # читаем с файла разбиваем по пробелам
        self.words = np.array(list_data, str)

    def search(self, pattern) -> list:
        x= []
        for i in self.words:
            res = re.match(pattern, i)
            if res:
                x.append(i)
        return  x       