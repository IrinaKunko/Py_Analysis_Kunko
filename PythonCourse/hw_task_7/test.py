import numpy as np

def f(*args):
    res =[]
    for i in args:
        if type(i) == int:
            res.append(i)
    if len(res) == 0:
        raise Exception('Error')
    res.sort()
    return res

print(f(1, 'ffe', False, 5.4))

print(max('a b c d'))

a = np.full(shape=20, fill_value=394, dtype=int)
print(a)

my_list = [45,7.8, 'dcsa','s']
print(list(map(lambda x: str, my_list)))

x = np.random.randint(0, 100, size=20)
print(x)
for i in range(len(x)):
    if x[i] <= 20 and x[i] != 0:
        x[i] = x[i]* 2
print(x)