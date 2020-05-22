"""
  * @FileName: s35_search_insert_position.py
  * @Author:   zzc
  * @Date:     2020年01月28日 14:09:24
  * @Version   V1.0.0
"""

"""
给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。
你可以假设数组中无重复元素。

示例 1:
输入: [1,3,5,6], 5
输出: 2

示例 2:
输入: [1,3,5,6], 2
输出: 1

示例 3:
输入: [1,3,5,6], 7
输出: 4

示例 4:
输入: [1,3,5,6], 0
输出: 0
"""


class Solution:
    @staticmethod
    def search_insert_1(nums: list, target: int):
        nums_len = len(nums)
        for i in range(nums_len):
            if nums[i] >= target:
                return i
        return nums_len

    @staticmethod
    def search_insert_2(nums: list, target: int):
        # 用二分法实现
        left = 0
        right = len(nums)
        while left < right:
            mid = int((left + right) / 2)
            if target < nums[mid]:
                right = mid
            elif target > nums[mid]:
                left = mid + 1
            else:
                return mid
        return left


if __name__ == '__main__':
    print(Solution.search_insert_1([1, 3, 5, 6], 5))
    print(Solution.search_insert_2([1, 3], 2))
