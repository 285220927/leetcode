"""
  * @FileName: s21_merge_two_sorted_lists.py
  * @Author:   zzc
  * @Date:     2020年01月28日 10:04:53
  * @Version   V1.0.0
"""

"""
将两个有序链表合并为一个新的有序链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 

示例：
输入：1->2->4, 1->3->4
输出：1->1->2->3->4->4
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    @staticmethod
    def merge_two_lists_1(l1: ListNode, l2: ListNode):
        head = ListNode(None)
        cur = head
        while l1 and l2:
            if l1.val < l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
        if l1 is None:
            cur.next = l2
        else:
            cur.next = l1
        return head.next

    @staticmethod
    def merge_two_lists_2(l1: ListNode, l2: ListNode):
        if l1 is None:
            return l2
        elif l2 is None:
            return l1
        elif l1.val < l2.val:
            l1.next = Solution.merge_two_lists_2(l1.next, l2)
            return l1
        else:
            l2.next = Solution.merge_two_lists_2(l1, l2.next)
            return l2


if __name__ == '__main__':
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(5)
    node4 = ListNode(1)
    node5 = ListNode(3)
    node6 = ListNode(4)
    node1.next = node2
    node2.next = node3
    node4.next = node5
    node5.next = node6
    print(Solution.merge_two_lists_1(node1, node4))
    print(Solution.merge_two_lists_2(node1, node4))
