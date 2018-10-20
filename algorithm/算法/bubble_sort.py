#!/usr/bin/env python
__author__ = 'Chocolee'
import random
import time


#  冒泡排序 时间复杂度 O(n²)
def cal_time(func):
    def wrapper(*args, **kwargs):
        ti = time.time()
        x = func(*args, **kwargs)
        ti2 =time.time()
        print('time cost:', func.__name__, ti2 - ti)
        return x
    return wrapper


# 最基础的冒泡排序
@cal_time
def bubble_sort(li):
    for i in range(len(li) - 1):
        for j in range(len(li) - i - 1):
            if li[j] > li[j+1]:
                li[j], li[j+1] = li[j+1], li[j]


# 优化后的冒泡排序
@cal_time
def bubble_sort_1(li):
    for i in range(len(li) - 1):
        exchange = False
        for j in range(len(li) - i - 1):
            if li[j] > li[j+1]:
                li[j], li[j+1] = li[j+1], li[j]
                exchange = True
        if not exchange:
            break


data = list(range(5000))
# 洗牌，打成乱序
random.shuffle(data)
#bubble_sort(data)
bubble_sort_1(data)
# print(data)
