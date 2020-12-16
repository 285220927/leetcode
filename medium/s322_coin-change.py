"""
  * @FileName: s322_coin-change.py
  * @Author:   zzc
  * @Date:     2020年12月03日 20:34:25
  * @Version   V1.0.0
"""
import queue
import sys

"""
给定不同面额的硬币 coins 和一个总金额 amount。编写一个函数来计算可以凑成总金额所需的最少的硬币个数。如果没有任何一种硬币组合能组成总金额，返回 -1。
你可以认为每种硬币的数量是无限的。

示例 1：
输入：coins = [1, 2, 5], amount = 11
输出：3 
解释：11 = 5 + 5 + 1

示例 2：
输入：coins = [2], amount = 3
输出：-1

示例 3：
输入：coins = [1], amount = 0
输出：0

示例 4：
输入：coins = [1], amount = 1
输出：1

示例 5：
输入：coins = [1], amount = 2
输出：2

提示：
1 <= coins.length <= 12
1 <= coins[i] <= 231 - 1
0 <= amount <= 104
"""


class Solution:
    def coinChange1(self, coins, amount):
        if amount == 0:
            return 0
        dp = [sys.maxsize for i in range(amount + 1)]
        dp[0] = 0
        n = len(coins)
        for i in range(1, amount + 1):
            for j in range(0, n):
                if i >= coins[j]:
                    dp[i] = min(dp[i], dp[i - coins[j]] + 1)
        if dp[amount] == sys.maxsize:
            return -1
        return dp[amount]

    def coinChange2(self, coins, amount):
        # bfs 求amount到0的最短路径
        if amount == 0:
            return 0
        visited = [False for i in range(amount + 1)]
        # 排序的作用是剪枝
        coins = sorted(coins)
        q = queue.Queue()
        q.put(amount)
        step = 1
        while not q.empty():
            for w in range(q.qsize()):
                v = q.get()
                visited[v] = True
                for coin in coins:
                    left = v - coin
                    if left == 0:
                        return step
                    elif left < 0:
                        # 由于已经对coins排序了，left会越来越小，所以一旦left小于0，就可以结束当前循环了
                        break
                    if not visited[left]:
                        visited[left] = True
                        q.put(left)
            step += 1
        return -1


if __name__ == '__main__':
    print(Solution().coinChange2([186, 419, 83, 408], 6249))
