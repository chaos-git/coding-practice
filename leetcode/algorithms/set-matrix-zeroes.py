'''
Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in-place.

Example 1:

Input:    
[
  [1,1,1],
  [1,0,1],
  [1,1,1]
]
Output:    
[
  [1,0,1],
  [0,0,0],
  [1,0,1]
]
Example 2:

Input:    
[
  [0,1,2,0],
  [3,4,5,2],
  [1,3,1,5]
]
Output:    
[
  [0,0,0,0],
  [0,4,5,0],
  [0,3,1,0]
]
Follow up:

A straight forward solution using O(mn) space is probably a bad idea.
A simple improvement uses O(m + n) space, but still not the best solution.
Could you devise a constant space solution?
'''


class Solution(object):

    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        if not matrix:
            return
    
        rows = len(matrix)
        cols = len(matrix[0])
        rows_zeroes = [1] * rows
        cols_zeroes = [1] * cols

        for row in range(rows):
            for col in range(cols):
                if matrix[row][col] == 0:
                    rows_zeroes[row] = 0
                    cols_zeroes[col] = 0

        for row in range(rows):
            for col in range(cols):
                if rows_zeroes[row] == 0 or cols_zeroes[col] == 0:
                    matrix[row][col] = 0
