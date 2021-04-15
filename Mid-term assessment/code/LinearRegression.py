import numpy as np


class LinearRegression:

    def __init__(self, alpha=0.1, times=1000):
        self.alpha = alpha
        self.times = times

    def mix(self, _x):
        """
        加上一列x0=1变成增广矩阵
        :param _x: 特征矩阵_x
        :return: 增广矩阵_X
        """
        x0 = np.ones([_x.shape[0], 1])  # 新增的全为1的列向量
        _X = np.concatenate([x0, _x], axis=1)  # 将x0这一列加到_x左边
        return _X

    def Gradient_fit(self, _x, _y):
        """
        负责拟合，传回一个theta
        :param _x: 未经处理的特征矩阵_x
        :param _y: 输出y，是一个列向量
        :return: theta， 一个列向量
        """

        _X = self.mix(_x)
        m = _X.shape[0]  # m行
        n = _X.shape[1]  # n列
        theta = np.ones([n, 1])

        # 梯度下降过程
        for j in range(int(self.times)):
            theta = theta - (self.alpha / m) * np.dot(_X.T, (np.dot(_X, theta) - _y))
        self.theta = theta

    def Equation_fit(self, _x, _y):
        """
        正规方程法
        :param _x: 未经处理的特征矩阵_x
        :param _y: 输出列向量
        :return:  theta
        """
        _X = self.mix(_x)
        theta = np.dot(np.linalg.inv(np.dot(_X.T, _X)), np.dot(_X.T))
        self.theta = theta

    def predict(self, x_test):
        _X = self.mix(x_test)
        y = np.dot((_X, self.theta))
        return y