"""
  * @FileName: s695_max-area-of-island.py
  * @Author:   zzc
  * @Date:     2020年10月25日 11:40:16
  * @Version   V1.0.0
"""

"""
695. 岛屿的最大面积
给定一个包含了一些 0 和 1 的非空二维数组 grid 。
一个 岛屿 是由一些相邻的 1 (代表土地) 构成的组合，这里的「相邻」要求两个 1 必须在水平或者竖直方向上相邻。你可以假设 grid 的四个边缘都被 0（代表水）包围着。
找到给定的二维数组中最大的岛屿面积。(如果没有岛屿，则返回面积为 0 。)

示例 1:
[[0,0,1,0,0,0,0,1,0,0,0,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,1,1,0,1,0,0,0,0,0,0,0,0],
 [0,1,0,0,1,1,0,0,1,0,1,0,0],
 [0,1,0,0,1,1,0,0,1,1,1,0,0],
 [0,0,0,0,0,0,0,0,0,0,1,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,0,0,0,0,0,0,1,1,0,0,0,0]]
对于上面这个给定矩阵应返回 6。注意答案不应该是 11 ，因为岛屿只能包含水平或垂直的四个方向的 1 。

示例 2:
[[0,0,0,0,0,0,0,0]]
对于上面这个给定的矩阵, 返回 0。

注意: 给定的矩阵grid 的长度和宽度都不超过 50。
"""


class Solution:

    def __init__(self):
        self.dirs = [[-1, 0], [0, 1], [1, 0], [0, -1]]
        self.visited = []
        self.graph = []

    def maxAreaOfIsland(self, grid):
        self.row = len(grid)
        if self.row == 0:
            return 0
        self.column = len(grid[0])
        if self.column == 0:
            return 0
        for v in range(self.row * self.column):
            self.graph.append(set())
        for v in range(self.row * self.column):
            # 求出周围四个方向的坐标
            x = int(v / self.column)
            y = v % self.column
            if grid[x][y] == 1:
                for d in range(4):
                    next_x = x + self.dirs[d][0]
                    next_y = y + self.dirs[d][1]
                    if self._in_area(next_x, next_y) and grid[next_x][next_y] == 1:
                        idx = next_x * self.column + next_y
                        self.graph[idx].add(v)
                        self.graph[v].add(idx)
        print(self.graph)
        for v in range(len(self.graph)):
            self.visited.append(False)
        # 求出图中顶点数最多的连通分量的顶点数
        res = 0
        for v in range(len(self.graph)):
            x = int(v / self.column)
            y = v % self.column
            if not self.visited[v] and grid[x][y] == 1:
                res = max(self._dfs(v), res)
        return res

    def _dfs(self, v):
        self.visited[v] = True
        count = 1
        for w in self.graph[v]:
            if not self.visited[w]:
                count += self._dfs(w)
        return count

    def _in_area(self, x, y):
        return 0 <= x < self.row and 0 <= y < self.column


class Solution2:
    # 不建图直接在给的grid中进行dfs操作
    def __init__(self):
        self.dirs = [[-1, 0], [0, 1], [1, 0], [0, -1]]
        self.visited = []

    def maxAreaOfIsland(self, grid):
        self.grid  =grid
        self.row = len(grid)
        if self.row == 0:
            return 0
        self.column = len(grid[0])
        if self.column == 0:
            return 0
        for i in range(self.row):
            arr = []
            for j in range(self.column):
                arr.append(False)
            self.visited.append(arr)
        res = 0
        for i in range(self.row):
            for j in range(self.column):
                if not self.visited[i][j] and grid[i][j] == 1:
                    res = max(res, self._dfs(i, j))
        return res

    def _dfs(self, x, y):
        self.visited[x][y] = True
        count = 1
        for i in range(4):
            next_x = x + self.dirs[i][0]
            next_y = y + self.dirs[i][1]
            if self._in_area(next_x, next_y) and not self.visited[next_x][next_y] and self.grid[next_x][next_y] == 1:
                count += self._dfs(next_x, next_y)
        return count

    def _in_area(self, x, y):
        return 0 <= x < self.row and 0 <= y < self.column


if __name__ == '__main__':
    """
    1 1
    1 0
    """
    print(Solution2().maxAreaOfIsland([[1, 1], [1, 0]]))
