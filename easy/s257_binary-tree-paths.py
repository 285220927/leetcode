"""
  * @FileName: s257_binary-tree-paths.py
  * @Author:   zzc
  * @Date:     2020年12月16日 21:31:24
  * @Version   V1.0.0
"""
from typing import List

"""
给定一个二叉树，返回所有从根节点到叶子节点的路径。

说明: 叶子节点是指没有子节点的节点。

示例:
输入:

   1
 /   \
2     3
 \
  5

输出: ["1->2->5", "1->3"]
解释: 所有根节点到叶子节点的路径为: 1->2->5, 1->3
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        res = []
        if not root:
            return res
        if not root.left and not root.right:
            return [str(root.val)]
        res.extend(self.binaryTreePaths(root.left))
        res.extend(self.binaryTreePaths(root.right))
        for i in range(len(res)):
            res[i] = str(root.val) + '->' + str(res[i])
        return res
