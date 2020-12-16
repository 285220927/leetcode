"""
  * @FileName: s1025_divisor-game.py
  * @Author:   zzc
  * @Date:     2020年12月02日 20:35:59
  * @Version   V1.0.0
"""

"""
爱丽丝和鲍勃一起玩游戏，他们轮流行动。爱丽丝先手开局。
最初，黑板上有一个数字 N 。在每个玩家的回合，玩家需要执行以下操作：
选出任一 x，满足 0 < x < N 且 N % x == 0 。
用 N - x 替换黑板上的数字 N 。
如果玩家无法执行这些操作，就会输掉游戏。
只有在爱丽丝在游戏中取得胜利时才返回 True，否则返回 False。假设两个玩家都以最佳状态参与游戏。

示例 1：
输入：2
输出：true
解释：爱丽丝选择 1，鲍勃无法进行操作。

示例 2：
输入：3
输出：false
解释：爱丽丝选择 1，鲍勃也选择 1，然后爱丽丝无法进行操作。

提示：
1 <= N <= 1000
"""


class Solution:
    def divisorGame(self, N):
        if N == 1:
            return False
        if N == 2:
            return True
        dp = [False for i in range(N + 1)]
        dp[1] = False
        dp[2] = True
        for i in range(3, N + 1):
            for j in range(1, i):
                if i % j == 0 and not dp[i - j]:
                    dp[i] = True
                    break
        return dp[N]


if __name__ == '__main__':
    print(Solution().divisorGame(4))
