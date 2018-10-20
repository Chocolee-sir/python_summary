#!/usr/bin/env python
__author__ = 'Chocolee'

import random

# 插入排序 时间复杂度 O(n²)
def insert_sort(li):
    for i in range(1, len(li)):
        tmp = li[i]
        j = i - 1
        while j >= 0 and li[j] > tmp:
            li[j + 1] = li[j]
            j = j - 1
        li[j + 1] = tmp

data = list(range(5000))
# 洗牌，打成乱序
random.shuffle(data)
insert_sort(data)
print(data)