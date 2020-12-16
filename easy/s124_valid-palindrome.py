"""
  * @FileName: s124_valid-palindrome.py
  * @Author:   zzc
  * @Date:     2020年12月06日 10:45:31
  * @Version   V1.0.0
"""

"""
给定一个字符串，验证它是否是回文串，只考虑字母和数字字符，可以忽略字母的大小写。
说明：本题中，我们将空字符串定义为有效的回文串。

示例 1:
输入: "A man, a plan, a canal: Panama"
输出: true

示例 2:
输入: "race a car"
输出: false
"""


class Solution:
    def isPalindrome(self, s):
        n = len(s)
        if n == 0:
            return True
        s = s.lower()
        l, r = 0, n - 1
        while l < r:
            if not 97 <= ord(s[l]) <= 122 and not 48 <= ord(s[l]) <= 57:
                l += 1
                continue
            if not 97 <= ord(s[r]) <= 122 and not 48 <= ord(s[r]) <= 57:
                r -= 1
                continue
            if s[l] != s[r]:
                return False
            else:
                l += 1
                r -= 1
        return True


print(Solution().isPalindrome("ab2a"))
