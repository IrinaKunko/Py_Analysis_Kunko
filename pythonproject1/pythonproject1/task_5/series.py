import pandas as pd

my_series = pd.Series([2, 3, 4, 5])

print(my_series)
print(my_series[3])

my_series_step_2 = pd.Series([1, 2, 3, 4, 5], index=['a', 'b', 'c', 'd', 'e'])

my_series_step_3 = pd.Series({'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5})

print(my_series_step_2[['a', 'b', 'c']])
my_series_step_2[['a', 'b', 'c']] = 10
print(my_series_step_2)

my_series_step_3 = pd.Series([1, 0, 2, -4, 3, 3.5, 4, 5, -7])
# Условие на ключ
print(my_series_step_3[my_series_step_3 >= 3])
# print(my_series_step_3[my_series_step_3])

print(my_series_step_3.values)
print(my_series_step_3.index)
print(my_series_step_3.name)

my_series_step_3.index = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']


def f(l1, l2):
    if len(l2) == len(l1):
        return pd.Series(l1, index=l2)
    else:
        raise Exception('Второй список не может быть индексами первого')


print(f([1, 2, 3], ['a', 'b', 'c']))
# print(f([1, 2, 3], ['a', 'b']))

# Создать series только из элементов 'day_1', 'day_2', 'day_3'
d = {'day_1': 300, 'day_2': 0,'day_3': 400,'day_4': 350}
s = pd.Series(d, index=['day_1', 'day_2', 'day_3'])
print(s[s != 0])