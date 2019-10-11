# coding=utf-8
"""
基于链表的队列
"""
class Node(object):
    """结点"""
    def __init__(self, value, next_node=None):
        self.value = value
        self.next = next_node

class LinkedQueue(object):
    """基于链表的队列"""
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self,item):
        """入栈,需要考虑为None的情况"""
        new_node = Node(item)
        if self.tail:
            self.tail.next = new_node
        else:
            self.head = new_node
        self.tail = new_node

    def dequeue(self):
        """出栈,考虑为空或者只有一个结点时的情况"""
        if self.head:
            temp = self.head.value
            self.head = self.head.next
            if not self.head:  # 只有一个结点时的情况
                self.tail = None
            return temp

    def __repr__(self) -> str:
        values = []
        current = self.head
        while current:
            values.append(current.value)
            current = current.next
        return "->".join(value for value in values)

if __name__ == "__main__":
    q = LinkedQueue()
    for i in range(10):
        q.enqueue(str(i))
    print(q)

    for _ in range(3):
        q.dequeue()
    print(q)

    q.enqueue("7")
    q.enqueue("8")
    print(q)