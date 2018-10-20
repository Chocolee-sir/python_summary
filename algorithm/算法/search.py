#!/usr/bin/env python
__author__ = 'Chocolee'

import time
import random

def cal_time(func):
    def wrapper(*args, **kwargs):
        ti = time.time()
        x = func(*args, **kwargs)
        ti2 =time.time()
        print('time cost:', func.__name__, ti2 - ti)
        return x
    return wrapper


# 二分法寻找数字, 利用索引的最大值和最小值
@cal_time
def bin_search(data_set, val):
    low = 0
    high = len(data_set) - 1
    while low <= high:
        mid = (low+high)//2
        if data_set[mid] == val:
            return mid
        elif data_set[mid] < val:
            low = mid + 1
        else:
            high = mid - 1
    return


# data = list(range(10))
# print(bin_search(data, 152))

# ################################################################## #


# 练习，生成数据后，输入数据、ID， 输出对应ID的游标及相应的内容
def random_list(n):
    result = []
    ids = list(range(1001,1001+n))
    a1 = ['zhao','qian','sun','li']
    a2 = ['li','hao','','']
    a3 = ['qiang','guo']
    for i in range(n):
        age = random.randint(18,60)
        id = ids[i]
        name = random.choice(a1)+random.choice(a2)+random.choice(a3)
        dict_info = {}
        dict_info['id'] = id
        dict_info['age'] = age
        dict_info['name'] = name
        result.append(dict_info)
    print(result)

#random_list(10)
user_data = [
    {'id': 1001, 'age': 35, 'name': 'lihaoqiang'},
    {'id': 1002, 'age': 59, 'name': 'sunqiang'},
    {'id': 1003, 'age': 37, 'name': 'zhaohaoqiang'},
    {'id': 1004, 'age': 59, 'name': 'liqiang'},
    {'id': 1005, 'age': 25, 'name': 'sunqiang'},
    {'id': 1006, 'age': 55, 'name': 'sunliguo'},
    {'id': 1007, 'age': 46, 'name': 'zhaoguo'},
    {'id': 1008, 'age': 33, 'name': 'zhaoqiang'},
    {'id': 1009, 'age': 51, 'name': 'sunhaoguo'},
    {'id': 1010, 'age': 44, 'name': 'qianliguo'}
]


def user_info_search(data_set, val):
    low = 0
    high = len(data_set) - 1
    while low <= high:
        mid = (low+high)//2
        if data_set[mid]['id'] == val:
            return mid
        elif data_set[mid]['id'] < val:
            low = mid + 1
        else:
            high = mid - 1
    return

print(user_data[user_info_search(user_data, 1008)])