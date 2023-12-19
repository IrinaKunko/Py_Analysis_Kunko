import random
import numpy as np
import matplotlib.pyplot as plt

class Neural:
    def __init__(self, path_dataset = 'water_potability.csv', input_dim=9, output_dim=2, h_dim=25, alpha=0.00001, num_epochs=1000, batch_size=30):
        self.path_dataset = path_dataset
        self.input_dim = input_dim
        self.output_dim = output_dim
        self.h_dim = h_dim
        self.alpha = alpha
        self.num_epochs = num_epochs
        self.batch_size = batch_size
        self.dataset = []
        self.nn_weights = {}

    @staticmethod
    def softmax_batch(self, t):
        out = np.exp(t)
        return out/np.sum(out, axis=1, keepdims=True)

    @staticmethod
    def sparse_cross_entropy_batch(z, y):
        return -np.log(np.array([z[j, y[j]] for j in range(len(y))]))

    @staticmethod
    def to_full_batch(y, num_classes):
        # Возращает карту правильных ответов
        '''

        :param y: правильные ответы
        :param num_classes: число выходных параметров
        :return:
        '''
        y_full = np.zeros((len(y), num_classes))
        for j, yj in enumerate(y):
            y_full[j, yj] = 1
        return y_full

    @staticmethod
    def relu(t):
        '''
        Функция активации
        :param t: матрица значений внутри нейронов
        :return:
        '''
        return np.maximum(t, 0)

    @staticmethod
    def relu_deriv(t):
        return (t>=0).astype(float)

    def data_preparation(self):
        dataset = np.genfromtxt(self.path_dataset, delimiter=',', dtype=float)
        dataset = dataset[1:,:]

        for i in range(len(dataset[0] - 1)):
            dataset = dataset[~np.isnan(dataset[:, i])]
        dataset[:, 2] = dataset[:, 2]*0.001
        dataset[:, 4] = dataset[:, 4]*0.01
        dataset[:, 5] = dataset[:, 5] * 0.01
        np.around(dataset, 2)

        target = dataset[:, -1]
        dataset = dataset[:, :8]
        if target.shape[0] != dataset.shape[0]:
            raise Exception('Число строк не совпадает')
        self.dataset = [(dataset[i][None, ...], int(target[i])) for i in range(len(target))]

    def inference(self, x):
        if not self.nn_weights:
            raise Exception('Сеть не обучена')
        t1 = x @ self.nn_weights['W1'] + self.nn_weights['b1']
        h1 = self.relu(t1)
        t2 = h1 @ self.nn_weights['W2'] + self.nn_weights['b2']
        z = self.softmax_batch(t2)

        return np.argmax(z)

    def calc_accuracy(self):
        correct = 0
        for x, y in self.dataset:
            z = self.inference(x)
            y_pred = self.inference(x)
            # y_pred = np.argmax(z)
            if y_pred == y:
                correct +=1
        return correct/len(self.dataset)

    def trainning(self):
        self.data_preparation()
        self.nn_weights['W1'] = np.random.rand(self.input_dim, self.h_dim)
        self.nn_weights['b1'] = np.random.rand(1, self.h_dim)
        self.nn_weights['W2'] = np.random.rand(self.h_dim, self.output_dim)
        self.nn_weights['b2'] = np.random.rand(1, self.output_dim)

        self.nn_weights['W1'] = (self.nn_weights['W1'] - 0.5)*2 * np.sqrt(1/self.input_dim)
        self.nn_weights['b1'] = (self.nn_weights['b1'] - 0.5) * 2 * np.sqrt(1 / self.input_dim)
        self.nn_weights['W2'] = (self.nn_weights['W2'] - 0.5) * 2 * np.sqrt(1 / self.h_dim)
        self.nn_weights['b2'] = (self.nn_weights['b2'] - 0.5) * 2 * np.sqrt(1 / self.h_dim)

        loss_arr = []

        for ep in range(self.num_epochs):
            random.shuffle(self.dataset)
            for i in range(len(self.dataset) // self.batch_size):
                batch_x, batch_y = zip(*self.dataset[i * self.batch_size: i * self.batch_size + self.batch_size])
                x=np.concatenate(batch_x, axis = 0)
                y = np.array(batch_y)

        t1 = x @ self.nn_weights['W1'] + self.nn_weights['b1']
        h1 = self.relu(t1)
        t2 = h1 @ self.nn_weights['W2'] + self.nn_weights['b2']
        z = self.softmax_batch(t2)
        E = np.sum(self.sparse_cross_entropy_batch(z, y))

        y_full = self.to_full_batch(y, self.output_dim)
        dE_dt2 = z - y_full
        dE_dW2 = h1.T @ dE_dt2
        dE_db2 = np.sum(dE_dt2, axis=0, keepdims=True)
        dE_dh1 = dE_dt2 @ self.nn_weights['W2'].T
        dE_dt1 = dE_dh1 * self.relu_deriv(t1)
        dE_dW1 = x.T @ dE_dt1
        dE_db1 = np.sum(dE_dt1, axis=0, keepdims=True)

        self.nn_weights['W1'] = self.nn_weights['W1'] - self.alpha * dE_dW1
        self.nn_weights['b1'] = self.nn_weights['b1'] - self.alpha * dE_db1
        self.nn_weights['W2'] = self.nn_weights['W2'] - self.alpha * dE_dW2
        self.nn_weights['b2'] = self.nn_weights['b2'] - self.alpha * dE_db2

        loss_arr.append(E)

        plt.plot(loss_arr)
        plt.show()