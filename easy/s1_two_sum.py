"""
  * @FileName: s1_two_sum.py
  * @Author:   zzc
  * @Date:     2020年01月26日 11:07:12
  * @Version   V1.0.0
"""

"""
给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那两个整数，并返回他们的数组下标。
你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。

示例:
给定 nums = [2, 7, 11, 15], target = 9
因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]
"""


class Solution:
    @staticmethod
    def two_sum_1(nums: list, target: int):
        sorted_id = sorted(range(len(nums)), key=lambda k: nums[k])
        head = 0
        tail = len(nums) - 1
        sum_result = nums[sorted_id[head]] + nums[sorted_id[tail]]
        while sum_result != target:
            if target > sum_result:
                head += 1
            elif target < sum_result:
                tail -= 1
            sum_result = nums[sorted_id[head]] + nums[sorted_id[tail]]
        return [sorted_id[head], sorted_id[tail]]

    @staticmethod
    def two_sum_2(nums: list, target: int):
        dct = {}
        for index, num in enumerate(nums):
            if target - num in dct:
                return [dct[target - num], index]
            dct[num] = index


if __name__ == '__main__':
    print(Solution.two_sum_1([3, 2, 4], 6))
    print(Solution.two_sum_2([3, 2, 4], 6))
