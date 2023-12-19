from sklearn import datasets, svm
from sklearn.model_selection import train_test_split
import numpy as np

dataset = np.genfromtxt('data.csv', delimiter=',', dtype=float)


X_train, X_test, y_train, y_test=train_test_split(dataset, dataset[:,-1], shuffle=False)

model = svm.SVC()
model.fit(X_train, y_train)
predicted=model.predict(X_test[0:5])

y_test = y_test[:5]
print('Предсказани сети')
print(predicted)
print('Правильные ответы')
print(y_test)