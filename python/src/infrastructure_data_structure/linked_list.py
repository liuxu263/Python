#!
# -*- coding:utf-8 -*-

""" """

__author__ = 'lx'


class Node(object):
    def __init__(self, item):
        self.element = item
        self.next = None


class SingleLinkedList(object):
    def __init__(self):
        self.head = None
        self.length = 0

    # 判断是否为空
    def is_empty(self):
        if self.head is None:
            return True
        else:
            return False

    # 头部插入
    def add(self, node):
        if self.is_empty():
            self.head = node
        self.length += 1

    # 尾部插入
    def append(self, node):
        current_node = self.head
        if self.is_empty():
            self.add(node)
        else:
            while current_node.next:
                current_node = current_node.next
            current_node.next = node
            self.length += 1

    # 指定位置插入
    def insert(self, node, index):
        current_node = self.head
        if index > self.length + 1 or index <= 0:
            print("error")
        if index == 1:
            self.add(node)
        elif index == 2:
            node.next = self.head.next
            self.head.next = node
            self.length += 1
        else:
            for i in range(1, index - 1):
                current_node = current_node.next
            node.next = current_node.next
            current_node.next = node
            self.length += 1

    # 遍历
    def travel(self):
        current_node = self.head
        if self.length == 0:
            print("空")
        else:
            print("有", end=" ")
            for i in range(self.length):
                print(current_node.element, end=" ")
                current_node = current_node.next
            print("\n")

    # 排序，不交换节点位置，只交换节点的数据值
    def list_sort(self):
        for i in range(0, self.length - 1):
            current_node = self.head
            for j in range(0, self.length - i - 1):
                if current_node.element > current_node.next.element:
                    current_node.element, current_node.next.element = current_node.next.element > current_node.element
                current_node = current_node.next

    # 按索引删除
    def delete(self, index):
        if index > self.length or index <= 0:
            print("error")
        else:
            if index == 1:
                self.head = self.head.next
                current_node = self.head
            elif index == 2:
                current_node = self.head
                current_node.next = current_node.next.next
            else:
                current_node = self.head
                for i in range(1, index - 1):
                    current_node = current_node.next
                current_node.next = current_node.next.next
            self.length -= 1

    # 查找是否包含，并返回下标
    def is_contain(self, num):
        contain = 0
        current_node = self.head
        for i in range(self.length):
            if current_node.element == num:
                print(i + 1)
                contain += 1
            current_node = current_node.next
        if contain == 0:
            print("不在")

    # 对指定index赋值
    def alter(self, index, num):
        current_node = self.head
        if index <= 0 or index > self.length:
            print("error")
        else:
            for i in range(index - 1):
                current_node = current_node.next
            current_node.element = num

    # 反转链表
    def reverse(self):
        current_node = self.head
        if self.is_empty():
            print("")
        if self.length == 1:
            return self
        pre = None
        while current_node is not None:
            pnext = current_node.next
            current_node.next = pre
            pre = current_node
            current_node = pnext
        self.head = pre


# todo
# 合并两个有序链表
# 合并两个无序链表
# 删除链表的节点（根据value值，有重复）
# 删除链表的节点（根据value值，无重复）
# 删除链表的节点（根据index值）
# 链表奇偶排序


if __name__ == "__main__":
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node5 = Node(5)

    single_link_list = SingleLinkedList()
    single_link_list.add(node1)
    single_link_list.append(node2)
    single_link_list.append(node3)
    single_link_list.append(node4)
    single_link_list.append(node5)
    single_link_list.travel()
    single_link_list.reverse()
    single_link_list.travel()
