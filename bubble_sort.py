# coding=utf-8
"""冒泡排序"""


def bubble_sort(alist):
    """冒泡排序"""
    length = len(alist)
    if length<=1:
        return alist
    for i in range(0,length):
        flag = False  # 标记是否有交换，没有交换提前跳出循环
        for j in range(0,length-i-1):
            if alist[j]>alist[j+1]:
                alist[j],alist[j+1] = alist[j+1],alist[j]
                flag = True
        if not flag:
            break
    return alist



al=[4,3,2,7,6,1,4,9,11,1]
print(bubble_sort(al))