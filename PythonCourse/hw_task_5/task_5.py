import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# 1.	Создайте DataFrame с рандомными целыми числами от 1 до 10, размером 10х10.
#

df = pd.DataFrame(np.random.randint(1, 10, size=(10, 10)))

# 2.	В DataFrame из предыдущего задания добавьте индексы строк в виде латинских букв. Выведите на печать строку в которой все числа > 5, если такая есть
#
df.index = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
for i in range(len(df.index)):
    flag = True
    for j in range(len(df.columns)):
        if df.iloc[i, j] <= 5:
            flag = False
            break
    if flag:
        print(df.iloc[i, :])


# 3.	Создайте DataFrame с рандомными числами, размером 10х10.
# a.	добавьте индексы столбцов и строк в виде латинских букв
# b.	Выведите на в консоль
# i.	Размерность матрицы
# ii.	индексы столбцов
# iii.	среднее значение всех чисел матрицы
# iv.	запишите матрицу в csv

df3 = pd.DataFrame(np.random.randint(1, 10, size=(10, 10)))
df3.index = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
df3.columns = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
print('Размерность: ', len(df3.index), ' на ', len(df3.columns))
print('Индексы столбцов: ', df3.columns)
print('Индексы строк: ', df3.index)
print('Среднее: ', np.mean(df3.values))
df3.to_csv('data.csv')

# 4.	Создайте DataFrame из файла emojis.csv.
# a.	в столбце Rank указан рейтинг смайлов, отсортированный в порядке убывания частоты. (чем чаще использовался эмоджи тем ниже значение)
# b.	Выведите в консоль самую популярную подкатегорию эмоджи
emojis = pd.read_csv('emojis.csv')
print(emojis)
print(emojis.groupby(['Subcategory'])['Rank'].mean().sort_values().head(1))


# 5.	Создайте DataFrame из файла emojis.csv.
# a.	Получите количество созданных эмоджи за каждый год
# b.	Постройте график
print(emojis.groupby(['Year'])['Name'].count())
print(emojis.groupby(['Year'])['Name'].count().plot())
plt.show()