# coding=utf-8
"""
实现单向链表
链表：不连续的空间存储,结点包含了value及next指向下一个节点，特殊的2个结点：头结点和尾结点
"""


class Node(object):
    def __init__(self, value, next_node=None):
        self.value = value
        self.next = next_node

    def __repr__(self):
        return self.value

    def __str__(self):
        return str(self.value)

class LinkedList(object):
    """
    单向链表
    """

    def __init__(self,item=None):
        if item:
            self.head = Node(item)
            self.tail = self.head
        else:
            self.head = None
            self.tail = None

    def add(self,item):
        """头部添加"""
        node = Node(item)
        if not self.head:
            self.head = node
            self.tail = self.head
        elif self.tail:
            node.next = self.head
            self.head = node
        else:
            self.tail = self.head.next

    def append(self,item):
        """尾部添加,多一个尾指针，每次插入减少遍历"""
        if not self.head:
            self.head = Node(item)
            self.tail = self.head
        elif self.tail:
            self.tail.next = Node(item)
            self.tail = self.tail.next
        else:  # 这一步感觉没必要
            self.tail = Node(item)

    def remove(self,item):
        """删除指定值的结点"""
        if not self.head:
            return False
        pre = None
        cur = self.head
        while cur != None:
            if cur.value != item:
                pre = cur
                cur = cur.next
            else:
                if cur==self.head:  # 删除的是头结点
                    self.head = cur.next
                    break
                else:  # 删除的不是头结点
                    pre.next = cur.next
                    break

    def remove_node(self,node):
        """删除指定值的结点"""
        if not self.head:
            return False
        pre = None
        cur = self.head
        while cur != None:
            if cur != node:
                pre = cur
                cur = cur.next
            else:
                if cur==self.head:  # 删除的是头结点
                    self.head = cur.next
                    break
                else:  # 删除的不是头结点
                    pre.next = cur.next
                    break

    def length(self):
        """计算链表长度"""
        count = 0
        cur = self.head
        while cur:
            count += 1
            cur = cur.next
        return count

    def is_empty(self):
        """判断链表是否为空"""
        if self.head:
            return False
        return True

    def travel(self):
        """
        遍历链表的值
        :return:
        """
        return self.__iter__()

    def __iter__(self):
        cur = self.head
        while cur:
            yield cur.value
            cur = cur.next

    def insert(self,pos, item):
        """插入指定位置,位置小标从0开始，类似数组"""
        if pos <= 0:
            self.add(item)
        elif pos >= self.length():
            self.append(item)
        else:
            count = 0
            pre = self.head
            node = Node(item)
            while count < (pos-1):  # pre 指向pos前一个位置
                pre = pre.next
                count += 1
            node.next = pre.next
            pre.next = node

    def insert_node_before(self,node,item):
        """
        在指定结点前插入新的值
        :param node:
        :param item:
        :return:
        """
        if (node is None) or (self.head is None):
            return
        if node == self.head:
            self.add(item)
            return
        pre = self.head
        while pre.next:
            if  pre.next == node:
                self.insert_node_after(pre,item)
                break
            pre = pre.next

    @staticmethod
    def insert_node_after(node,item):
        """
        在指定结点后插入新的值
        :param node:
        :param item:
        :return:
        """
        if node is None:
            return
        new_node = Node(item)
        new_node.next =node.next
        node.next = new_node

    def exist(self,item):
        """
        查找某个值是否存在
        :param item:
        :return:
        """
        cur = self.head
        while cur:
            if cur.value == item:
                return True
            else:
                cur = cur.next
        return False

    def find_node(self,item):
        """
        根据值查找结点
        :param item:
        :return:
        """
        cur = self.head
        while cur:
            if cur.value == item:
                return cur
            else:
                cur = cur.next
        return False

    def find_mid_node(self):
        """
        查找中间结点
        思想：设置快慢指针，快指针走2步，慢指针走1步，直到最后一个结点
        :return:
        """
        fast = self.head
        slow = self.head
        while  fast and fast.next:  #  偶数时，取中间的后一个值
            fast = fast.next.next
            slow = slow.next
        return slow

    def delete_last_n_node(self,n):
        """
        删除倒数第n个结点
        思想：快慢2个指针，快指针先走n步后，快慢指针同时走，直到快指针走到最后一个结点
        :param n:
        :return:
        """
        count = 0
        slow = self.head
        fast = self.head
        pre = None
        while fast.next:
            if count == n:
                pre = slow
                fast = fast.next
                slow = slow.next
            else:
                fast = fast.next
                count += 1
        if fast == self.head:
            self.remove_node(fast)
            return
        if pre:
            pre.next = slow.next

    def has_ring(self):
        """
        查找是否有环
        思想：设置快、慢两种指针，快指针每次跨两步，慢指针每次跨一步，如果快指针没有与慢指针相遇而是顺利到达链表尾部
        :return:
        """
        slow = self.head
        fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow==fast:
                return True
        return False

    def reverse_self(self):
        """
        翻转链表
        相邻之前两两交换
        :return:
        """
        if (self.head is None) or (self.head.next is None):
            return
        pre = self.head
        next_node = self.head.next
        self.tail = self.head
        while next_node:
            tmp = next_node.next
            next_node.next = pre
            pre = next_node
            next_node = tmp
        self.head.next = None  # 开始的head next是存有地址的，注意置空，否则是环
        self.head = pre


def merge_sorted_list(l1, l2):
    """
    合并2个有序链表
    :param l1:
    :param l2:
    :return:
    """
    if l1 and l2:
        fake_head = Node(None)
        current = fake_head
        p1,p2 = l1.head, l2.head
        while p1 and p2:
            if p1.value <= p2.value:
                current.next = p1
                p1 = p1.next
            else:
                current.next = p2
                p2 = p2.next
            current = current.next
        current.next =p1 if p1 else p2
        return fake_head.next

    return l1 or l2










