# coding=utf-8
"""
计数排序
核心思想：待排序数据范围不大，非负整数或者相对大小不变的情况下可以转成成非负整数
          例如范围是k，将分成k桶，每个桶中存个数，从而可以知道<=kn数据的位置（累加）
"""

def counting_sort(alist):
    length = len(alist)
    if length <= 1:
        return alist
    max_value = alist[0]
    for i in range(1,length):  # 求最大值可以用max代替
        if alist[i] > max_value:
            max_value = alist[i]

    bucket_list = [0]*(max_value+1)

    for value in alist:
        bucket_list[value] += 1

    temp = bucket_list[:]
    for i in range(0,len(bucket_list)):  # 可以用list(itertools.accumulate(counts)) [1,2,3,4] --> [1, 1+2, (1+2)+3, ((1+2)+3)+4]替代
        total = 0
        for j in range(0,i+1):
            total += temp[j]
        bucket_list[i] = total

    #copy到另外一个临时空间
    result = [0]*length

    for i in range(length-1,-1,-1):  # 逆序也可以用reverse
        cur_value = alist[i]
        index = bucket_list[cur_value]
        result[index-1] = cur_value
        bucket_list[cur_value] -= 1
    alist = result[:]



test_list=[2,5,3,0,2,3,0,3]

counting_sort(test_list)