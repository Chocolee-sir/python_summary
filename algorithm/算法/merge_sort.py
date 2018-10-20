#!/usr/bin/env python
__author__ = 'Chocolee'

# 归并排序 时间复杂度 O(nlogn)  空间复杂度 O(n)

def merge(li, low, mid, high):
    i = low
    j = mid + 1
    ltmp = []
    while i <= mid and j <= high:
        if li[i] < li[j]:
            ltmp.append(li[i])
            i += 1
        else:
            ltmp.append(li[j])
            j += 1
    while i <= mid:
        ltmp.append(li[i])
        i += 1
    while j <= high:
        ltmp.append(li[j])
        j += 1
    li[low:high+1] = ltmp


def _mergesort(li, low, high):
    if low < high:
        mid = (low + high) // 2
        _mergesort(li, low, mid)
        _mergesort(li, mid+1, high)
        merge(li, low, mid, high)


def mergesort(li):
    _mergesort(li, 0, len(li) - 1)