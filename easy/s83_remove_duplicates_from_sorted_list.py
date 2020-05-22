"""
  * @FileName: s83_remove_duplicates_from_sorted_list.py
  * @Author:   zzc
  * @Date:     2020年02月01日 10:05:14
  * @Version   V1.0.0
"""

"""
给定一个排序链表，删除所有重复的元素，使得每个元素只出现一次。

示例 1:
输入: 1->1->2
输出: 1->2

示例 2:
输入: 1->1->2->3->3
输出: 1->2->3
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    @staticmethod
    def delete_duplicates_1(head: ListNode):
        cur = head
        while head:
            if head.next and head.val == head.next.val:
                head.next = head.next.next
            else:
                head = head.next
        return cur


if __name__ == '__main__':
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(5)
    node4 = ListNode(5)
    node5 = ListNode(5)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    print(Solution.delete_duplicates_1(node1))
