"""
  * @FileName: s7_reverse_integer.py
  * @Author:   zzc
  * @Date:     2020年01月26日 11:46:18
  * @Version   V1.0.0
"""

"""
给出一个32位的有符号整数，你需要将这个整数中每位上的数字进行反转。

示例1:
输入: 123
输出: 321

示例2:
输入: -123
输出: -321

示例3:
输入: 120
输出: 21

注意:
假设我们的环境只能存储得下32位的有符号整数，则其数值范围为 [−2的31次方,  2的31次方 − 1]。请根据这个假设，如果反转后整数溢出那么就返回 0。
"""


class Solution:
    @staticmethod
    def reverse_1(x: int):
        if x == 0 or x == -0:
            return 0
        x = str(x)
        li = list(x)
        is_negative_number = False
        if li[0] == '-':
            li.pop(0)
            is_negative_number = True
        li.reverse()
        if is_negative_number:
            li.insert(0, '-')
        x = int(''.join(li))
        if x > pow(2, 31) - 1 or x < pow(2, 31) * -1:
            return 0
        return x


if __name__ == '__main__':
    print(Solution.reverse_1(1563847412))
