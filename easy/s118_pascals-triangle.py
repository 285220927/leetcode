"""
  * @FileName: s118_pascals-triangle.py
  * @Author:   zzc
  * @Date:     2020年12月06日 11:00:10
  * @Version   V1.0.0
"""

"""
给定一个非负整数 numRows，生成杨辉三角的前 numRows 行。
在杨辉三角中，每个数是它左上方和右上方的数的和。

示例:

输入: 5
输出:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
"""


class Solution:
    def generate(self, numRows):
        res = [[] for i in range(numRows)]
        for i in range(numRows):
            res[i] = [1 for j in range(i + 1)]
        if numRows <= 2:
            return res
        for i in range(1, numRows - 1):
            for j in range(1, i + 1):
                res[i + 1][j] = res[i][j] + res[i][j - 1]
        return res


if __name__ == '__main__':
    print(Solution().generate(5))
