"""
  * @FileName: s343_integer-break.py
  * @Author:   zzc
  * @Date:     2020年11月28日 11:12:20
  * @Version   V1.0.0
"""

"""
给定一个正整数n，将其拆分为至少两个正整数的和，并使这些整数的乘积最大化。 返回你可以获得的最大乘积。

示例 1:
输入: 2
输出: 1
解释: 2 = 1 + 1, 1 × 1 = 1。

示例2:
输入: 10
输出: 36
解释: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36。

说明: 你可以假设n不小于 2 且不大于 58。
"""


class Solution:
    def __init__(self):
        self.memory = list()  # 记忆化搜索

    def integerBreak(self, n):
        self.memory = [-1 for i in range(n + 1)]
        return self._split(n)

    def _split(self, n):
        if n == 1:
            return 1
        if self.memory[n] != -1:
            return self.memory[n]
        # 切分为i和n - i
        res = -1
        for i in range(1, n):
            res = max(res, i * (n - i), i * self._split(n - i))
        self.memory[n] = res
        return res

    def integerBreak2(self, n):
        # dp
        memory = [-1 for i in range(n + 1)]
        memory[1] = 1
        # 外部的循环求出memory[i]的最大值
        for i in range(2, n + 1):
            # 内部的循环是对i进行切分
            for j in range(1, i):
                memory[i] = max(memory[i], j * (i - j), j * memory[i - j])
        return memory[n]


if __name__ == '__main__':
    print(Solution().integerBreak2(10))
