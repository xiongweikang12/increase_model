from functools import reduce
import math


class Test_data:
    point_set = [
        [5000, 0.04, (2, 10)],
        [7000, 0.04, (9, 1)],
        [3500, 0.095, (3, 6)],
        [3500, 0.095, (4, 7)],
        [5500, 0.095, (5, 10)]
    ]


def get_point_center(list1) -> list: #计算中心点 运量 比例 坐标
    x_1 = reduce(lambda x, y: x + y, [i[0] * i[1] * i[2][0] for i in list1])
    x_2 = reduce(lambda x, y: x + y, [i[0] * i[1] for i in list1])
    y_1 = reduce(lambda x, y: x + y, [i[0] * i[1] * i[2][1] for i in list1])
    y_2 = reduce(lambda x, y: x + y, [i[0] * i[1] for i in list1])
    return [x_1 / x_2, y_1 / y_2]


def equation_x_y(tuple_x_y,list_x_y):
    return math.sqrt((list_x_y[0]-tuple_x_y[0])**2+(list_x_y[1]-tuple_x_y[1])**2)

def repeat_point(list1,list_x_y)->list: #迭代公式
    x_1 = reduce(lambda x, y: x + y, [i[0] * i[1] * i[2][0]/equation_x_y(i[2],list_x_y) for i in list1])
    x_2 = reduce(lambda x, y: x + y, [i[0] * i[1]/equation_x_y(i[2],list_x_y) for i in list1])
    y_1 = reduce(lambda x, y: x + y, [i[0] * i[1] * i[2][1]/equation_x_y(i[2],list_x_y) for i in list1])
    y_2 = reduce(lambda x, y: x + y, [i[0] * i[1]/equation_x_y(i[2],list_x_y) for i in list1])
    return [x_1 / x_2, y_1 / y_2]

def iter_equation()->list: #迭代过程
    flag = 0
    container_consequence = [get_point_center(Test_data.point_set)]
    while True:
        if flag == 0:
            new_center = repeat_point(Test_data.point_set, get_point_center(Test_data.point_set))
            container_consequence.append(new_center)
            flag += 1
        else:
            if container_consequence[flag][0] != container_consequence[flag - 1][0]:
                new_center = repeat_point(Test_data.point_set, new_center)
                container_consequence.append(new_center)
                flag += 1

            else:
                break
            print(flag,new_center)
    return new_center


print(get_point_center(Test_data.point_set))
print(iter_equation())

