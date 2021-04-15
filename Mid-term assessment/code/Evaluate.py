import numpy as np
import pandas as pd
def accuracy(y_test, y_predict):
    y_test = np.array(y_test)
    y_predict = np.array(y_predict)
    num_correct = (y_test.reshape(-1, 1) == y_predict.reshape(-1, 1)).sum()
    return num_correct/len(y_predict)


def mse(y_true, y_predict):
    loss = ((y_true-y_predict)**2).sum()
    return loss/len(y_predict)


def rsquare(y_true, y_predict):
    """
    R方评价函数，越趋近于1，模型越好
    :param y_true: 真实值
    :param y_predict: 预测值
    :return: a num
    """
    loss_predict = ((y_true-y_predict)**2).sum()
    loss_bar = ((y_true-y_true.mean())**2).sum()
    judge = 1-(loss_predict/loss_bar)
    return judge





