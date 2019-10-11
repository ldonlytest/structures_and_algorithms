# coding=utf-8
"""
基于数组的队列
"""

class ArrayQueue(object):
    """
    基于数组的队列
    问题点：当不断出队、入队，出现的空闲空间用不了的问题
    """
    def __init__(self,size):
        self.size = size
        self.array = []
        self.head = 0
        self.tail =0

    def enqueue(self,item):
        """入队"""
        if self.tail == self.size:
            return False
        self.array.insert(self.tail,item)
        self.tail += 1
        return True

    def dequeue(self):
        """出队"""
        if self.head == self.tail:
            return
        temp = self.array[self.head]
        self.head += 1
        return temp
class ArrayQueueAfter(object):
    """
    基于数组的队列
    解决上述问题：出队是判断是否有空闲一段空间，进行数据迁移
    """
    def __init__(self,size):
        self.size = size
        self.array = []
        self.head = 0
        self.tail =0

    def enqueue(self,item):
        """入队"""
        if self.tail == self.size:
            if self.head==0:
                return False
            else:  # 数据迁移
                for i in range(0,self.tail-self.head):
                    self.array[i] = self.array[self.head+i]
                self.tail = (self.tail - self.head)
                self.head = 0
            self.array.insert(self.tail,item)
            self.tail += 1
            return True


    def dequeue(self):
        """出队"""
        if self.head == self.tail:
            return
        temp = self.array[self.head]
        self.head += 1
        return temp

