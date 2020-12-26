"""
  * @FileName: s46_permutations.py
  * @Author:   zzc
  * @Date:     2020年12月19日 16:32:15
  * @Version   V1.0.0
"""
from copy import deepcopy
from typing import List

"""
给定一个 没有重复 数字的序列，返回其所有可能的全排列。

示例:
输入: [1,2,3]
输出:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
"""


class Solution:
    def __init__(self):
        self.res = []

    def permute(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
        self.visited = [False] * len(nums)
        self.helper(nums, 0, [])
        return self.res

    def helper(self, nums, idx, aux):
        if idx == len(nums):
            self.res.append(deepcopy(aux))
            return
        for i in range(len(nums)):
            if not self.visited[i]:
                self.visited[i] = True
                aux.append(nums[i])
                self.helper(nums, idx + 1, aux)
                aux.remove(nums[i])
                self.visited[i] = False
        return


if __name__ == '__main__':
    print(Solution().permute([1, 2, 3]))
