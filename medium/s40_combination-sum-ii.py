"""
  * @FileName: s40_combination-sum-ii.py
  * @Author:   zzc
  * @Date:     2020年12月25日 20:31:00
  * @Version   V1.0.0
"""
from copy import deepcopy
from typing import List

"""
给定一个数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。
candidates 中的每个数字在每个组合中只能使用一次。

说明：
所有数字（包括目标数）都是正整数。
解集不能包含重复的组合。 

示例 1:
输入: candidates = [10,1,2,7,6,1,5], target = 8,
所求解集为:
[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]

示例 2:
输入: candidates = [2,5,2,1,2], target = 5,
所求解集为:
[
  [1,2,2],
  [5]
]
"""


class Solution:
    def __init__(self):
        self.res = []

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        if not candidates:
            return []
        candidates.sort()
        self.helper(candidates, target, 0, [])
        return self.res

    def helper(self, candidates, target, idx, aux):
        # 1 1 2 5 6 7 10
        # target 8
        if not target:
            self.res.append(deepcopy(aux))
            return
        for i in range(idx, len(candidates)):
            if candidates[i] > target:
                break
            if i > idx and candidates[i] == candidates[i - 1]:
                # 在递归层数相同时 不能发生重复
                continue
            aux.append(candidates[i])
            self.helper(candidates, target - candidates[i], i + 1, aux)
            aux.pop()


if __name__ == '__main__':
    print(Solution().combinationSum2([10, 1, 2, 7, 6, 1, 5], 8))
