"""
  * @FileName: s88_merge_sorted_array.py
  * @Author:   zzc
  * @Date:     2020年02月01日 10:46:53
  * @Version   V1.0.0
"""

"""
给定两个有序整数数组 nums1和nums2，将nums2合并到 nums1 中，使得 num1成为一个有序数组。

说明:
初始化 nums1和nums2的元素数量分别为 m和n。
你可以假设 nums1 有足够的空间（空间大小大于或等于 m + n）来保存nums2中的元素。

示例:
输入:
nums1 = [1, 2, 3, 0, 0, 0], m = 3
nums2 = [2, 5, 6], n = 3
输出: [1, 2, 2, 3, 5, 6]
"""


class Solution:
    @staticmethod
    def merge_1(nums1: list, m: int, nums2: list, n: int):
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # 逆序双指针
        p1 = m - 1
        p2 = n - 1
        p = m + n - 1
        while p1 >= 0 and p2 >= 0:
            if nums1[p1] < nums2[p2]:
                nums1[p] = nums2[p2]
                p2 -= 1
            else:
                nums1[p] = nums1[p1]
                p1 -= 1
            p -= 1
        nums1[:p2 + 1] = nums2[:p2 + 1]
        print(nums1)


if __name__ == '__main__':
    Solution.merge_1([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3)
