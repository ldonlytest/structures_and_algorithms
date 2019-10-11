# coding=utf-8
"""
二分查找
  核心思想：不断缩小范围
  数据类型：数组
  实现：非递归和递归
"""

def binary_search(alist,value):
    lenght = len(alist)
    if lenght <= 1:
        return alist
    low = 0
    high = lenght-1

    while low<=high:
        mid = low + ((high - low)>>1)  # 注意括号，+ 的优先级更高
        if alist[mid] == value:
            return mid
        elif alist[mid] > value:
            high = mid - 1
        else:
            low = mid + 1
    return -1


"""以下递归实现"""

def binary_search_1(alist,value):
    lenght = len(alist)
    if lenght <= 1:
        return alist
    return binary_search_inter(0, lenght - 1, alist, value)


def binary_search_inter(low,high,alist,value):
    if low > high:
        return -1
    mid = low + ((high - low)>>1)
    if alist[mid] == value:
        return mid
    elif alist[mid] > value:
        return binary_search_inter(low, mid - 1, alist, value)
    else:
        return binary_search_inter(mid + 1, high, alist, value)




aa=[1,3,5,6,7,8,9,10]

print(binary_search_1(aa,5))