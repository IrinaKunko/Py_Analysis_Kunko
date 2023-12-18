from sklearn import svm
from sklearn.model_selection import train_test_split
import numpy as np
import pandas as pd

def f(x):
    if x == '1st':
        return 1
    elif x == '2nd':
        return 2
    elif x == '3rd':
        return 3
    else:
        return 4

# 1.	Создайте класс для лиц, с фото и видео.
# a.	В классе должны быть следующие методы:
# i.	Метод предобработки фото, видео (путь получаем при инициализации) - метод загружает фото, или видео
# ii.	Метод детекта
# iii.	Метод инференса
# iv.	Метод отображения
# b.	Также сделайте возможность изменять размеры отображаемого фото, видео, при вызове метода.
#


# 2.	Сделайте предсказание выживаемости пассажира, на основе датасета “titanic.csv”, с использованием библиотеки sklearn. Сделайте тестовый проход на 10 пассажирах.

dataset = pd.read_csv('titanic.csv')
data = dataset[['Age', 'SexCode', 'PClass']]

data['PClass'] = data['PClass'].apply(f)
m = data['Age'].mean(skipna=True)
data.loc[data['Age'].isna(), 'Age'] = m

model = svm.SVC()
X_train, X_test, y_train, y_test = train_test_split(data, dataset['Survived'], test_size=0.5, shuffle=True)
model.fit(X_train, y_train)
predicted = model.predict(X_test[0:10])

y_test = y_test[:10]
print('Предсказание')
print(predicted)
print('\nПравильные ответы')
print(y_test)