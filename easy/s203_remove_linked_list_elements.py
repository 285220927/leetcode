"""
  * @FileName: s203_remove_linked_list_elements.py
  * @Author:   zzc
  * @Date:     2020年02月14日 12:38:55
  * @Version   V1.0.0
"""

"""
删除链表中等于给定值 val 的所有节点。

示例:
输入: 1->2->6->3->4->5->6, val = 6
输出: 1->2->3->4->5
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    @staticmethod
    def remove_elements_1(head: ListNode, val: int):
        if not head:
            return None
        while head and head.val == val:
            head = head.next
        cur = head
        while cur and cur.next:
            if cur.next.val == val:
                cur.next = cur.next.next
            else:
                cur = cur.next
        return head

    @staticmethod
    def remove_elements_2(head: ListNode, val: int):
        # 递归
        if not head:
            return None
        res = Solution.remove_elements_2(head.next, val)
        if head.val == val:
            return res
        else:
            head.next = res
            return head


if __name__ == '__main__':
    n1 = ListNode(1)
    n2 = ListNode(2)
    n3 = ListNode(6)
    n4 = ListNode(3)
    n5 = ListNode(4)
    n6 = ListNode(5)
    n7 = ListNode(6)
    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n5
    n5.next = n6
    n6.next = n7
    print(Solution.remove_elements_1(n1, 1))
    print(Solution.remove_elements_2(n1, 1))
