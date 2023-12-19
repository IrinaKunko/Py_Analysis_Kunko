from sklearn import datasets, svm
from sklearn.model_selection import train_test_split

digits = datasets.load_digits()

n_samples = len(digits.images)
data = digits.images.reshape((n_samples, -1))

model = svm.SVC()
X_train, X_test, y_train, y_test=train_test_split(data, digits.target, test_size=0.5, shuffle=False)
model.fit(X_train, y_train)
predicted=model.predict(X_test[0:5])

y_test = y_test[:5]
print('Предсказани сети')
print(predicted)
print('Правильные ответы')
print(y_test)