'''
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:

Input:
11110
11010
11000
00000

Output: 1
Example 2:

Input:
11000
11000
00100
00011

Output: 3
'''


class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid or not len(grid) or not len(grid[0]):
            return 0

        height = len(grid)
        width = len(grid[0])

        def fill(x, y):
            stack = [(x, y)]
            while stack:
                cur_x, cur_y = stack.pop()
                grid[cur_y][cur_x] = "0"
                for n_x, n_y in nearby_land(cur_x, cur_y):
                    stack.append((n_x, n_y))

        def nearby_land(x, y):
            return [
                (x1, y1) for x1, y1 in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]
                if x1 >= 0 and x1 < width and y1 >= 0 and y1 < height and grid[y1][x1] == "1"
            ]

        islands = 0
        for y, row in enumerate(grid):
            for x, cell in enumerate(row):
                if cell == "1":
                    islands += 1
                    fill(x, y)
        return islands
