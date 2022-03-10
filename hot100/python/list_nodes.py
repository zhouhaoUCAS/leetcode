"""
链表：
    leetcode性质：
        # Definition for singly-linked list.
        # class ListNode:
        #     def __init__(self, val=0, next=None):
        #         self.val = val
        #         self.next = next
    初始化： one_node = ListNode(9), full_node, update_node = one_node
    更新： update_node = update_node.next() update_node.val = 9

"""

"""
一、两数之和
给你两个非空 的链表，表示两个非负的整数。它们每位数字都是按照逆序的方式存储的，并且每个节点只能存储一位数字。

请你将两个数相加，并以相同形式返回一个表示和的链表。

你可以假设除了数字 0 之外，这两个数都不会以 0开头。

输入：l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
输出：[8,9,9,9,0,0,0,1]
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # 初始化第一个节点， 不进位
        next_node = ListNode(l1.val + l2.val)
        # 一个作为第一个节点返回节点， 一个迭代更新
        result, update = next_node, next_node
        # 只要有一个输入链表还有节点或者需要进位
        while (l1 and (l1.next != None)) or (l2 and (l2.next != None)) or update.val > 9:
            # 对后续还有节点的进行判断
            l1, l2 = l1.next if l1 else l1, l2.next if l2 else l2
            # 加总下一个节点
            sum_val = (l1.val if l1 else 0) + (l2.val if l2 else 0)
            # 更新下一个节点， 不进位
            update.next = ListNode(sum_val + update.val // 10)
            # 更新当前节点取个位
            update.val %= 10
            # 往后遍历下一个节点
            update = update.next
        return result
