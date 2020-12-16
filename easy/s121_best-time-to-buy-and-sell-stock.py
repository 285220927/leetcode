"""
  * @FileName: s121_best-time-to-buy-and-sell-stock.py
  * @Author:   zzc
  * @Date:     2020年12月04日 21:10:48
  * @Version   V1.0.0
"""

"""
给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。
如果你最多只允许完成一笔交易（即买入和卖出一支股票一次），设计一个算法来计算你所能获取的最大利润。
注意：你不能在买入股票前卖出股票。

示例 1:
输入: [7,1,5,3,6,4]
输出: 5
解释: 在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。
     注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格；同时，你不能在买入前卖出股票。
     
示例 2:
输入: [7,6,4,3,1]
输出: 0
解释: 在这种情况下, 没有交易完成, 所以最大利润为 0。
"""


class Solution:
    def maxProfit(self, prices):
        n = len(prices)
        if n <= 1:
            return 0
        min_price = prices[0]
        max_price = 0
        for i in range(1, n):
            max_price = max(max_price, prices[i] - min_price)
            min_price = min(min_price, prices[i])
        return max_price


if __name__ == '__main__':
    print(Solution().maxProfit([7, 1, 5, 3, 6, 4]))
