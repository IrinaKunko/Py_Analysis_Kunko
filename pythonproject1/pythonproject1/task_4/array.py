import numpy as np

a = np.array([1, 2, 3, 4], float)
print(type(a))

print(a[:2])
print(a[3])

a[0] = 10.1
print(a)

# Заполнение массива одинаковыми массивами
b = np.full(10, 1)
print(b)

# Два двоеточия -1 это шаг
b = a[::-1]
print(b)

x = np.zeros(10)
print(x)

x = np.arange(10, 20)
print(x)

x = np.ones(10)
print(x)

x = np.full(10, True)
print(x)

print(x.mean())
print(x.max())
print(x.min())

