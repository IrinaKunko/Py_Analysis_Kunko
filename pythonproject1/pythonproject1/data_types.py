age = 21
print("Возраст: ", age)

count = 15
print('Количество: ', count)


print(6+2)
print(6-2)
print(6*2)
print(6/2)
print(6**2)
print(7//2) ##целое число от деления
print(6**2) ##возведение в степень


s = 'это строка'
g = '''Многострочная
 строка'''
print(s + '\n')
print(g + '\n')


print('Сложение' + 'строк')
print('Auto'*3)

a = 'Auto'
print(a[-1])
print(a[0:2]) #вывод первого и второго эелемента строки
print(a.index('t'))


'''Списки'''
a = [5, 10, 15, 29, 20, 35 ]
b = ['str', 1, [0, 1, 2], 1.5]
test_list = ['один', 'два', 'три']

# Изменение элемента
for elem in test_list:
    print(elem)
print(len(test_list))
test_list.append('шесть')
print(test_list)


'''ЛОГИЧЕСКИЙ ТИП ДАННЫХ'''
print(10>9)
print(10 == 9)
a = True
if a:
    print('a = True')
else:
    print('a != False')

