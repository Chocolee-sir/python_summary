#!/usr/bin/env python
__author__ = 'Chocolee'

import random

# 堆排序
def sift(data, low, high):
    i = low
    j = 2 * i + 1
    tmp = data[i]
    while j <= high:  # 孩子在堆里
        if j < high and data[j] < data[j + 1]: #如果有右孩子且比左孩子大
            j += 1   # 指向右孩子
        if tmp < data[j]:  # 孩子比最高领导大
            data[i] = data[j]  # 孩子填到父亲的空位上
            i = j        # 孩子成为父亲
            j = 2 * i + 1  # 新孩子
        else:
            break
    data[i] = tmp   # 最高领导放到父亲位置


# 最后结果为升序
def heap_sort(data):
    n = len(data)
    for i in range(n // 2 - 1, -1, -1):
        sift(data, i, n - 1)
        # 堆建好了
    for i in range(n-1, -1, -1):     # i 指向堆的最后
        data[0], data[i] = data[i], data[0]  # 领导退休，小弟上位
        sift(data, 0, i - 1)    # 调整出新领导


# 方法二，最后结果为降序，废一块内存。
def heap_sort_1(data):
    n = len(data)
    for i in range(n // 2 - 1, -1, -1):
        sift(data, i, n - 1)
        # 堆建好了
    li = []
    for i in range(n-1, -1, -1):     # i 指向堆的最后
        li.append(data[0])
        data[0] = data[i]
        sift(data, 0, i - 1)
    return li



data = list(range(10))
# 洗牌，打成乱序
random.shuffle(data)
# heap_sort(data)
# print(data)
# print(heap_sort_1(data))
