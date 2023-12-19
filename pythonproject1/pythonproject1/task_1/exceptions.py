try:
    print(a)
except:
    print("Переменная 'а' не определена")

try:
    print(a)
except Exception as ex:
    print('Переменная "а" не определена')
    print(ex)


try:
    k = 1/0
    print(k)
except ZeroDivisionError:
    k=0
    print('app close')
finally:
    print('finally')


# Создать свое исключение
x =-1
if x<0:
    raise Exception('число меньше нуля')