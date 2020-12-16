"""
  * @FileName: s62_unique-paths.py
  * @Author:   zzc
  * @Date:     2020年12月09日 19:58:21
  * @Version   V1.0.0
"""

"""
一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为 “Start” ）。
机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为 “Finish” ）。
问总共有多少条不同的路径？

示例 1：
输入：m = 3, n = 7
输出：28

示例 2：
输入：m = 3, n = 2
输出：3
解释：
从左上角开始，总共有 3 条路径可以到达右下角。
1. 向右 -> 向右 -> 向下
2. 向右 -> 向下 -> 向右
3. 向下 -> 向右 -> 向右

示例 3：
输入：m = 7, n = 3
输出：28

示例 4：
输入：m = 3, n = 3
输出：6

提示：
1 <= m, n <= 100
题目数据保证答案小于等于 2 * 109
"""


class Solution:
    def uniquePaths(self, m, n):
        if m == 1 or n == 1:
            return 1
        if m > n:
            m, n = n, m
        dp = [1 for _ in range(m)]
        for i in range(1, n):
            for j in range(1, m):
                dp[j] += dp[j - 1]
        return dp[-1]


if __name__ == '__main__':
    print(Solution().uniquePaths(3, 7))