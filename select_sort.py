# coding=utf-8
"""选择排序"""

def select_sort(alist):
    """
    选择排序，思想：分成未排序区和已排序区，从未排序区找出最小的值插入已排序区
    :param alist:
    :return:
    """
    lenght = len(alist)
    if lenght<=1:
        return alist

    for i in range(0,lenght):
        min_index = i
        for j in range(i+1,lenght):
            if alist[min_index]>alist[j]:
                min_index = j
        alist[i],alist[min_index] = alist[min_index],alist[i]
    return alist

al = [1,0,4,2,5,2,4,6,4,77,11]
print(select_sort(al))