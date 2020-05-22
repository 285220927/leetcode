"""
  * @FileName: s67_add_binary.py
  * @Author:   zzc
  * @Date:     2020年01月30日 11:13:43
  * @Version   V1.0.0
"""

"""
给定两个二进制字符串，返回他们的和（用二进制表示）。
输入为非空字符串且只包含数字 1 和 0。

示例 1:
输入: a = "11", b = "1"
输出: "100"

示例 2:
输入: a = "1010", b = "1011"
输出: "10101"

01  01  010
10  10  100
11  11  110
1111 1111 11110
"""


class Solution:
    @staticmethod
    def add_binary_1(a: str, b: str):
        a_len = len(a)
        b_len = len(b)
        if a_len > b_len:
            b = '0' * (a_len - b_len) + b
        elif a_len < b_len:
            a = '0' * (b_len - a_len) + a
        result = ''
        flag = False
        for i in range(len(a) - 1, -1, -1):
            cur = int(a[i]) + int(b[i])
            if flag:
                cur += 1
            if cur == 0 or cur == 1:
                flag = False
                result += str(cur)
            else:
                flag = True
                result += '0' if cur == 2 else '1'
            if i == 0:
                # 最后一次循环
                result += '1' if cur == 2 or cur == 3 else ''
        return result[::-1]


if __name__ == '__main__':
    print(Solution.add_binary_1('1010', '1011'))
