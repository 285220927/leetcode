"""
  * @FileName: s349_intersection_of_two_arrays.py
  * @Author:   zzc
  * @Date:     2020年02月16日 13:28:58
  * @Version   V1.0.0
"""

"""
给定两个数组，编写一个函数来计算它们的交集。

示例 1:
输入: nums1 = [1,2,2,1], nums2 = [2,2]
输出: [2]

示例 2:
输入: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
输出: [9,4]

说明:
输出结果中的每个元素一定是唯一的。
我们可以不考虑输出结果的顺序。
"""


class Solution:
    @staticmethod
    def intersection_1(nums1, nums2):
        num_set = set(nums1)
        res = []
        for i in nums2:
            if i in num_set:
                res.append(i)
                num_set.remove(i)
        return res


if __name__ == '__main__':
    print(Solution.intersection_1([1, 2, 2, 1], [2, 2]))
