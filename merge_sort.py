# coding=utf-8
"""归并排序"""

def merge_sort(alist):
    """归并排序"""
    length = len(alist)
    if length <=1:
        return alist
    merge_sort_between(alist,0,length-1)
    return alist


def merge_sort_between(blist,start,end):
    """切分及调用合并"""
    if start >= end:
        return
    mid = int((start+end)/2)
    print("左")
    merge_sort_between(blist,start,mid)
    print("右")
    merge_sort_between(blist,mid+1,end)
    print("合并")
    merge(blist,start,mid,end)


def merge(ablist,start,mid,end):
    """合并"""
    temp = []
    left_cur = start
    right_cur = mid+1
    print(ablist,start,mid,end)
    while left_cur<=mid and right_cur<=end:
        if ablist[left_cur]<ablist[right_cur]:
            temp.append(ablist[left_cur])
            left_cur += 1
        else:
            temp.append(ablist[right_cur])
            right_cur += 1

    last_start = left_cur if left_cur<=mid else right_cur
    last_end= mid if left_cur<=mid else end
    temp.extend(ablist[last_start:last_end+1])
    ablist[start:end+1]=temp




aaa=[3,2,1,11,3,4,55,33,22,43,21,3]
print(merge_sort(aaa))
