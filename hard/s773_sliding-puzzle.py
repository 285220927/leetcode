"""
  * @FileName: s773_sliding-puzzle.py
  * @Author:   zzc
  * @Date:     2020年10月29日 21:44:22
  * @Version   V1.0.0
"""
from queue import Queue

"""
在一个 2 x 3 的板上（board）有 5 块砖瓦，用数字 1~5 来表示, 以及一块空缺用0来表示.
一次移动定义为选择0与一个相邻的数字（上下左右）进行交换.
最终当板board的结果是[[1,2,3],[4,5,0]]谜板被解开。
给出一个谜板的初始状态，返回最少可以通过多少次移动解开谜板，如果不能解开谜板，则返回 -1 。

示例：
输入：board = [[1,2,3],[4,0,5]]
输出：1
解释：交换 0 和 5 ，1 步完成
输入：board = [[1,2,3],[5,4,0]]
输出：-1
解释：没有办法完成谜板
输入：board = [[4,1,2],[5,0,3]]
输出：5
解释：
最少完成谜板的最少移动次数是 5 ，
一种移动路径:
尚未移动: [[4,1,2],[5,0,3]]
移动 1 次: [[4,1,2],[0,5,3]]
移动 2 次: [[0,1,2],[4,5,3]]
移动 3 次: [[1,0,2],[4,5,3]]
移动 4 次: [[1,2,0],[4,5,3]]
移动 5 次: [[1,2,3],[4,5,0]]
输入：board = [[3,2,4],[1,5,0]]
输出：14

提示：
board是一个如上所述的 2 x 3 的数组.
board[i][j]是一个[0, 1, 2, 3, 4, 5]的排列.
"""

"""
4 1 2
5 0 3

4 1 2
0 5 3

0 1 2
4 5 3

1 0 2
4 5 3

1 2 0
4 5 3

1 2 3
4 5 0
"""


class Solution:
    def __init__(self):
        # 改进成r * c
        # O(n!)时间复杂度
        self.r = 2  # row
        self.c = 3  # column
        self.directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]

    def slidingPuzzle(self, board):
        init_num = self._list2int(board)
        if init_num == 123450:
            return 0
        visited = {init_num: 0}
        queue = Queue()
        queue.put(init_num)
        while not queue.empty():
            v = queue.get()
            v_next_keys = self._get_next_keys(v)
            for next_key in v_next_keys:
                if visited.get(next_key) is None:
                    queue.put(next_key)
                    visited[next_key] = visited[v] + 1
                    if next_key == 123450:
                        return visited[next_key]
        return -1

    def _list2int(self, board):
        num = 0
        figures = self.r * self.c
        for i in range(self.r):
            for j in range(self.c):
                num += board[i][j] * pow(10, figures - 1)
                figures -= 1
        return num

    def _int2list(self, v):
        v_arr = []
        figures = self.r * self.c
        for i in range(self.r):
            column_arr = []
            for j in range(self.c):
                num = int(v / pow(10, figures - 1))
                figures -= 1
                if i == j == 0:
                    column_arr.append(num)
                else:
                    column_arr.append(num % 10)
            v_arr.append(column_arr)
        return v_arr

    def _get_next_keys(self, v):
        next_ints = []
        v_arr = self._int2list(v)
        i = 0
        one_arr = [i for item in v_arr for i in item]  # 转为一维数组
        while True:
            if one_arr[i] == 0:
                break
            i += 1
        r = int(i / self.c)
        c = i % self.c
        for i in range(4):
            # 四连通
            next_r = r + self.directions[i][0]
            next_c = c + self.directions[i][1]
            if self._in_area(next_r, next_c):
                self._swap(v_arr, r, c, next_r, next_c)
                next_ints.append(self._list2int(v_arr))
                self._swap(v_arr, r, c, next_r, next_c)  # 还要再换回来
        return next_ints

    def _in_area(self, r, c):
        return 0 <= r < self.r and 0 <= c < self.c

    def _swap(self, board, r1, c1, r2, c2):
        temp = board[r1][c1]
        board[r1][c1] = board[r2][c2]
        board[r2][c2] = temp


if __name__ == '__main__':
    print(Solution().slidingPuzzle([[4, 1, 2], [5, 0, 3]]))
