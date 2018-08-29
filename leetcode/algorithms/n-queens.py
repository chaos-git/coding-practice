'''
The n-queens puzzle is the problem of placing n queens on an n×n chessboard such that no two queens attack each other.



Given an integer n, return all distinct solutions to the n-queens puzzle.

Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space respectively.

Example:

Input: 4
Output: [
 [".Q..",  // Solution 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // Solution 2
  "Q...",
  "...Q",
  ".Q.."]
]
Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above.
'''


class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        seen = set()
        results = []
        stack = [(0, [], range(n))]
        while stack:
            row, board, col_rack = stack.pop()

            key = "".join(board)
            if key in seen:
                continue
            seen.add(key)

            if not self.__is_valid(board):
                continue

            if row == n:
                results.append(board)
                continue

            for index, col in enumerate(col_rack):
                new_row = ('.' * col) + 'Q' + ('.' * (n - col - 1))
                stack.append((row + 1, board + [new_row], col_rack[:index] + col_rack[index + 1:]))

        return results

    def __is_valid(self, board):
        seen_row, seen_col, seen_diag_left, seen_diag_right = set(), set(), set(), set()
        for row in range(len(board)):
            for col in range(len(board[row])):
                if board[row][col] == 'Q':
                    if row in seen_row or col in seen_col:
                        return False
                    if (col + row) in seen_diag_left or (len(board[row]) - 1 - col + row) in seen_diag_right:
                        return False
                    seen_row.add(row)
                    seen_col.add(col)
                    seen_diag_left.add(col + row)
                    seen_diag_right.add(len(board[row]) - 1 - col + row)
        return True
