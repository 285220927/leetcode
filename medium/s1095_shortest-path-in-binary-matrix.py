"""
  * @FileName: s1095_shortest-path-in-binary-matrix.py
  * @Author:   zzc
  * @Date:     2020年10月26日 21:14:43
  * @Version   V1.0.0
"""
import queue

"""
1091. 二进制矩阵中的最短路径
在一个 N × N 的方形网格中，每个单元格有两种状态：空（0）或者阻塞（1）。

一条从左上角到右下角、长度为 k 的畅通路径，由满足下述条件的单元格 C_1, C_2, ..., C_k 组成：

相邻单元格 C_i 和 C_{i+1} 在八个方向之一上连通（此时，C_i 和 C_{i+1} 不同且共享边或角）
C_1 位于 (0, 0)（即，值为 grid[0][0]）
C_k 位于 (N-1, N-1)（即，值为 grid[N-1][N-1]）
如果 C_i 位于 (r, c)，则 grid[r][c] 为空（即，grid[r][c] == 0）
返回这条从左上角到右下角的最短畅通路径的长度。如果不存在这样的路径，返回 -1 。

提示：

1 <= grid.length == grid[0].length <= 100
grid[i][j] 为 0 或 1
"""


class Solution:
    # bfs
    def __init__(self):
        self.dirs = [[-1, 0], [-1, -1], [0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, 1]]
        self.q = queue.Queue()

    def shortestPathBinaryMatrix(self, grid):
        if grid[0][0] == 1:
            return -1
        self.row = len(grid)
        self.column = len(grid[0])
        if self.row == self.column == 1:
            return 1

        # 坑!
        # visited = []
        # distance = []
        # v_arr = [False] * self.row
        # d_arr = [None] * self.row
        # for i in range(self.column):
        #     visited.append(v_arr)
        #     distance.append(d_arr)

        visited = [[False] * self.row for i in range(self.column)]
        distance = [[None] * self.row for i in range(self.column)]

        visited[0][0] = True
        distance[0][0] = 1
        self.q.put(0)
        while not self.q.empty():
            v = self.q.get()
            x = int(v / self.column)
            y = v % self.column
            for i in range(8):
                next_x = x + self.dirs[i][0]
                next_y = y + self.dirs[i][1]
                if self._in_area(next_x, next_y) and not visited[next_x][next_y] and grid[next_x][next_y] == 0:
                    self.q.put(next_x * self.column + next_y)
                    visited[next_x][next_y] = True
                    distance[next_x][next_y] = distance[x][y] + 1
                    if next_x == self.row - 1 and next_y == self.column - 1:
                        return distance[next_x][next_y]
        return -1

    def _in_area(self, x, y):
        return 0 <= x < self.row and 0 <= y < self.column


if __name__ == '__main__':
    print(Solution().shortestPathBinaryMatrix([[0, 1], [1, 0]]))
