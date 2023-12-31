import numpy as np
import parsetext

# 1.	Создайте вектор размером 10 с рандомными значениями, отсортируйте и выведите в консоль.
a = np.sort(np.array(np.random.randint(0, 100, 10)))
print(a)

# 2.	Создайте матрицу 8х8 состоящую из 1 и 0 и заполненную в шахматном порядке
arlist = []
for i in range(8):
    for j in range(8):
        arlist.append((i+j)%2)
matrix = np.array(arlist, int).reshape((8, 8))
print(matrix)

# 3.	Создайте матрицы 8x4 и 4x2 и перемножьте, результирующую матрицу выведите в консоль. 
matrix1= np.array(range(32), int).reshape((8, 4))
matrix2= np.array(range(8), int).reshape((4, 2))
print(np.dot(matrix1, matrix2))

# 4.	Создать вектор размера 10 со значениями от 0 до 1, не включая ни то, ни другое.
vec = np.array(np.random.random(size=10), float)
print(vec)

# 5.	Создайте функцию, которая
# a.	принимает число (количество элементов в матрице)
# b.	Проверяет можно ли построить матрицы с размерностью из множителей принимаемого числа.
# c.	При проверке не учитывать матрицы с множителем “1”
# d.	постройте все возможные матрицы и выведите в консоль.
# e.	если число нельзя разбить на множители без остатка выведите сообщение в консоль.
def function(value):
    flag = True
    for i in range(2, value):
        if value%i==0:
            print(np.zeros((i, int(value/i))))
            flag = False
    if flag:
        print('Число нельзя разбить на множители без остатка')

function(72)
function(5)
# 6.	Постройте класс для анализа файла с данными:
# a.	Класс принимает путь к файлу при инициализации
# b.	Создайте метод для чтения файла - метод считывает массив из файла и сохраняет в атрибут класса.
# Файл состоит из строк с произвольным текстом, элементами массива должны быть строки.
# c.	Создайте метод поиска по тексту. Метод принимает паттерн поиска и возвращает список всех найденных совпадений.

obj = parsetext.ParseText('pythcourse/text.txt')
obj.getText()
print(obj.search(r'th'))

# 7.	напишите функцию которая
# a.	принимает 
# i.	вектор A длинной X 
# ii.	размер слоя S - натуральное число
# iii.	Булевый параметр last - по умолчанию False
# b.	генерируется случайную матрицу B размером SxX
# c.	создайте новую матрицу - произведение вектора A и матрицы B
# d.	Найдите сумму каждой строки результирующей матрицы - должен получится вектор размером S
# e.	Результирующий вектор проходит через функцию:
# i.	Если last == False то функция - np.sin(x) 
# ii.	иначе np.maximum(x, 0)
# f.	Вернуть результирующий массив и рандомную матрицу сгенерированную в начале функции,
# g.	Для теста вызовите функцию 3 раза:
# i.	первый - длинна вектора 5, заполнен случайными числами. Размер слоя 10
# ii.	второй - на вход передайте вектор из предыдущего запуска. Размер слоя 10
# iii.	третий - на вход передайте вектор из второго запуска, размер слоя 5 и last = True. Значения результата переведите в проценты и выведите в консоль.


def fullnet(A, X, S, last=False):
    B = np.random.rand(X, S)
    C = A*B
    sums = (sum(i) for i in C)
    if not last:
        out = np.sin(sums)
    else:
        out = np.maximum(sums, 0)
    return out, B


fullnet()

# h.	Вы написали прототип прямого распространения полносвязной нейронной сети. 
