"""
  * @FileName: s200_number-of-islands.py
  * @Author:   zzc
  * @Date:     2020年12月26日 10:37:03
  * @Version   V1.0.0
"""
from typing import List

"""
给你一个由 '1'（陆地）和 '0'（水）组成的的二维网格，请你计算网格中岛屿的数量。
岛屿总是被水包围，并且每座岛屿只能由水平方向和/或竖直方向上相邻的陆地连接形成。
此外，你可以假设该网格的四条边均被水包围。

示例 1：
输入：grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
输出：1

示例 2：
输入：grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
输出：3

提示：
m == grid.length
n == grid[i].length
1 <= m, n <= 300
grid[i][j] 的值为 '0' 或 '1'
"""


class Solution:
    def __init__(self):
        self.dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]]

    def numIslands(self, grid: List[List[str]]) -> int:
        self.r = len(grid)
        self.c = len(grid[0])
        res = 0
        self.visited = [[False for _ in range(self.c)] for _ in range(self.r)]
        for i in range(self.r):
            for j in range(self.c):
                if not self.visited[i][j] and grid[i][j] == '1':
                    self.dfs(grid, i, j)
                    res += 1
        return res

    def dfs(self, grid, x, y):
        self.visited[x][y] = True
        for i in range(4):
            next_x = x + self.dirs[i][0]
            next_y = y + self.dirs[i][1]
            if 0 <= next_x < self.r and 0 <= next_y < self.c and grid[next_x][next_y] == '1' and not \
            self.visited[next_x][next_y]:
                self.dfs(grid, next_x, next_y)


if __name__ == '__main__':
    print(Solution().numIslands([
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"]
    ]))
