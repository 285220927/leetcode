"""
  * @FileName: s39_combination-sum.py
  * @Author:   zzc
  * @Date:     2020年12月23日 20:24:27
  * @Version   V1.0.0
"""
from copy import deepcopy
from typing import List

"""
给定一个无重复元素的数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。
candidates 中的数字可以无限制重复被选取。

说明：
所有数字（包括 target）都是正整数。
解集不能包含重复的组合。 

示例 1：
输入：candidates = [2,3,6,7], target = 7,
所求解集为：
[
  [7],
  [2,2,3]
]

示例 2：
输入：candidates = [2,3,5], target = 8,
所求解集为：
[
  [2,2,2,2],
  [2,3,3],
  [3,5]
]

提示：
1 <= candidates.length <= 30
1 <= candidates[i] <= 200
candidate 中的每个元素都是独一无二的。
1 <= target <= 500
"""


class Solution:
    def __init__(self):
        self.res = []

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        if not candidates:
            return []
        candidates = sorted(candidates)
        self.helper(candidates, 0, target, [])
        return self.res

    def helper(self, candidates, idx, target, aux):
        if target == 0:
            self.res.append(deepcopy(aux))
            return
        for i in range(idx, len(candidates)):
            if candidates[i] > target:
                break
            aux.append(candidates[i])
            self.helper(candidates, i, target - candidates[i], aux)
            aux.pop()


if __name__ == '__main__':
    print(Solution().combinationSum([2, 3, 5], 8))
