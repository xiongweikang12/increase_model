from test_trans_assignments_base import short_path
import numpy as np



def change_list_mat(list_1):
    #[(1,4,300)...]
    """
    :param list_1: 将[(start,end,flow)...]的列表转换成相应的对称矩阵，根据索引填充
    :return: 填充完毕的矩阵
    """
    size_list=len(list_1)
    mat_1=np.zeros((size_list,size_list))
    for i in list_1:
        mat_1[i[0]-1][i[1]-1]=i[2]
        mat_1[i[1]-1][i[0]-1]=i[2]

    return mat_1

def change_list_all_mat(list_1,size):
    """
    :param list_1: 将[(start,end,catipty)....]（这个为算法接收的数据类型形式）转换成图的邻接矩阵
    :param size: 邻接矩阵大小
    :return: 转换完的邻接矩阵
    """
    mat_1=np.zeros((size,size))
    for i in list_1:
        mat_1[i[0]-1][i[1]-1]=i[2]
    return mat_1

def mat_exchange_list(mat_1):
    """
    :param mat_1:被处理的邻接矩阵
    :return: 转换成[(start,end,flow)...]算法能接收的形式输出
    """

    size=len(mat_1)
    container=[]
    for i in range(size):
        for j in range(size):
            if(mat_1[i][j]==0):
                continue
            else:
                container.append((i+1,j+1,mat_1[i][j]))
    print(mat_exchange_list.__name__+": \t")
    return container

def grahp_extent(list1):
    """
    :param list1:
    :return:扩大为对称，双向
    """
    list_xechange=[(i[1],i[0],i[2]) for i in list1]
    for j in list_xechange:
        list1.append(j)
    return list1


def get_max(list):
    max_=list[0][0]
    for i in list:
        if max_<=i[0]:
            max_=i[0]
        elif max_<=i[1]:
            max_=i[1]
        else:
            continue
    return max_





class string_data:

    def __init__(self,init_string):
        self.string_data=init_string

    def new_string_data(self,list_new):
        self.string_data=list_new





class graph_string:

    def __init__(self,OD_string:list,list_q:list,string_path_pow:string_data):
        #导入od一般为对称
        """

        :param OD_string: 流量表
        :param list_q: 参数Q
        :param string_path_pow: 最短路径的边权数
        """
        self.OD_string=OD_string
        self.string_Q=list_q
        self.string_path_pow=string_path_pow.string_data
        self.size_=get_max(self.string_path_pow)
        self.string_chart=np.zeros((self.size_,self.size_))

    def new_string_path_pow(self):
        return mat_exchange_list(self.string_path_pow)


    def change_string_one(self):

        def start_assignment():
            #单方向的表示从start->end
            for i in self.OD_string:
                # 根据流量表计算对应的最小路径
                short_path_data = short_path(i[0], i[1], self.string_path_pow)
                for j in short_path_data:
                    self.string_chart[j[0] - 1][j[1] - 1] = self.string_chart[j[0] - 1][j[1] - 1] + i[
                        2]



        start_assignment()


    def change_string_iter(self,pop_assignment):

        def start_assignment():
            for i in self.OD_string:
                # 根据流量表计算对应的最小路径
                short_path_data = short_path(i[0], i[1], self.string_path_pow)
                for j in short_path_data:
                    self.string_chart[j[0] - 1][j[1] - 1] = self.string_chart[j[0] - 1][j[1] - 1] + i[
                        2]*pop_assignment



        start_assignment()
        # 将OD_string分配过调整
        print(self.string_chart)
        mat_temp = change_list_all_mat(self.OD_string,self.size_)
        self.OD_string = mat_exchange_list(mat_temp)

        # 产生新的路径表
        mat_temp_listq = change_list_all_mat(self.string_Q,self.size_)
        size_mat = self.size_
        self.string_Q=mat_temp_listq
        self.string_path_pow=change_list_all_mat(self.string_path_pow,self.size_)
        for k in range(size_mat):
            for kk in range(size_mat):
                if self.string_Q[k][kk] == 0:
                    continue
                else:
                    self.string_path_pow[k][kk] = self.string_path_pow[k][kk]+\
                    self.string_chart[k][kk] * self.string_Q[k][kk]

        # 形成新的路径表
        self.string_path_pow=mat_exchange_list(self.string_path_pow)
        print(self.string_path_pow)
        start_assignment()


        #TODO 最短路径选择的是start->end所以对于流量来说就是一个方向的,
        # 其对称的流量相加，才能形成正确的结果


    def show_string_chart(self):
        print("{}:\n{}".format(self.show_string_chart.__name__,self.string_chart))
        return self.string_chart

    def get_listtype_string_char(self):
        temp=self.string_chart
        return mat_exchange_list(temp)

    def get_string_chart_doubleaction(self):

        #TODO 要保证其在start_assignment后调用才有意义
        # 将单向流量扩展成双向流量

        temp_string_chart_mat=self.string_chart #mat
        temp_string_chart_list=self.get_listtype_string_char()
        for i in temp_string_chart_list:
            if(temp_string_chart_mat[i[0]-1][i[1]-1]==temp_string_chart_mat[i[1]-1][i[0]-1]):
                continue
            else:
                sum_doubleaction=temp_string_chart_mat[i[0]-1][i[1]-1]+temp_string_chart_mat[i[1]-1][i[0]-1]
                temp_string_chart_mat[i[0]-1][i[1]-1]=sum_doubleaction
                temp_string_chart_mat[i[1]-1][i[0]-1]=sum_doubleaction


        return mat_exchange_list(temp_string_chart_mat)










a=[(1,4,300),(1,5,400),(1,7,500),(4,5,100),(4,7,250),(5,7,600)]
b=[(1,3,5),(1,2,3),(2,4,2),(3,4,1.5),(3,5,4),(4,6,3),(5,6,0.5),(5,7,3),(6,7,1.5)]
list_q=[(1,2,0.02),(3,4,0.06),(5,6,0.06),(4,6,0.02),(3,5,0.06)]
print(grahp_extent(b))
print(get_max(b))
c=string_data(b)
k=graph_string(OD_string=a,string_path_pow=c,list_q=list_q)
k.change_string_iter(0.5)
print(mat_exchange_list(k.show_string_chart()))
print(k.get_string_chart_doubleaction())


"""
print(mat_exchange_list(k.show_string_chart()))

v=short_path(1,7,mat_exchange_list(k.string_chart))
"""





# a=[(1,4,300),(1,5,400),(1,5,400),(1,7,500),(4,5,100),(4,7,250),(5,7,600)]
# print(change_list_mat(a))

"""

a=[(1,3,2),(1,2,4),(1,4,5)]
b=change_list_all_mat(a,4)
print(b)
c=mat_exchange_list(b)
print(c)

"""
