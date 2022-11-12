import math

from class_all_testdata import Test
from class_all_testdata import Time_data
import numpy as np
from test_homework_login import test_


class TEST_DATA_TIME:
    # c_ij_now = [[8.0, 17.0,22.0], [17.0, 15.0, 23.0], [22.0, 3.0, 7.0]]
    # c_ij_future=[[4.0,9.0,11.0],[9.0,8.0,12.0],[11.0,12.0,4.0]]
    c_ij_now =Time_data.c_ij_now
    c_ij_future =Time_data.c_ij_future

def cal_all_data(i: int, j: int, test: Test):
    return [
        (i, j), test.Test_data[i][j],
        test.Oi[i], test.Di[j], test.Oi[i] * test.Di[j],
        TEST_DATA_TIME.c_ij_now[i][j], np.log(test.Test_data[i][j]),
        np.log(test.Oi[i] * test.Di[j]), np.log(TEST_DATA_TIME.c_ij_now[i][j])
    ]

def cal_data_profit(test: Test):
    contain_all_data = []
    for i in range(test.data_len):
        for j in range(test.data_len):
            contain_all_data.append(cal_all_data(i, j, test))
    return [(k[-3], k[-2], k[-1]) for k in contain_all_data]


def return_define_const_fit(target=True): #拟合结果,需根据目的函数回归形式去设定矩阵
    """
    :return:
    target ->true 表示一个参数为一
    """
    Y=[]
    X=[]
    if target:
        flag=-1
    else:
        flag=0
    for i in cal_data_profit(Test()):
        Y.append(i[0]+flag*i[1]) #y
        if flag==-1:
            X.append([1,i[-1]]) # a0 ,a2
        else:
            X.append([1,i[1],i[-1]])
    X=np.array(X)
    Y=np.array(Y)
    print(np.dot(np.linalg.inv(np.dot(X.T,X)),X.T).dot(Y))
    return np.dot(np.linalg.inv(np.dot(X.T,X)),X.T).dot(Y)



def get_new_fit(target=True):
    temp = return_define_const_fit(target)
    if len(temp)==2:
        container_return=[np.exp(temp[0]), -temp[-1]]
    else:
        container_return=(np.exp(temp[0]), temp[1], -temp[-1])
        print(container_return)
    return container_return


def get_new_Od(test1: Test, cij,target=True) -> list:
    container_copy = test1.Test_data
    get_new_fit1=get_new_fit(target)
    for i in range(test1.data_len):
        for j in range(test1.data_len):
            temp1=get_new_fit1[0]
            temp2=(test1.ui_len[i]*test1.vi_len[j]) #将来的OI 和DJ
            temp3=math.pow(cij[i][j], get_new_fit1[-1])
            container_copy[i][j]=temp1*temp2/temp3
    print(container_copy)
    return container_copy
