from sklearn import datasets, svm
from sklearn.model_selection import train_test_split

iris = datasets.load_iris()
data = iris.data

model = svm.SVC()
X_train, X_test, y_train, y_test=train_test_split(data, iris.target, test_size=0.3, shuffle=True)
model.fit(X_train, y_train)
predicted=model.predict(X_test[0:3])

y_test = y_test[:3]
print('Предсказани сети')
print(predicted)
print('Правильные ответы')
print(y_test)