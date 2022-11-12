import numpy as np
from functools import reduce
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from sklearn.linear_model import LinearRegression


class TestData:
    list_data = [(59159, 28720), (60909, 30625), (62554, 32177), (64172, 33690), (65696, 34974), (67206, 36250)]


x = [i[0] for i in TestData.list_data]
y = [i[1] for i in TestData.list_data]


def get_polyfit(deg1=1):
    ploy = np.polyfit(x, y, deg=deg1)
    ploy1 = np.poly1d(ploy)
    print(ploy1)


def mean_1(list1):
    len_1 = len(list1)
    sum_1 = reduce(lambda x1, y1: x1 + y1, list1)
    return sum_1 / len_1


def get_R():
    p1 = x2 = y2 = 0.0
    # 计算平均值
    x_ = mean_1(x)
    y_ = mean_1(y)
    # 循环读取每个值，计算对应值的累和
    for i in range(len(x)):
        p1 += (x[i] - x_) * (y[i] - y_)
        x2 += (x[i] - x_) ** 2
        y2 += (y[i] - y_) ** 2
    # print(p1,x2,y2)
    # 计算相关系数
    r = p1 / ((x2 ** 0.5) * (y2 ** 0.5))
    print(r)


# get_R()
# get_polyfit()


import pandas as pd


def test_(x,y):
    """
    df = pd.read_excel('客户价值数据表.xlsx')

    X = df[['历史贷款金额', '贷款次数', '学历', '月收入', '性别']]
    Y = df['客户价值']

    """
    model = LinearRegression()
    model.fit(x, y)

    return model.coef_
