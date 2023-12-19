from sklearn import datasets, svm
from sklearn.model_selection import train_test_split
import numpy as np

np.set_printoptions(precision=2, floatmode='fixed', suppress=True)
dataset = np.genfromtxt('water_potability.csv', delimiter=',', dtype=float)
dataset = dataset[1:]

for i in range(len(dataset[0])-1):
    dataset = dataset[~np.isnan(dataset[:, i])]

X_train, _, y_train, _ = train_test_split(dataset, dataset[:,-1], shuffle=True)


model = svm.SVC(gamma=3)
model.fit(X_train, y_train)
predicted=model.predict(X_train[0:5])

y_test = y_train[:5]
print('Предсказани сети')
print(predicted)
print('Правильные ответы')
print(y_test)