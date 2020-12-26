"""
  * @FileName: s404_sum-of-left-leaves.py
  * @Author:   zzc
  * @Date:     2020年12月16日 20:28:04
  * @Version   V1.0.0
"""

"""
计算给定二叉树的所有左叶子之和。

示例：

    3
   / \
  9  20
    /  \
   15   7

在这个二叉树中，有两个左叶子，分别是 9 和 15，所以返回 24
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        if not root:
            return 0
        res = 0
        if root.left and not root.left.left and not root.left.right:
            res += root.left.val
        return self.sumOfLeftLeaves(root.left) + self.sumOfLeftLeaves(root.right) + res
