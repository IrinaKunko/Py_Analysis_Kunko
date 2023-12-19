def main(a, b):
    return a + b


main(1, 2)
print(main(23, 69))
result_main = main(23, 89)


def arg(a, b, c=2, d=3):
    return a+b+c+d

print(arg(1, 1, 1, 1))
print(arg(1, 1))
# будет ошибка
# print(arg(1, 1, '1', 1))


def range_arg(a, b, c, d):
    return a + ' ' + b + ' ' + c + ' ' + d


print(range_arg('1', '2', '3', '4'))
print(range_arg('1', '2', d='3', c='4'))


def square(a):
    return 4 * a, a ** 2


print(square(3))


# ags может принять только неименованные аргументы
def add(*args):
    value = 0
    for item in args:
        if isinstance(item, (int, float)):
            value += item
    return value


total = add(1, 'function', 2, 3, 4, 'Python', 5.0, 'kwargs')
print("Total:", total)


def print_kwargs(a, **kwargs):
    print(kwargs)


print_kwargs(kone='One', ktwo=2, kthree=3)