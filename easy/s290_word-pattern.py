"""
  * @FileName: s290_word-pattern.py
  * @Author:   zzc
  * @Date:     2020年12月16日 22:19:19
  * @Version   V1.0.0
"""

"""
给定一种规律 pattern 和一个字符串 str ，判断 str 是否遵循相同的规律。
这里的 遵循 指完全匹配，例如， pattern 里的每个字母和字符串 str 中的每个非空单词之间存在着双向连接的对应规律。

示例1:
输入: pattern = "abba", str = "dog cat cat dog"
输出: true

示例 2:
输入:pattern = "abba", str = "dog cat cat fish"
输出: false

示例 3:
输入: pattern = "aaaa", str = "dog cat cat dog"
输出: false

示例 4:
输入: pattern = "abba", str = "dog dog dog dog"
输出: false
说明:
你可以假设 pattern 只包含小写字母， str 包含了由单个空格分隔的小写字母。    
"""


class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        dict = {}
        reverse_dict = {}
        strs = s.split(" ")
        length = len(strs)
        if length != len(pattern):
            return False
        for i in range(length):
            if not dict.get(pattern[i]):
                dict[pattern[i]] = strs[i]
            if not reverse_dict.get(strs[i]):
                if dict[pattern[i]] != strs[i]:
                    return False
                reverse_dict[strs[i]] = pattern[i]
            elif dict[pattern[i]] != strs[i] or reverse_dict[strs[i]] != pattern[i]:
                return False
        return True
