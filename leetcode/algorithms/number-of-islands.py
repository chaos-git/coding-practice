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
                for n_x, n_y in get_neighbors(cur_x, cur_y):
                    if is_inside(n_x, n_y) and grid[n_y][n_x] == "1":
                        stack.append((n_x, n_y))

        def get_neighbors(x, y):
            offsets = [(-1, 0), (1, 0),(0, -1), (0, 1)]
            return [(x + off_x, y + off_y) for off_x, off_y in offsets]

        def is_inside(x, y):
            return x >= 0 and \
                    x < width and \
                    y >= 0 and \
                    y < height

        islands = 0
        for y, row in enumerate(grid):
            for x, cell in enumerate(row):
                if cell == "1":
                    islands += 1
                    fill(x, y)
        return islands
