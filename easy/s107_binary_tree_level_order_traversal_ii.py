"""
  * @FileName: s107_binary_tree_level_order_traversal_ii.py
  * @Author:   zzc
  * @Date:     2020年02月03日 11:12:21
  * @Version   V1.0.0
"""

"""
给定一个二叉树，返回其节点值自底向上的层次遍历。 （即按从叶子节点所在层到根节点所在的层，逐层从左向右遍历）

例如：
给定二叉树 [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回其自底向上的层次遍历为：

[
  [15,7],
  [9,20],
  [3]
]
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    @staticmethod
    def level_order_bottom_1(root: TreeNode):
        if not root:
            return []
        queue = [root]
        res = []
        while queue:
            cur = []
            queue_len = len(queue)
            for i in range(queue_len):
                node = queue.pop(0)
                cur.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(cur)
        return res[::-1]


if __name__ == '__main__':
    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    node4 = TreeNode(4)
    node5 = TreeNode(5)
    node1.left = node2
    node1.right = node3
    node2.left = node4
    node3.right = node5
    print(Solution.level_order_bottom_1(node1))
