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
        results = []
        stack = [(0, range(n), [], [], [])]
        while stack:
            row, cols, ldiags, rdiags, grid = stack.pop()
            if row == n:
                results.append(grid)
                continue

            for c_i, col in enumerate(cols):
                ldiag, rdiag = col + row, col + n - row - 1  # compute diagonal ids
                if ldiag not in ldiags and rdiag not in rdiags:  # never used these diagonal ids before?
                    stack.append((
                        row + 1,
                        cols[:c_i] + cols[c_i + 1:],
                        ldiags + [ldiag],
                        rdiags + [rdiag],
                        grid + [('.' * col) + 'Q' + ('.' * (n - col - 1))]
                    ))
        return results
