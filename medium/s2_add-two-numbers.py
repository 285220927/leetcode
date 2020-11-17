"""
  * @FileName: s2_add-two-numbers.py
  * @Author:   zzc
  * @Date:     2020年11月08日 14:47:37
  * @Version   V1.0.0
"""

"""
2. 两数相加
给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。
如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。
您可以假设除了数字 0 之外，这两个数都不会以 0 开头。

示例：
输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
输出：7 -> 0 -> 8
原因：342 + 465 = 807
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def __init__(self):
        self.ten = 0
        self.res = ListNode()
        self.nex = self.res

    def addTwoNumbers(self, l1, l2):
        if l1 or l2 or self.ten:
            self.nex.next = ListNode()
            self.nex = self.nex.next
            val = self.ten + (l1.val if l1 else 0) + (l2.val if l2 else 0)
            self.ten = val / 10
            self.nex.val = val % 10
            self.addTwoNumbers(l1.next if l1 else None, l2.next if l2 else None)
        return self.res.next


if __name__ == '__main__':
    l1 = ListNode(2)
    l1.next = ListNode(4)
    # l1.next.next = ListNode(3)
    l2 = ListNode(5)
    l2.next = ListNode(1)
    # l2.next.next = ListNode(4)
    Solution().addTwoNumbers(l1, l2)
    # print(Solution().addTwoNumbers(l1, l2).val)
    # print(Solution().addTwoNumbers(l1, l2).next.val)
    # print(Solution().addTwoNumbers(l1, l2).next.next.val)

