# coding=utf-8
"""插入排序"""

def insert_sort(alist):
    """插入排序,需要挪动位置"""
    length = len(alist)
    if length<=1:
        return alist
    for i in range(1,length):
        value = alist[i]
        pre = i-1
        while pre>=0:
            if value < alist[pre]:
                alist[pre+1] =alist[pre]  # 数据移动
            else:
                break
            pre -= 1
        alist[pre+1] = value  # 注意这个位置
    return alist

al = [1,4,2,5,2,4,6,4,77,11]
print(insert_sort(al))