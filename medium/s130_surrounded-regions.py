"""
  * @FileName: s130_surrounded-regions.py
  * @Author:   zzc
  * @Date:     2020年12月26日 11:08:39
  * @Version   V1.0.0
"""
from typing import List

"""
给定一个二维的矩阵，包含 'X' 和 'O'（字母 O）。
找到所有被 'X' 围绕的区域，并将这些区域里所有的 'O' 用 'X' 填充。

示例:
X X X X
X O O X
X X O X
X O X X

运行你的函数后，矩阵变为：

X X X X
X X X X
X X X X
X O X X

解释:
被围绕的区间不会存在于边界上，换句话说，任何边界上的 'O' 都不会被填充为 'X'。 任何不在边界上，或不与边界上的 'O' 相连的 'O' 最终都会被填充为 'X'。
如果两个元素在水平或垂直方向相邻，则称它们是“相连”的。
"""


class Solution:
    def __init__(self):
        self.dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]]

    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board:
            return
        self.r = len(board)
        self.c = len(board[0])
        for i in range(self.r):
            self.dfs(board, i, 0)
            self.dfs(board, i, self.c - 1)
        for i in range(self.c):
            self.dfs(board, 0, i)
            self.dfs(board, self.r - 1, i)
        dic = {'X': 'X', 'O': 'X', '-': 'O'}
        for i in range(self.r):
            for j in range(self.c):
                board[i][j] = dic[board[i][j]]
        print(board)

    def dfs(self, board, x, y):
        if 0 <= x < self.r and 0 <= y < self.c and board[x][y] == 'O':
            board[x][y] = '-'
            for i in range(4):
                next_x = x + self.dirs[i][0]
                next_y = y + self.dirs[i][1]
                self.dfs(board, next_x, next_y)


if __name__ == '__main__':
    Solution().solve([['X', 'X', 'X', 'X'],
                      ['X', 'O', 'O', 'X'],
                      ['X', 'X', 'O', 'X'],
                      ['X', 'O', 'X', 'X']])
