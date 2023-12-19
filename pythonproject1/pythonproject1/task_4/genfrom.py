import numpy as np
import random
data = np.genfromtxt('data.csv', delimiter=',')
print(data)

def multi(shape1, shape2):
    if shape1[1] == shape2[0]:
        matr1 = np.ones(shape1[0]*shape1[1]).reshape(shape1)
        matr2 = np.ones(shape2[0] * shape2[1]).reshape(shape2)
        return np.dot(matr1, matr2)
    else:
        raise Exception('Нельзя перемножить')


print(multi((3, 4), (4, 5)))
# print(multi((3, 4), (3, 4)))

def create_array():
    a = np.array([random.randint(0, 15) for i in range(15)], int)
    for i in range(a.size):
        if 3 < a[i] < 8: a[i] = 0 - a[i]
    return a


print(create_array())