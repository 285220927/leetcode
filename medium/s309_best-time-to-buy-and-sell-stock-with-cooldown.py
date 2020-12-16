"""
  * @FileName: s309_best-time-to-buy-and-sell-stock-with-cooldown.py
  * @Author:   zzc
  * @Date:     2020年12月11日 20:14:41
  * @Version   V1.0.0
"""

"""
给定一个整数数组，其中第 i 个元素代表了第 i 天的股票价格 。
设计一个算法计算出最大利润。在满足以下约束条件下，你可以尽可能地完成更多的交易（多次买卖一支股票）:
你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
卖出股票后，你无法在第二天买入股票 (即冷冻期为 1 天)。

示例:
输入: [1,2,3,0,2]
输出: 3
解释: 对应的交易状态为: [买入, 卖出, 冷冻期, 买入, 卖出]
"""

"""
dp[i][0] 表示第 i 天持有股票
dp[i][1] 表示第 i 天不持有股票，且处于冷冻期
dp[i][2] 表示第 i 天不持有股票，且不处于冷冻期
"""


class Solution:
    def maxProfit1(self, prices):
        n = len(prices)
        if n <= 1:
            return 0
        dp = [[0 for _ in range(3)] for _ in range(n)]
        dp[0][0] = -prices[0]
        dp[0][1] = dp[0][2] = 0
        for i in range(1, n):
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][2] - prices[i])
            dp[i][1] = dp[i - 1][0] + prices[i]
            dp[i][2] = max(dp[i - 1][2], dp[i - 1][1])
        return max(dp[n - 1][1], dp[n - 1][2])

    def maxProfit2(self, prices):
        # 空间复杂度优化
        n = len(prices)
        if n <= 1:
            return 0
        f0, f1, f2 = -prices[0], 0, 0
        for i in range(1, n):
            t0 = max(f0, f2 - prices[i])
            t1 = f0 + prices[i]
            f2 = max(f1, f2)
            f0, f1 = t0, t1
        return max(f1, f2)


if __name__ == '__main__':
    print(Solution().maxProfit2([1, 2, 3, 0, 2]))
