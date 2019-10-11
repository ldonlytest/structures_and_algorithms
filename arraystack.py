# coding=utf-8
"""
基于数组的栈
"""

class ArrayStack(object):
    """基于数组的栈类"""
    def __init__(self,size=10):
        self.array=[]
        self.top = 0
        self.size = size

    def push(self,item):
        """
        入栈操作
        :param item:
        :return:
        """
        if self.top==self.size:
            return False
        self.array.append(item)
        self.top += 1
        return True

    def pop(self):
        """
        出栈操作
        :return:
        """
        if self.top <= 0:
            return
        tmp = self.array[self.top-1]
        self.top -= 1
        return tmp








