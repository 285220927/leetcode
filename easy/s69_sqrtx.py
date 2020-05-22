"""
  * @FileName: s69_sqrtx.py
  * @Author:   zzc
  * @Date:     2020年01月31日 10:37:59
  * @Version   V1.0.0
"""

"""
实现 int sqrt(int x) 函数。
计算并返回 x 的平方根，其中 x 是非负整数。
由于返回类型是整数，结果只保留整数的部分，小数部分将被舍去。

示例 1:
输入: 4
输出: 2

示例 2:
输入: 8
输出: 2
说明: 8 的平方根是 2.82842..., 
"""


class Solution:
    @staticmethod
    def my_sqrt_1(x: int):
        start = 0
        end = x
        while True:
            mid = (start + end + 1) // 2
            if (mid + 1) ** 2 == x:
                return mid + 1
            elif mid ** 2 < x and (mid + 1) ** 2 < x:
                start = mid + 1
                continue
            elif mid ** 2 > x:
                end = mid - 1
                continue
            elif mid ** 2 <= x < (mid + 1) ** 2:
                return mid


if __name__ == '__main__':
    print(Solution.my_sqrt_1(9))
