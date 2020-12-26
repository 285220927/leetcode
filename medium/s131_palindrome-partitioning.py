"""
  * @FileName: s131_palindrome-partitioning.py
  * @Author:   zzc
  * @Date:     2020年12月19日 16:20:15
  * @Version   V1.0.0
"""
from typing import List

"""
给定一个字符串 s，将 s 分割成一些子串，使每个子串都是回文串。
返回 s 所有可能的分割方案。

示例:
输入: "aab"
输出:
[
  ["aa","b"],
  ["a","a","b"]
]
"""


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        if not s:
            return [[]]
        if len(s) == 1:
            return [[s]]
        res = []
        for i in range(1, len(s) + 1):
            left = s[: i]
            right = s[i:]
            if left == left[::-1]:
                right = self.partition(right)
                for i in right:
                    res.append([left] + i)
        return res
