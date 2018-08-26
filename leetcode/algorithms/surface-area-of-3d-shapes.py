'''
On a N * N grid, we place some 1 * 1 * 1 cubes.

Each value v = grid[i][j] represents a tower of v cubes placed on top of grid cell (i, j).

Return the total surface area of the resulting shapes.



Example 1:

Input: [[2]]
Output: 10
Example 2:

Input: [[1,2],[3,4]]
Output: 34
Example 3:

Input: [[1,0],[0,2]]
Output: 16
Example 4:

Input: [[1,1,1],[1,0,1],[1,1,1]]
Output: 32
Example 5:

Input: [[2,2,2],[2,1,2],[2,2,2]]
Output: 46


Note:

1 <= N <= 50
0 <= grid[i][j] <= 50
'''


class Solution(object):
    def surfaceArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        row_count = len(grid)
        col_count = len(grid[0])
        surface = 0
        for row in range(row_count):
            for col in range(col_count):
                # if the cell is left-most or front-most
                if row == 0:
                    surface += grid[row][col]
                if col == 0:
                    surface += grid[row][col]

                # if the cell is right-most or back-most
                if row == row_count - 1:
                    surface += grid[row][col]
                if col == col_count - 1:
                    surface += grid[row][col]

                # the delta between the cell to the right and the cell to the front
                if row != row_count - 1:
                    surface += abs(grid[row][col] - grid[row + 1][col])
                if col != col_count - 1:
                    surface += abs(grid[row][col] - grid[row][col + 1])

                # top and bottom
                if grid[row][col] > 0:
                    surface += 2

        return surface
