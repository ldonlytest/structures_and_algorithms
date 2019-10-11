# coding=utf-8
"""
循环队列,会有一个空间是空闲的
"""
class CircularQueue(object):
    """循环队列"""
    def __init__(self,size):
        self.size  = size
        self.head = 0
        self.tail = 0
        self.array = []

    def enqueue(self,item):
        """入栈,入之前判断是否满"""
        if (self.tail+1)%self.size == self.head:
            return False
        self.array.insert(self.tail,item)
        self.tail = (self.tail+1)%self.size
        return True

    def dequeue(self):
        """出栈，出之前判断是否为空"""
        if self.tail == self.head:
            return
        temp = self.array[self.head]
        self.head = (self.head+1)%self.size
        return temp