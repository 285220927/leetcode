"""
  * @FileName: s1504_count-submatrices-with-all-ones.py
  * @Author:   zzc
  * @Date:     2020年12月12日 11:12:42
  * @Version   V1.0.0
"""
import sys

"""
给你一个只包含 0 和 1 的 rows * columns 矩阵 mat ，请你返回有多少个 子矩形 的元素全部都是 1 。

示例 1：
输入：mat = [[1,0,1],
            [1,1,0],
            [1,1,0]]
输出：13
解释：
有 6 个 1x1 的矩形。
有 2 个 1x2 的矩形。
有 3 个 2x1 的矩形。
有 1 个 2x2 的矩形。
有 1 个 3x1 的矩形。
矩形数目总共 = 6 + 2 + 3 + 1 + 1 = 13 。

示例 2：
输入：mat = [[0,1,1,0],
            [0,1,1,1],
            [1,1,1,0]]
输出：24
解释：
有 8 个 1x1 的子矩形。
有 5 个 1x2 的子矩形。
有 2 个 1x3 的子矩形。
有 4 个 2x1 的子矩形。
有 2 个 2x2 的子矩形。
有 2 个 3x1 的子矩形。
有 1 个 3x2 的子矩形。
矩形数目总共 = 8 + 5 + 2 + 4 + 2 + 2 + 1 = 24 。

示例 3：
输入：mat = [[1,1,1,1,1,1]]
输出：21

示例 4：
输入：mat = [[1,0,1],[0,1,0],[1,0,1]]
输出：5

提示：
1 <= rows <= 150
1 <= columns <= 150
0 <= mat[i][j] <= 1
"""


class Solution:
    def numSubmat(self, mat):
        if not len(mat) or not len(mat[0]):
            return 0
        r, c = len(mat), len(mat[0])
        dp = [[0 for _ in range(c)] for _ in range(r)]
        dp[0][0] = mat[0][0]
        res = 0
        for i in range(r):
            for j in range(c):
                if mat[i][j]:
                    dp[i][j] = 1 if not j else dp[i][j - 1] + 1
                    m = sys.maxsize
                    for k in range(i, -1, -1):
                        m = min(m, dp[k][j])
                        res += m
                        if m == 0:
                            break
        return res


"""
输入：mat = [[0, 1, 1, 0],
            [0, 1, 1, 1],
            [1, 1, 1, 0]
"""

if __name__ == '__main__':
    print(Solution().numSubmat([[0, 1, 1, 0], [0, 1, 1, 1], [1, 1, 1, 0]]))
