import numpy as np
import matplotlib.pyplot as plt


# 由于逻辑回归推导出来的偏导项跟多元线性回归一样...其实就是套了个sigmoid的壳
class LogisticRegression:

    def __init__(self, alpha=0.1, times=1000):
        self.alpha = alpha
        self.times = times

    def sigmoid(self, z):
        z.astype(float)
        return 1 / (1+np.exp(-z))  # sigmoid函数

    def mix(self, _x):
        """
        加上一列x0=1变成增广矩阵
        :param _x: 特征矩阵_x
        :return: 增广矩阵_X
        """
        x0 = np.ones([_x.shape[0], 1])  # 新增的全为1的列向量
        _X = np.concatenate([x0, _x], axis=1)  # 将x0这一列加到_x左边
        return _X

    def fit(self, _x, _y):
        """
        负责拟合，传回一个theta
        :param _x: 未经处理的特征矩阵_x
        :param _y: 真实值，是一个列向量,0,1,表示有无
        :return: theta， 一个列向量
        """
        _x = np.array(_x.astype(float))
        _y = np.array(_y).reshape(-1, 1)
        _X = self.mix(_x)
        m = _X.shape[0]  # m行
        n = _X.shape[1]  # n列
        theta = np.ones([n, 1])

        #  梯度下降过程
        for j in range(int(self.times)):
            theta = theta - (self.alpha/m)*np.dot(_X.T, (self.sigmoid( np.dot(_X, theta)) - _y))
        self.theta = theta

    def predict(self, x_test):
        _X = self.mix(x_test)
        y = self.sigmoid(np.dot(_X, self.theta))
        y[y >= 0.5] = 1
        y[y < 0.5] = 0
        return y
