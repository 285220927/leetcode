"""
  * @FileName: s90_subsets-i.py
  * @Author:   zzc
  * @Date:     2020年12月25日 21:32:06
  * @Version   V1.0.0
"""
from copy import deepcopy
from typing import List

"""
给定一个可能包含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。

说明：解集不能包含重复的子集。

示例:
输入: [1,2,2]
输出:
[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]
"""


class Solution:
    def __init__(self):
        self.res = [[]]

    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return self.res
        nums.sort()
        for i in range(1, len(nums) + 1):
            self.helper(nums, i, 0, [])
        return self.res

    def helper(self, nums, count, idx, aux):
        if count == len(aux):
            self.res.append(deepcopy(aux))
            return
        for i in range(idx, len(nums)):
            if i > idx and nums[i] == nums[i - 1]:
                continue
            aux.append(nums[i])
            self.helper(nums, count, i + 1, aux)
            aux.pop()
