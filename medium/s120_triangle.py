"""
  * @FileName: s120_triangle.py
  * @Author:   zzc
  * @Date:     2020年11月26日 21:44:45
  * @Version   V1.0.0
"""

"""
给定一个三角形，找出自顶向下的最小路径和。每一步只能移动到下一行中相邻的结点上。
相邻的结点 在这里指的是 下标 与 上一层结点下标 相同或者等于 上一层结点下标 + 1 的两个结点。

例如，给定三角形：
[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
自顶向下的最小路径和为 11（即，2 + 3 + 5 + 1 = 11）。

说明：
如果你可以只使用 O(n) 的额外空间（n 为三角形的总行数）来解决这个问题，那么你的算法会很加分。
"""


class Solution:
    def __init__(self):
        self.memory = []

    def minimumTotal(self, triangle):
        x = len(triangle)
        self.memory = [[-1 for i in range(x)] for j in range(x)]  # 记忆
        return self.min(triangle, 0, 0)

    def min(self, triangle, n, m):
        if n == len(triangle) - 1:
            return triangle[n][m]
        if self.memory[n + 1][m] == -1:
            self.memory[n + 1][m] = self.min(triangle, n + 1, m)
        if self.memory[n + 1][m + 1] == -1:
            self.memory[n + 1][m + 1] = self.min(triangle, n + 1, m + 1)
        return triangle[n][m] + min(self.memory[n + 1][m], self.memory[n + 1][m + 1])

    def minimumTotal2(self, triangle):
        # dp
        x = len(triangle)
        memory = [0 for i in range(x + 1)]
        for i in range(x - 1, -1, -1):
            for j in range(i + 1):
                memory[j] = min(memory[j], memory[j + 1]) + triangle[i][j]
        return memory[0]


if __name__ == '__main__':
    """
         [2],
        [3,4],
       [6,5,7],
      [4,1,8,3]
    """
    print(Solution().minimumTotal2([[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]))
