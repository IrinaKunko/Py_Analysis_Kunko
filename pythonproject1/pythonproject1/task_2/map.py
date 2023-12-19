def square(number):
    return number ** 2


numbers = [1, 2, 3, 4, 5]
print(list(map(square, numbers)))


str_nums = ['4', '5', '6']
print(list(map(int, str_nums)))


s = 'Mapping'
print(list(map(lambda x: x.upper(), s)))

string_upper = 'Mapping'
print(''.join(list(map(lambda x: x.upper(), string_upper))))

s = ['sad', 'weqwd', 's', 'eafwe',  'gr', 'awedwqdqwedwe']
print(list(map(len, s)))

