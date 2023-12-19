double = lambda x: x*2
print(double(5))

list_values = [1, 3, 4, 2, 6, 7, 5, 8, 9]
print(list(filter(lambda x: x % 2 == 0, list_values)))

s = ' a s d g  yghyjr ewrtg  w erfqwe'
print(list(filter(lambda x: not x == ' ', list(s))))


l = [1, 1.7, 'asdkfv', True, 5]
# isinstanse не работает для булевых типов
# print(list(filter(lambda x: isinstance(x, int), l) and not isinstance(x, int) and not isinstance(x, int)))

numbers = [1, 2, 3, 4, 5, 6]


def filter_num(in_num):
    return in_num % 2 == 0


print(list(filter(filter_num, numbers)))

