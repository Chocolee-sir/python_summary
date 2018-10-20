#!/usr/bin/env python
__author__ = 'Chocolee'
import random
import time
import sys

# 设置递归深度限制。
sys.setrecursionlimit(10000)

# 快速排序  时间复杂度 O(nlogn)
def cal_time(func):
    def wrapper(*args, **kwargs):
        ti = time.time()
        x = func(*args, **kwargs)
        ti2 =time.time()
        print('time cost:', func.__name__, ti2 - ti)
        return x
    return wrapper


def quick_sort_x(data, left, right):
    if left < right:
        mid = partition(data, left, right)
        quick_sort_x(data, left, mid - 1)
        quick_sort_x(data, mid + 1, right)


def partition(data, left, right):
    tmp = data[left]
    while left < right:
        while left < right and data[right] >= tmp:
            right -= 1
        data[left] = data[right]
        while left < right and data[left] <= tmp:
            left += 1
        data[right] = data[left]
    data[left] = tmp
    return left


@cal_time
def quick_sort(data):
    return quick_sort_x(data, 0, len(data) - 1)

data = list(range(5000))
# 洗牌，打成乱序
random.shuffle(data)
quick_sort(data)

