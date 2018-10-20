#!/usr/bin/env python
__author__ = 'Chocolee'

# 希尔排序 时间复杂度 O(1.3n)
def shell_sort(li):
    gap = int(len(li) // 2)
    while gap >= 1:
        for i in range(gap, len(li)):
            tmp = li[i]
            j = i - gap
            while j >= 0 and tmp < li[j]:
                li[j + gap] = li[j]
                j -= gap
            li[i - gap] = tmp
        gap = gap // 2


# 现在有一个列表，列表中的数范围都在0到100之间，列表长度大约为100万。设计算法在O(n)时间复杂度内将列表进行排序。
# 计数排序， 数据必须存在范围，才能使用
def count_sort(li, max_num):
    count = [0 for i in range(max_num + 1)]
    for num in li:
        count[num] += 1
    i = 0
    for num,m in enumerate(count):  #将数据和索引一起传入
        for j in range(m):
            li[i] = num
            i += 1

