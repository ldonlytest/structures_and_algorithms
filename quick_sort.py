# coding=utf-8
"""快速排序"""

def quick_sort(alist):
    """快速排序"""
    length = len(alist)
    if length <=1:
        return alist
    quick_sort_part(alist,0,length-1)
    return alist


def quick_sort_part(blist,start,end):
    """切分及调用合并"""
    if start >= end:
        return
    privot = partion(blist,start,end)
    print(privot)
    print("左")
    quick_sort_part(blist,start,privot-1)
    print("右")
    quick_sort_part(blist,privot+1,end)

def partion(blist,start,end):
    privot = blist[end]
    current = start
    for i in range(start,end+1):
        if blist[i]<privot:
            blist[i], blist[current] = blist[current], blist[i]
            current+=1

    blist[current], blist[end] = blist[end], blist[current]
    return current




aaa=[3,2,1,11,3,4,55,33,22,43,21,3]
print(quick_sort(aaa))
