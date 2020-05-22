"""
  * @FileName: s100_same_tree.py
  * @Author:   zzc
  * @Date:     2020年02月02日 10:16:36
  * @Version   V1.0.0
"""

"""
给定两个二叉树，编写一个函数来检验它们是否相同。
如果两个树在结构上相同，并且节点具有相同的值，则认为它们是相同的。

示例 1:
输入:       1         1
          / \       / \
         2   3     2   3

        [1,2,3],   [1,2,3]

输出: true

示例 2:
输入:      1          1
          /           \
         2             2

        [1,2],     [1,null,2]

输出: false

示例 3:
输入:       1         1
          / \       / \
         2   1     1   2

        [1,2,1],   [1,1,2]

输出: false
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    @staticmethod
    def is_same_tree_1(p: TreeNode, q: TreeNode):
        if not p and not q:
            return True
        if p and q and p.val == q.val:
            return Solution.is_same_tree_1(p.left, q.left) and Solution.is_same_tree_1(p.right, q.right)
        else:
            return False


if __name__ == '__main__':
    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    node4 = TreeNode(1)
    node5 = TreeNode(2)
    node6 = TreeNode(3)
    node1.left = node2
    node1.right = node3
    node4.left = node5
    node4.right = node6
    print(Solution.is_same_tree_1(node1, node4))
