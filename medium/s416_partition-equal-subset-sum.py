"""
  * @FileName: s416_partition-equal-subset-sum.py
  * @Author:   zzc
  * @Date:     2020年12月05日 14:17:23
  * @Version   V1.0.0
"""

"""
给定一个只包含正整数的非空数组。是否可以将这个数组分割成两个子集，使得两个子集的元素和相等。

注意:
每个数组中的元素不会超过 100
数组的大小不会超过 200

示例 1:
输入: [1, 5, 11, 5]
输出: true
解释: 数组可以分割成 [1, 5, 5] 和 [11].
 
示例 2:
输入: [1, 2, 3, 5]
输出: false
解释: 数组不能分割成两个元素和相等的子集.
"""


class Solution:
    def canPartition(self, nums):
        if len(nums) <= 1:
            return False
        arr_sum = sum(nums)
        if arr_sum & 1 == 1:
            return False
        half = int(arr_sum / 2)
        n = len(nums)
        dp = [False] * (half + 1)
        if nums[0] < len(dp):
            dp[nums[0]] = True
        for i in range(1, n):
            for j in range(half, nums[i] - 1, -1):
                dp[j] = dp[j] or dp[j - nums[i]]
        return dp[half]


if __name__ == '__main__':
    print(Solution().canPartition([9, 5]))
