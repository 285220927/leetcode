"""
  * @FileName: s1277_count-square-submatrices-with-all-ones.py
  * @Author:   zzc
  * @Date:     2020年12月07日 20:39:04
  * @Version   V1.0.0
"""

"""
给你一个  m * n  的矩阵，矩阵中的元素不是 0 就是 1，请你统计并返回其中完全由 1 组成的 正方形 子矩阵的个数。

示例 1：
输入：matrix =
[
   [0,1,1,1],
   [1,1,1,1],
   [0,1,1,1]
]
输出：15
解释： 
边长为 1 的正方形有 10 个。
边长为 2 的正方形有 4 个。
边长为 3 的正方形有 1 个。
正方形的总数 = 10 + 4 + 1 = 15.

示例 2：
输入：matrix = 
[
  [1,0,1],
  [1,1,0],
  [1,1,0]
]
输出：7
解释：
边长为 1 的正方形有 6 个。 
边长为 2 的正方形有 1 个。
正方形的总数 = 6 + 1 = 7.

提示：
1 <= arr.length  <= 300
1 <= arr[0].length  <= 300
0 <= arr[i][j] <= 1
"""


class Solution:
    def countSquares(self, matrix):
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return 0
        r, c = len(matrix), len(matrix[0])
        dp = [[0 for i in range(len(matrix[0]))] for j in range(len(matrix))]
        dp[0][0] = matrix[0][0]
        res = 0
        for i in range(r):
            for j in range(c):
                if matrix[i][j] != 0:
                    if i != 0 and j != 0:
                        dp[i][j] = min(dp[i - 1][j], dp[i - 1][j - 1], dp[i][j - 1]) + 1
                    else:
                        dp[i][j] = 1
                    res += dp[i][j]
        return res


if __name__ == '__main__':
    """
    0 1 1 1
    1 1 2 2
    0 1 2 3
    """
    print(Solution().countSquares([
        [0, 1, 1, 1],
        [1, 1, 1, 1],
        [0, 1, 1, 1]
    ]))
