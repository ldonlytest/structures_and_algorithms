# coding=utf-8
"""
基于链表的栈
"""
class Node(object):
    def __init__(self, value, next_node=None):
        self.value = value
        self.next = next_node

    def __repr__(self):
        return self.value

    def __str__(self):
        return str(self.value)

class LinkedStack(object):
    """基于链表的栈,长度固定"""
    def __init__(self,item,size):
        self.size = size
        self.count = 0
        if item:
            self.head = Node(item)
        else:
            self.head = None

    def push(self,item):
        """入栈操作"""
        if self.count == self.size:
            return False
        new_node = Node(item)
        new_node.next = self.head
        self.head = new_node
        self.count += 1
        return True

    def pop(self):
        """出栈操作"""
        if self.count==0:
            return
        temp = self.head.value
        self.head = self.head.next
        return temp


class DynamicLinkedStack(object):
    """基于链表的栈,长度不固定"""
    def __init__(self):
        self._top = None  # 哨兵结点

    def push(self,item):
        """入栈操作"""
        new_node = Node(item)
        new_node.next = self._top
        self._top = new_node
        return True

    def pop(self):
        """出栈操作"""
        if self._top is None:
            return
        temp = self._top.value
        self._top = self._top.next
        return temp