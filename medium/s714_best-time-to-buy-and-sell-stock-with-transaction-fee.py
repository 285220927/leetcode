"""
  * @FileName: s714_best-time-to-buy-and-sell-stock-with-transaction-fee.py
  * @Author:   zzc
  * @Date:     2020年12月08日 19:39:53
  * @Version   V1.0.0
"""

"""
给定一个整数数组 prices，其中第 i 个元素代表了第 i 天的股票价格 ；非负整数 fee 代表了交易股票的手续费用。
你可以无限次地完成交易，但是你每笔交易都需要付手续费。如果你已经购买了一个股票，在卖出它之前你就不能再继续购买股票了。
返回获得利润的最大值。
注意：这里的一笔交易指买入持有并卖出股票的整个过程，每笔交易你只需要为支付一次手续费。

示例 1:
输入: prices = [1, 3, 2, 8, 4, 9], fee = 2
输出: 8
解释: 能够达到的最大利润:  
在此处买入 prices[0] = 1
在此处卖出 prices[3] = 8
在此处买入 prices[4] = 4
在此处卖出 prices[5] = 9
总利润: ((8 - 1) - 2) + ((9 - 4) - 2) = 8.

注意:
0 < prices.length <= 50000.
0 < prices[i] < 50000.
0 <= fee < 50000.
"""


class Solution:
    def maxProfit(self, prices, fee):
        n = len(prices)
        if n < 2:
            return 0
        dp = [[0, 0] for _ in range(n)]
        # dp[i][0] 表示第i天不持股，dp[i][1] 表示第i天持股，由第i - 1天转换而来
        dp[0][0] = 0
        dp[0][1] = -prices[0]
        for i in range(1, n):
            # 第i天不持股 = max(前一天不持股(什么都不做)， 前一天持股(卖出，需要扣除手续费))
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i] - fee)
            # 第i天持股 = max(前一天持股(什么都不做)，前一天不持股(买入))
            dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] - prices[i])
        return dp[n - 1][0]


if __name__ == '__main__':
    print(Solution().maxProfit([1, 3, 2, 8, 4, 9], 2))
