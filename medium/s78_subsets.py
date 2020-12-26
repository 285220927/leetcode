"""
  * @FileName: s78_subsets.py
  * @Author:   zzc
  * @Date:     2020年12月21日 22:46:08
  * @Version   V1.0.0
"""
from copy import deepcopy
from typing import List

"""
给定一组不含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。

说明：解集不能包含重复的子集。

示例:

输入: nums = [1,2,3]
输出:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
"""


class Solution:
    def __init__(self):
        self.res = [[]]

    def subsets(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return [[]]
        for i in range(1, len(nums) + 1):
            self.helper(nums, 0, i, [])
        return self.res

    def helper(self, nums, start, count, aux):
        if len(aux) == count:
            self.res.append(deepcopy(aux))
            return
        for i in range(start, len(nums)):
            aux.append(nums[i])
            self.helper(nums, i + 1, count, aux)
            aux.pop()


if __name__ == '__main__':
    print(Solution().subsets([1, 2, 3]))
