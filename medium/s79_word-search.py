"""
  * @FileName: s79_word-search.py
  * @Author:   zzc
  * @Date:     2020年12月26日 10:20:08
  * @Version   V1.0.0
"""
from typing import List

"""
给定一个二维网格和一个单词，找出该单词是否存在于网格中。
单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。

示例:
board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]
给定 word = "ABCCED", 返回 true
给定 word = "SEE", 返回 true
给定 word = "ABCB", 返回 false

提示：
board 和 word 中只包含大写和小写英文字母。
1 <= board.length <= 200
1 <= board[i].length <= 200
1 <= word.length <= 10^3
"""


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        self.r = len(board)
        self.c = len(board[0])
        self.visited = [[False for _ in range(self.c)] for _ in range(self.r)]
        self.dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        for i in range(0, self.r):
            for j in range(0, self.c):
                if self.helper(board, word, 0, i, j):
                    return True
        return False

    def helper(self, board, word, idx, x, y):
        if idx == len(word) - 1:
            return board[x][y] == word[idx]

        if board[x][y] == word[idx]:
            self.visited[x][y] = True
            for i in range(4):
                next_x = x + self.dirs[i][0]
                next_y = y + self.dirs[i][1]
                if 0 <= next_x < self.r and 0 <= next_y < self.c and not self.visited[next_x][next_y]:
                    if self.helper(board, word, idx + 1, next_x, next_y):
                        return True
            self.visited[x][y] = False
        return False


if __name__ == '__main__':
    print(Solution().exist([["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "ABCCED"))
