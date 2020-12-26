"""
  * @FileName: s216_combination-sum-iii.py
  * @Author:   zzc
  * @Date:     2020年12月25日 21:04:30
  * @Version   V1.0.0
"""
from copy import deepcopy
from typing import List

"""
找出所有相加之和为 n 的 k 个数的组合。组合中只允许含有 1 - 9 的正整数，并且每种组合中不存在重复的数字。

说明：
所有数字都是正整数。
解集不能包含重复的组合。

示例 1:
输入: k = 3, n = 7
输出: [[1,2,4]]

示例 2:
输入: k = 3, n = 9
输出: [[1,2,6], [1,3,5], [2,3,4]]
"""


class Solution:
    def __init__(self):
        self.res = []

    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        self.helper(k, n, 1, [])
        return self.res

    def helper(self, k, n, idx, aux):
        if not k and not n:
            self.res.append(deepcopy(aux))
            return
        for i in range(idx, 10):
            if aux and i == aux[-1]:
                continue
            if i > n:
                break
            aux.append(i)
            self.helper(k - 1, n - i, i + 1, aux)
            aux.pop()
