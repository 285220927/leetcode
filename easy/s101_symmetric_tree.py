"""
  * @FileName: s101_symmetric_tree.py
  * @Author:   zzc
  * @Date:     2020年02月02日 11:30:11
  * @Version   V1.0.0
"""

"""
给定一个二叉树，检查它是否是镜像对称的。

例如，二叉树 [1,2,2,3,4,4,3] 是对称的。

    1
   / \
  2   2
 / \ / \
3  4 4  3
但是下面这个 [1,2,2,null,3,null,3] 则不是镜像对称的:
1 2 2 3 4 4 3 5 6 6 5 5 6 6 5

2  2-3
3  4-7
4  8-15
5  16-31
    1
   / \
  2   2
   \   \
   3    3
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    @staticmethod
    def is_symmetric_1(root: TreeNode):
        queue = [root]
        while queue:
            next_queue = []
            temp = []
            for node in queue:
                if not node:
                    temp.append(None)
                    continue
                temp.append(node.val)
                next_queue.append(node.left)
                next_queue.append(node.right)
            queue = next_queue
            if temp != temp[::-1]:
                return False
        return True

    @staticmethod
    def check(left_tree, right_tree):
        if not left_tree and not left_tree:
            return True
        if not left_tree or not right_tree:
            return False
        return left_tree.val == right_tree.val and Solution.check(left_tree.left, right_tree.right) and Solution.check(
            left_tree.right, right_tree.left)

    @staticmethod
    def is_symmetric_2(root: TreeNode):
        return Solution.check(root, root)


if __name__ == '__main__':
    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(2)
    node4 = TreeNode(None)
    node5 = TreeNode(3)
    node6 = TreeNode(None)
    node7 = TreeNode(3)
    node1.left = node2
    node1.right = node3
    node2.left = node4
    node2.right = node5
    node3.left = node6
    node3.right = node7
    print(Solution.is_symmetric_1(node1))
    print(Solution.is_symmetric_2(node1))
