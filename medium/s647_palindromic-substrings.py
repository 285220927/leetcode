"""
  * @FileName: s647_palindromic-substrings.py
  * @Author:   zzc
  * @Date:     2020年12月10日 20:09:34
  * @Version   V1.0.0
"""

"""
给定一个字符串，你的任务是计算这个字符串中有多少个回文子串。
具有不同开始位置或结束位置的子串，即使是由相同的字符组成，也会被视作不同的子串。

示例 1：
输入："abc"
输出：3
解释：三个回文子串: "a", "b", "c"

示例 2：
输入："aaa"
输出：6
解释：6个回文子串: "a", "a", "a", "aa", "aa", "aaa"

提示：
输入的字符串长度不会超过 1000 。
"""


class Solution:
    def countSubstrings(self, s):
        n = len(s)
        dp = [[False for i in range(n)] for j in range(n)]
        res = 0
        for i in range(n):
            for j in range(i, -1, -1):
                # 计算[s[j] ... s[i]] 之间是否为回文串
                # 在 s[j] == s[i] 时 如果字串的长度为1或2或3时 字串一定是回文串
                # 或者 s[j + 1] 到 s[i - 1] 是回文串 那么 s[j] 到 s[i] 也是回文串
                if s[i] == s[j] and (i - j < 3 or dp[j + 1][i - 1]):
                    res += 1
                    dp[j][i] = True
        return res


if __name__ == '__main__':
    print(Solution().countSubstrings("abc"))
    print(Solution().countSubstrings("aaa"))
    print(Solution().countSubstrings("abcba"))
