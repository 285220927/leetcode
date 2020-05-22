"""
  * @FileName: s70_climbing_stairs.py
  * @Author:   zzc
  * @Date:     2020年01月31日 12:08:44
  * @Version   V1.0.0
"""

"""
假设你正在爬楼梯。需要 n 阶你才能到达楼顶。
每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？
注意：给定 n 是一个正整数。

示例 1：
输入： 2
输出： 2
解释： 有两种方法可以爬到楼顶。
1.  1 阶 + 1 阶
2.  2 阶

示例 2：
输入： 3
输出： 3
解释： 有三种方法可以爬到楼顶。
1.  1 阶 + 1 阶 + 1 阶
2.  1 阶 + 2 阶
3.  2 阶 + 1 阶

1   1
2   2
3   3
4   5
5   8
6   13
"""


class Solution:
    @staticmethod
    def climb_stairs_1(n: int):
        li = [1]
        for i in range(1, n):
            li.append(li[i - 1] + li[i - 2])
        return li[n - 1]

    @staticmethod
    def climb_stairs_2(n: int):
        if n == 1:
            return 1
        i1 = 1
        i2 = 2
        for i in range(2, n):
            temp = i2
            i2 += i1
            i1 = temp
        return i2


if __name__ == '__main__':
    print(Solution.climb_stairs_1(100))
    print(Solution.climb_stairs_2(100))
