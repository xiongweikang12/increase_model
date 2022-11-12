
from functools import reduce
from test_homework_gravity import *

class array_l:

    def __init__(self, length: int, array_k, future_data_ul, future_data_v_):
        """
        :param length: 长度
        :param array_k: 数据本身
        :param future_data_ul: 未来的u立 发生
        :param future_data_v_: 未来的v 吸引
        """
        self.len = length
        self.future_data_ul = future_data_ul
        self.future_data_v_ = future_data_v_
        self.list = np.array(array_k)
        self.sum_u = np.sum(self.list, axis=1)
        self.sum_v = np.sum(self.list, axis=0)
        self.u_o = self.future_data_ul / self.sum_u
        self.v_d = self.future_data_v_ / self.sum_v
        self.future_T = sum(future_data_ul)
        self.T = sum(self.sum_u)

    def new_object_data(self, function_model):
        """

        :param function_model: 处理方法，通过传入不同的fx实现多态
        :return:
        """

        return_data = self.list
        basic_data = self.list
        Oi = np.sum(basic_data, axis=1)
        Di = np.sum(basic_data, axis=0)

        for i in range(len(self.list)):
            for j in range(len(self.list)):
                return_data[i][j] *= \
                    function_model(self.u_o[i], self.v_d[j], basic_data,
                                   self.u_o, self.v_d, i, j,
                                   self.future_T, self.T, flag)

                # print(return_data[i][j])
                # print(average(self.u_o[i], self.v_d[j]))
        print("{}:{}:{}\n".format(getattr(function_model, "__name__"), flag, return_data))
        return return_data


"""
ui: 将来发生交通量
vi: 将来吸引交通量
X: 将来生成交通量
Oi:原来的发生交通量
Di:原来的吸引交通量

"""

"""
qij (k)=qij (k-1) *average(increase_happen(k-1)+increase_strike(k-1))

迭代终点: 1.1-b<increase_happen(ui,oi)<1+b
        2.1-b<increase_strike(vi,di)<1+b

[v1(1)sum ,v2(1),v3(1)]
[ui1(1)sum ,ui2(1),ui3(1)]


"""

def new_int(array_float):

    copy_test_out=[]
    len_1=len(array_float[0])
    for i in range(len_1):
        copy_test_in = []
        for j in range(len_1):
            copy_test_in.append(int(array_float[i][j]/100))
        copy_test_out.append(copy_test_in)
    return copy_test_out


def increase_happen(ui, oi) -> float:
    return ui / oi


def increase_strike(vi, di) -> float:
    return vi / di


# 平均增长系数
def average(Fo, Fd, basic_data,
            u_o_all, v_d_all, i, j,
            futrue_T=0, T=0, flag=0, ) -> float:
    return (Fo + Fd) / 2


# 底特律法
def Detroit(Fo, Fd, basic_data,
            u_o_all, v_d_all, i, j
            , frtrueT=0, T=0, flag=0) -> float:
    return Fo * Fd * T / frtrueT


# 佛尼斯法
def furness(Fo, Fd, basic_data,
            u_o_all, v_d_all, i, j,
            frtrueT=0, T=0, flag=0) -> float:
    return [Fo, Fd][(flag - 1) % 2]


def fratar(Fo, Fd, basic_data,
           u_o_all, v_d_all, i, j,
           frtrueT=0, T=0, flag=0) -> float:
    Oi = np.sum(basic_data, axis=1)
    Di = np.sum(basic_data, axis=0)
    if i == 0 and j == 0:
        li = Oi[0] / basic_data[0][0] * v_d_all[0]
        lj = Di[0] / basic_data[0][0] * u_o_all[0]
    elif i == 0 and j != 0:
        li = Oi[i] / reduce(lambda x, y: x + y, [basic_data[i][k] * v_d_all[k] for k in range(j)])
        lj = Di[j] / basic_data[0][j] * u_o_all[j]
    elif i != 0 and j == 0:
        li = Oi[0] / basic_data[i][0] * v_d_all[0]
        lj = Di[j] / reduce(lambda x, y: x + y, [basic_data[kk][j] * u_o_all[j] for kk in range(i)])
    else:
        li = Oi[i] / reduce(lambda x, y: x + y, [basic_data[i][k] * v_d_all[k] for k in range(j)])
        lj = Di[j] / reduce(lambda x, y: x + y, [basic_data[kk][j] * u_o_all[j] for kk in range(i)])

    return Fo * Fd * (li + lj) / 2


def check_1(i,check_num=0.03):
    return 1 - check_num< i < 1 + check_num


def if_yes(list1):
    return len(list(filter(check_1, list1))) == len(list1)


def start_iter(funtion_model,check_num=0.03):
    global flag, new_object_1
    while True:
        if flag == 1:
            new_object = a
        else:
            new_object = new_object_1

        if if_yes(new_object.u_o):
            if if_yes(new_object.v_d) or flag > 10:
                return new_object_1
            else:
                next_data = new_object.new_object_data(funtion_model)
                # 多态的实现
        else:
            next_data = new_object.new_object_data(funtion_model)
            flag += 1
        new_object_1 = array_l(new_object.len, next_data, new_object.future_data_ul, new_object.future_data_v_)


def return_object_by_data(list1, list2, list3):
    # array_l(3, Test.Test_data, Test.ui_len, Test.vi_len)
    return array_l(3, list1, list2, list3)


# a = return_object_by_data(Test.Test_data, Test.ui_len, Test.vi_len)
a = return_object_by_data(get_new_Od(Test(),TEST_DATA_TIME.c_ij_future), Test.ui_len, Test.vi_len)
flag = 1

# start_iter(furness)
# start_iter(average)
new_data=start_iter(average)
print(new_data.list)
print(type(new_data.list))
# start_iter(fratar)
#TODO 绘图Od
from TUMU.experiment.experment_3.exper import draw_OD
position=[(0,0) for j in range(12)]
label=[str(i) for i in range(1,13)]

print(new_int(new_data.list))
j = draw_OD(label=label,position=position,array=(new_int(new_data.list)) ,title="交通分布", model='pot')
j.show()
# ll = draw_OD(label=label, array=array_1, model='line')
# ll.show()