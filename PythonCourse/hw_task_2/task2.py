# 1.	Имеется строка состоящая из слов. Напишите функцию которая возвращает строку убрав из нее стоп слова. Стоп слова находятся в списке:
# a.	[“Python”, “php”, “go”, “C”]

s = 'asdf hyhh Python wed   go eeeee ooJN ;sdc C'
blacklist = ['Python', 'php', 'go', 'C']

s = ' '.join(list(filter(lambda x: not x in blacklist, s.split())))
print(s)


# 2.	Имеется список, состоящий из чисел. 
# Напишите функцию которая принимает число и возвращает список состоящий
#  из элементов первого списка кратных входному параметру.

l = [3, 7, 6.9, 22, 54]


def func(a) -> list:
    global l
    return list(filter(lambda x: x % a == 0, l))


print(func(1))


# 3.	Напишите функцию, которая принимает любое количество не именованных
#  аргументов и возвращает кортеж состоящий из аргументов у которых тип данных str

def function(*args) -> tuple:
    return tuple(filter(lambda x: type(x) == str, args))


print(function(4, 'sdfg', True, 8.9, 'dddd', "asdsa"))


# 4.	Имеются два списка состоящие из произвольных элементов.
#  Напишите функцию которая возвращает пересечение списков 
# (элементы которые встречаются в и там и там)

l1 = [4, 'sdfg', True, 8.9, 'dddd', "asdsa", 'sdcawsd', [8]]
l2 = [False, True, 99, 4.9, 'sdcawsd', [8], 8.9, 'dddd']

def intersection(l1, l2):
    return list(filter(lambda x: x in l2, l1))

print(intersection(l1, l2))


# 5.	Лесенка.
# Лесенкой - условный набор кубиков, в котором каждый последующий слой содержит меньше кубиков, чем предыдущий. 

# Напишите функцию, вычисляющую число лесенок, которое можно построить из n кубиков. 
# -	Длина каждой ступени может отличаться.
# -	n - натуральное число в диапазоне от 1 до 100. 


def stairs(n):
    if n <= 2:
        return 1#1 или 2 кубика можно разложить только 1 способом
    out = 0
    i = 0
    while 2*i <= n:#Меняем i от 0 до половины n
        # Отделяем от кучи i кубиков и смотрим сколькими способами их можно разолжить:
        out += stairs(i)
        # Если отделили ровно половину, то убираем из подсчета случай, когда n раскладывается на два слоя одинаковой
        # ширины:
        if i * 2 == n:
            out -= 1
        i += 1
    return out


print("Число лесенок: ", stairs(100))

# 6.	Напишите декоратор который выводит исключение в случае если декорируемая функция
# возвращает тип данных отличный от int
# Напишите 2 тестовые декорируемые функции с произвольными данными.

def decorator(fn):
    def wrapper(*args, **kwargs):
        result = fn(*args, **kwargs)
        if type(result) != int:
            raise Exception('Функция не возвращает целочисленное значение')
        return result
    return wrapper    
        
@decorator
def example1(a, b) -> float:
    return a / b

@decorator
def example2(a, b) -> int:
    return a + b

# раскомментровать при просмотре 6 задания. Закомментировать при просмотре 7 задания
# print(example2(66, 55))
# print(example1(66,55.7))



# 7.	Напишите декоратор который запускает декорируемую функцию повторно,
#  в случае если произошло исключение при первом запуске.
# Напишите 2 тестовые декорируемые функции с произвольными данными.


def decorator2(fn):
    def wrapper(*args, **kwargs):
        try:
            result = fn(*args, **kwargs)
            if type(result) != int:
                raise Exception('Функция не возвращает целочисленное значение')
            return result
        except Exception as ex:
            print(ex)
            return fn(*args, **kwargs)
    return wrapper


decorator2(decorator)


@decorator2
def example3(a, b) -> float:
    return a / b

@decorator2
def example4(a, b) -> int:
    return a + b


print(example4(66, 55))
print(example3(66, 55.7))
