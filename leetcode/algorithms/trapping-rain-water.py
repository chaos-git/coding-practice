'''
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.


The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped. Thanks Marcos for contributing this image!

Example:

Input: [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
'''


class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # imagine looking at the map from the left and the right. which spaces were hidden?
        hidden_left, max_left = self.compute_hidden(height, 0, 1)
        hidden_right, max_right = self.compute_hidden(height, len(height) - 1, -1)

        # spaces that can hold water are double counted as hidden. use this to compute answer.
        total_area = len(height) * max(max_left, max_right)
        return hidden_left + hidden_right + sum(height) - total_area

    def compute_hidden(self, heights, index, step):
        shadow = 0
        max_height = 0
        while index >= 0 and index < len(heights):
            if heights[index] > max_height:
                max_height = heights[index]
            else:
                shadow += max_height - heights[index]
                index += step
        return (shadow, max_height)
