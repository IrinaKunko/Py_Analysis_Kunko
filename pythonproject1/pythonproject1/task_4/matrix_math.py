import numpy as np

a = np.array([1, 2, 3], int)
b = np.array([5, 2, 6], int)
print(a + b)
print(a*b)
print(a/b)
print(a**b)

a = np.array([4, 9, 16, 25], int)
print(np.sqrt(a))

array_for = np.array(range(15), int)
for i in array_for:
    print(i)

print('\nМатрица')
array_for_m = np.array(range(15), int).reshape(3, 5)
for i in array_for_m:
    print(i)

matrix_a = np.array([[1, 2], [3, 4]], int)
matrix_b = np.array([7, 8], int)
print(np.dot(matrix_a, matrix_b))