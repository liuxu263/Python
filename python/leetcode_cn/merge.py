# 将两个升序链表合并为一个新的 升序 链表并返回。
# 新链表是通过拼接给定的两个链表的所有节点组成的。 
# 示例：
# 输入：1->2->4, 1->3->4
# 输出：1->1->2->3->4->4

class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None


def __init__(self, node):
    self.head = None
    self.length = 0


def merge(node1, node2):
    if node1.value > node2.value:
        temp = node2


if __name__ == "__main__":
    node1 = Node(1)
    node2 = Node(3)
    node3 = Node(5)
    node4 = Node(7)
    node5 = Node(2)
    node6 = Node(4)
    node7 = Node(6)
    node8 = Node(8)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node5.next = node6
    node6.next = node7
    node7.next = node8
