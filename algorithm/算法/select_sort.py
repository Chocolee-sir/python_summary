#!/usr/bin/env python
__author__ = 'Chocolee'
import random


# 时间复杂度 O(n²)
def select_sort(li):
    for i in range(len(li) - 1):
        min_loc = i
        for j in range(i+1, len(li)):
            if li[j] < li[min_loc]:
                min_loc = j
        li[i], li[min_loc] = li[min_loc], li[i]


data = list(range(1000))
#洗牌，打成乱序
random.shuffle(data)
select_sort(data)
print(data)

