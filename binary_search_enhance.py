# coding=utf-8
"""
二分查找的“近似”值查找
假设前提：从小到大的有序、可能会有重复元素
  1. 查找第一个相等给定值的位置
  2. 查找最后一个相等给定值的位置
  3. 查找第一个大于等于给定值的位置
  4. 查找最后一个小于等于给定值的位置
"""

def binary_search_by_first(alist,value):
    """查找第一个相等给定值的位置"""
    length = len(alist)
    if length <= 1:
        return alist
    low = 0
    high = length - 1
    while low<=high:
        mid = low +((high - low)>>1)
        if alist[mid] > value:
            high = mid - 1
        elif alist[mid] < value:
            low = mid + 1
        else:
            if mid ==0 or alist[mid-1] != value:
                return mid
            else:
                high = mid -1
    return -1


def binary_search_by_last(alist,value):
    """查找最后一个相等给定值的位置"""
    length = len(alist)
    if length <= 1:
        return alist
    low = 0
    high = length - 1
    while low <= high:
        mid = low + ((high-low)>>1)
        if alist[mid] > value:
            high = mid - 1
        elif alist[mid] < value:
            low = mid + 1
        else:
            if mid == length -1 or alist[mid+1] != value:
                return mid
            else:
                low = mid +1
    return -1

def binary_search_gt(alist,value):
    """查找第一个大于等于给定值的位置"""
    length = len(alist)
    if length <= 1:
        return alist
    low = 0
    high = length - 1
    while low <= high:
        mid = low + ((high - low) >> 1)
        if alist[mid] < value:
            low = mid + 1
        else:
            if mid==0 or alist[mid-1]<value:
                return mid
            else:
                high = mid -1
    return -1

def binary_search_lt(alist,value):
    """查找最后一个小于等于给定值的位置"""
    length = len(alist)
    if length <= 1:
        return alist
    low = 0
    high = length - 1
    while low <= high:
        mid = low + ((high - low) >> 1)
        if alist[mid] > value:
            high = mid -1
        else:
            if mid==length-1 or alist[mid+1]>value:
                return mid
            else:
                low = mid + 1
    return -1

aa=[1,3,4,5,6,8,8,8,11,18]
print(binary_search_lt(aa,3))