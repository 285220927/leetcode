"""
  * @FileName: s110_balanced_binary_tree.py
  * @Author:   zzc
  * @Date:     2020年02月04日 11:04:13
  * @Version   V1.0.0
"""

"""
给定一个二叉树，判断它是否是高度平衡的二叉树。
本题中，一棵高度平衡二叉树定义为：
一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过1。

示例 1:
给定二叉树 [3,9,20,null,null,15,7]

    3
   / \
  9  20
    /  \
   15   7
返回 true 

示例 2:
给定二叉树 [1,2,2,3,3,null,null,4,4]

       1
      / \
     2   2
    / \
   3   3
  / \
 4   4
返回 false
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    @staticmethod
    def is_balanced_1(root):
        return Solution.depth(root) != -1

    @staticmethod
    def depth(root):
        if not root:
            return 0
        left = Solution.depth(root.left)
        if left == -1:
            return -1
        right = Solution.depth(root.right)
        if right == -1:
            return -1
        return max(left, right) + 1 if abs(left - right) < 2 else -1


if __name__ == '__main__':
    node1 = TreeNode(3)
    node2 = TreeNode(9)
    node3 = TreeNode(20)
    node4 = TreeNode(None)
    node5 = TreeNode(None)
    node6 = TreeNode(15)
    node7 = TreeNode(7)
    node1.left = node2
    node1.right = node3
    node2.left = node4
    node2.right = node5
    node3.left = node6
    node3.right = node7
    print(Solution.is_balanced_1(node1))
