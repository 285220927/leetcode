"""
  * @FileName: s77_combinations.py
  * @Author:   zzc
  * @Date:     2020年12月20日 12:56:55
  * @Version   V1.0.0
"""
from copy import deepcopy
from typing import List

"""
给定两个整数 n 和 k，返回 1 ... n 中所有可能的 k 个数的组合。

示例:
输入: n = 4, k = 2
输出:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]
"""


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        self.res = []
        if n <= 0 or k <= 0 or k > n:
            return self.res
        self.helper(n, k, 1, [])
        return self.res

    def helper(self, n, k, start, aux):
        if len(aux) == k:
            self.res.append(deepcopy(aux))
            return
        for i in range(start, n - (k - len(aux)) + 2):
            aux.append(i)
            self.helper(n, k, i + 1, aux)
            aux.pop()
        return


if __name__ == '__main__':
    print(Solution().combine(4, 2))
