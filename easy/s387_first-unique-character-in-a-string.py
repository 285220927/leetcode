"""
  * @FileName: s387_first-unique-character-in-a-string.py
  * @Author:   zzc
  * @Date:     2020年12月23日 21:25:09
  * @Version   V1.0.0
"""

"""
给定一个字符串，找到它的第一个不重复的字符，并返回它的索引。如果不存在，则返回 -1。

示例：
s = "leetcode"
返回 0
s = "loveleetcode"
返回 2

提示：你可以假定该字符串只包含小写字母。
"""


class Solution:
    def firstUniqChar(self, s: str) -> int:
        dic1 = {}
        dic2 = {}
        for i in range(0, len(s)):
            dic1[s[i]] = 1 if not dic1.get(s[i]) else dic1[s[i]] + 1
            dic2[s[i]] = i
        for k, v in dic1.items():
            if v == 1:
                return dic2[k]
        return -1


if __name__ == '__main__':
    print(Solution().firstUniqChar('aa'))
