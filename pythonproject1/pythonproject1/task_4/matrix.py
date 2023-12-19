import numpy as np
import random

a = np.array([[1, 2, 3], [4, 5, 6]], float)

print(a[0, 1])
print(a[1, 1])

print(a.shape)
print(a.dtype)

b = np.array(range(10), float)
b_reshape = b.reshape((2, 5))

print(b)
print(b_reshape)

print(b.tolist())

def func(*args):
    l = []
    for i in args:
        if type(i) == int:
            l.append(i)

    return np.sort(np.array(l, int))


print(func(3, 'rfvge', 9, 100, 5., True, False, 3, 11, 35))


def f(x, y):
    l =[random.randint(1, 101) for i in range(x*y)]
    b = np.array(l, int)
    matrix = b.reshape(x, y)
    return b.min(), b.max(), b.mean()


def task_2(x, y):
    result = np.random.random(x, y)
    return result.mean(), result.min(), result.max()


print(f(3, 6))


a = np.array(range(6), float).reshape((2, 3))
print(a)
print('\n')
# Транспонирование
b = a.transpose()
print(b)

matrix = np.array([[1, 2, 3], [4, 5, 6]], float)
print(matrix)
print('\n')
print(matrix.flatten())

a = np.array([1, 2], float)
b = np.array([3, 4, 5, 6], float)
c = np.array([7, 8, 9], float)

print(np.concatenate((a, b, c)))

a = np.array([[1, 2], [3, 4]], float)
b = np.array([[5, 6], [7, 8]], float)
print(np.concatenate((a, b)))
print(np.concatenate((a, b), axis=1))


app = np.array(range(10), int)
print(app)
app_new = np.append(app, [111, 444])
print(app_new)

a = np.array([[1, 2], [3, 4]], int)
print(app)
app_new = np.append(app, np.array([[10, 11]]), axis=1)
print(app_new)
