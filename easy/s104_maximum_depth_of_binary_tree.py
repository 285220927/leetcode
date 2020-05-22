"""
  * @FileName: s104_maximum_depth_of_binary_tree.py
  * @Author:   zzc
  * @Date:     2020年02月03日 10:13:24
  * @Version   V1.0.0
"""

"""
给定一个二叉树，找出其最大深度。
二叉树的深度为根节点到最远叶子节点的最长路径上的节点数。

说明: 叶子节点是指没有子节点的节点。

示例：
给定二叉树 [3,9,20,null,null,15,7]，

    3
   / \
  9  20
    /  \
   15   7
返回它的最大深度 3 。
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    @staticmethod
    def max_depth_1(root: TreeNode):
        queue = [root]
        depth = 0
        while queue:
            next_queue = []
            flag = False
            for node in queue:
                if node:
                    next_queue.append(node.left)
                    next_queue.append(node.right)
                    flag = True
            queue = next_queue
            if flag:
                depth += 1
        return depth

    @staticmethod
    def max_depth_2(root: TreeNode):
        if not root:
            return 0
        left_height = Solution.max_depth_2(root.left)
        right_height = Solution.max_depth_2(root.right)
        return max(left_height, right_height) + 1


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
    print(Solution.max_depth_1(node1))
    print(Solution.max_depth_2(node1))
