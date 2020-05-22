"""
  * @FileName: s9_palindrome_number.py
  * @Author:   zzc
  * @Date:     2020年01月26日 12:30:40
  * @Version   V1.0.0
"""

"""
判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。

示例1:
输入: 121
输出: true

示例2:
输入: -121
输出: false
解释: 从左向右读, 为 -121 。 从右向左读, 为 121- 。因此它不是一个回文数。

示例3:
输入: 10
输出: false
解释: 从右向左读, 为 01 。因此它不是一个回文数。
"""


class Solution:
    @staticmethod
    def is_palindrome_1(x: int):
        if x < 0:
            return False
        x = str(x)
        for i in range(len(x)):
            if x[i] != x[len(x) - i - 1]:
                return False
            if i == int(len(x) / 2):
                break
        return True

    @staticmethod
    def is_palindrome_2(x: int):
        li1 = list(str(x))
        li2 = list(str(x))
        li2.reverse()
        return li1 == li2

    @staticmethod
    def is_palindrome_3(x: int):
        return str(x) == str(x)[::-1]


if __name__ == '__main__':
    print(Solution.is_palindrome_1(112211))
    print(Solution.is_palindrome_2(112211))
    print(Solution.is_palindrome_2(112211))
