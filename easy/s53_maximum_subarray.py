"""
  * @FileName: s53_maximum_subarray.py
  * @Author:   zzc
  * @Date:     2020年01月29日 11:17:02
  * @Version   V1.0.0
"""

"""
给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

示例:
输入: [-2,1,-3,4,-1,2,1,-5,4],
输出: 6
解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。
"""


class Solution:
    @staticmethod
    def max_sub_array_1(nums: list):
        max_sum = None
        for i in range(len(nums)):
            for j in range(i, len(nums) + 1):
                cur_num = sum(nums[i: j + 1])
                max_sum = cur_num if max_sum is None or cur_num > max_sum else max_sum
        return max_sum

    @staticmethod
    def max_sub_array_2(nums: list):
        # 动态规划
        for i in range(1, len(nums)):
            nums[i] = nums[i] + max(nums[i - 1], 0)
            # [-2, 1, -2, 4, 3, 5, 6, 1, 5]
        return max(nums)


if __name__ == '__main__':
    print(Solution.max_sub_array_1([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
    print(Solution.max_sub_array_2([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
