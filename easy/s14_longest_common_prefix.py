"""
  * @FileName: s14_longest_common_prefix.py
  * @Author:   zzc
  * @Date:     2020年01月27日 10:30:48
  * @Version   V1.0.0
"""

"""
编写一个函数来查找字符串数组中的最长公共前缀。
如果不存在公共前缀，返回空字符串 ""。

示例 1:
输入: ["flower","flow","flight"]
输出: "fl"

示例 2:
输入: ["dog","racecar","car"]
输出: ""
解释: 输入不存在公共前缀。

说明:
所有输入只包含小写字母 a-z 。
"""


class Solution:
    @staticmethod
    def longest_common_prefix_1(strs: list):
        if not strs:
            return ""
        s1 = max(strs)
        s2 = min(strs)
        for i, x in enumerate(s1):
            if len(s1) != len(s2) and (i == len(s1) or i == len(s2)):
                return s2
            else:
                if x != s2[i]:
                    return s2[:i]
        return s1


if __name__ == '__main__':
    print(Solution.longest_common_prefix_1(["ac", "ab"]))
