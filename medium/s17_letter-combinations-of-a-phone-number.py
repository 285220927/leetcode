"""
  * @FileName: s17_letter-combinations-of-a-phone-number.py
  * @Author:   zzc
  * @Date:     2020年12月19日 10:48:10
  * @Version   V1.0.0
"""
from typing import List

"""
给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。
给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。

示例:
输入："23"
输出：["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
"""


class Solution:
    def __init__(self):
        self.dict = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}

    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        return self.helper(digits, 0)

    def helper(self, digits, idx) -> List[str]:
        if idx == len(digits) - 1:
            res = []
            for i in self.dict[digits[idx]]:
                res.append(i)
            return res
        cur = self.dict[digits[idx]]
        next = self.helper(digits, idx + 1)
        res = []
        for c1 in cur:
            for c2 in next:
                res.append(c1 + c2)
        return res


if __name__ == '__main__':
    print(Solution().letterCombinations('23'))
