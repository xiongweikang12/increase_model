import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd
from itertools import chain
import time
from functools import reduce


# TODO,通过输入表读取数据，草稿get

#TODO 图的流量分配

# 最短路径


def short_path(start,end,data):
    g = nx.DiGraph()
    g.add_weighted_edges_from(data)
    pos_node = nx.spring_layout(g)
    label_1 = nx.get_edge_attributes(g, 'weight')  # 为图添加边权标注
    list_node = nx.dijkstra_path(g, source=start, target=end)
    min_pathlenght = nx.dijkstra_path_length(g, source=start, target=end)
    short_edges_container = []

    for num_choice_node in range(len(list_node) - 1):
        short_edges_tuple = []
        short_edges_tuple.append(list_node[num_choice_node])
        short_edges_tuple.append(list_node[num_choice_node + 1])
        short_edges_tuple = tuple(short_edges_tuple)
        short_edges_container.append(short_edges_tuple)

    # print(short_edges_container) 最短路径
    # print(min_pathlenght)  最短路径长度

    short_edges_container_set = []
    for short_node_tuple in short_edges_container:
        short_path_node1, short_path_node2 = short_node_tuple
        short_edges_container_set.append(short_path_node1)
        short_edges_container_set.append(short_path_node2)
    short_edges_container_set = set(short_edges_container_set)
    short_edges_container_set = list(short_edges_container_set)

    pos_short_node = {}
    for get_tick in short_edges_container_set:
        pos_short_node[get_tick] = pos_node[get_tick]

    short_path = nx.Graph()  #
    short_path.add_edges_from(short_edges_container)
    nx.draw_networkx_nodes(g, pos_node, node_color='g', node_size=500, alpha=0.8)  # 画图的节点
    nx.draw_networkx_edges(g, pos_node, width=1.0, alpha=0.5, edge_color='b')  # 画图的边
    nx.draw_networkx_labels(g, pos_node)  # 标签默认
    nx.draw_networkx_edge_labels(g, pos_node, label_1)
    nx.draw_networkx_nodes(short_path, pos_short_node, node_color='r', node_size=500, alpha=0.8)
    nx.draw_networkx_edges(short_path, pos_short_node, width=1.0, alpha=0.5, edge_color='r')
    # copy_short_edges_container_set=short_edges_container_set
    # exprience_point=sorted(set(chain(short_edges_container_set)))
    #去重是无序的
    title_str=reduce(lambda x,y: x+y ,[str(i)+"->" for i in short_edges_container])
    title_str+=str(min_pathlenght)
    plt.title(title_str)
    # plt.show()
    return short_edges_container

# print(short_path(1,9,a))