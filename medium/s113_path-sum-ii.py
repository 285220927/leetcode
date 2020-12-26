"""
  * @FileName: s113_path-sum-ii.py
  * @Author:   zzc
  * @Date:     2020年12月16日 22:53:04
  * @Version   V1.0.0
"""
from typing import List

"""
给定一个二叉树和一个目标和，找到所有从根节点到叶子节点路径总和等于给定目标和的路径。

说明: 叶子节点是指没有子节点的节点。

示例:
给定如下二叉树，以及目标和 sum = 22，

              5
             / \
            4   8
           /   / \
          11  9   4
         /  \    / \
        7    2  5   1
返回:

[
   [5,4,11,2],
   [5,8,4,5]
]
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        if not root:
            return [[]]
        if not root.left and not root.right and sum == root.val:
            return [[sum]]
        res = []
        left = self.pathSum(root.left, sum - root.val)
        right = self.pathSum(root.right, sum - root.val)
        for i in left:
            i.insert(0, root.val)
            res += i
        for i in right:
            i.insert(0, root.val)
            res += i
        return res
