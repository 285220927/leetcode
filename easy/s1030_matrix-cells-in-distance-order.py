"""
  * @FileName: s1030_matrix-cells-in-distance-order.py
  * @Author:   zzc
  * @Date:     2020年11月17日 19:37:52
  * @Version   V1.0.0
"""
from queue import Queue

"""
给出 R 行 C 列的矩阵，其中的单元格的整数坐标为 (r, c)，满足 0 <= r < R 且 0 <= c < C。
另外，我们在该矩阵中给出了一个坐标为(r0, c0) 的单元格。
返回矩阵中的所有单元格的坐标，并按到 (r0, c0) 的距离从最小到最大的顺序排，其中，两单元格(r1, c1) 和 (r2, c2) 之间的距离是曼哈顿距离，|r1 - r2| + |c1 - c2|。
（你可以按任何满足此条件的顺序返回答案。）

示例 1：
输入：R = 1, C = 2, r0 = 0, c0 = 0
输出：[[0,0],[0,1]]
解释：从 (r0, c0) 到其他单元格的距离为：[0,1]

示例 2：
输入：R = 2, C = 2, r0 = 0, c0 = 1
输出：[[0,1],[0,0],[1,1],[1,0]]
解释：从 (r0, c0) 到其他单元格的距离为：[0,1,1,2]
[[0,1],[1,1],[0,0],[1,0]] 也会被视作正确答案。

示例 3：
输入：R = 2, C = 3, r0 = 1, c0 = 2
输出：[[1,2],[0,2],[1,1],[0,1],[1,0],[0,0]]
解释：从 (r0, c0) 到其他单元格的距离为：[0,1,1,2,2,3]
其他满足题目要求的答案也会被视为正确，例如 [[1,2],[1,1],[0,2],[1,0],[0,1],[0,0]]。

提示：
1 <= R <= 100
1 <= C <= 100
0 <= r0 < R
0 <= c0 < C
"""


class Solution:
    def allCellsDistOrder(self, R, C, r0, c0):
        dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        visited = [False] * (R * C)
        res = []
        queue = Queue()
        queue.put(r0 * C + c0)
        res.append([r0, c0])
        while not queue.empty():
            v = queue.get()
            visited[v] = True
            x = int(v / C)
            y = v % C
            for i in range(4):
                next_x = x + dirs[i][0]
                next_y = y + dirs[i][1]
                next_v = next_x * C + next_y
                # 是否出界
                if 0 <= next_x < R and 0 <= next_y < C and not visited[next_v]:
                    res.append([next_x, next_y])
                    if len(res) == R * C:
                        return res
                    visited[next_v] = True
                    queue.put(next_v)
        return res


if __name__ == '__main__':
    print(Solution().allCellsDistOrder(2, 3, 1, 2))

