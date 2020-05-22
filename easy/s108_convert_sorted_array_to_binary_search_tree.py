"""
  * @FileName: s108_convert_sorted_array_to_binary_search_tree.py
  * @Author:   zzc
  * @Date:     2020年02月04日 10:41:33
  * @Version   V1.0.0
"""

"""
将一个按照升序排列的有序数组，转换为一棵高度平衡二叉搜索树。
本题中，一个高度平衡二叉树是指一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过 1。

示例:
给定有序数组: [-10,-3,0,5,9],
一个可能的答案是：[0,-3,9,-10,null,5]，它可以表示下面这个高度平衡二叉搜索树：

      0
     / \
   -3   9
   /   /
 -10  5
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    @staticmethod
    def sorted_array_to_binary_search_tree_1(nums: list):
        if not nums:
            return None
        mid = len(nums) // 2
        tree = TreeNode(nums[mid])
        tree.left = Solution.sorted_array_to_binary_search_tree_1(nums[:mid])
        tree.right = Solution.sorted_array_to_binary_search_tree_1(nums[mid + 1: len(nums)])
        return tree


if __name__ == '__main__':
    print(Solution.sorted_array_to_binary_search_tree_1([-10, -3, 0, 5, 9]))
