'''
Given a sorted integer array nums, where the range of elements are in the inclusive range [lower, upper], return its missing ranges.

Example:

Input: nums = [0, 1, 3, 50, 75], lower = 0 and upper = 99,
Output: ["2", "4->49", "51->74", "76->99"]
'''


class Solution(object):
    def findMissingRanges(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: List[str]
        """
        nums = [lower - 1] + nums + [upper + 1]
        ranges = []
        for index in range(1, len(nums)):
            if nums[index] - nums[index - 1] == 2:
                ranges.append(str(nums[index] - 1))
            elif nums[index] - nums[index - 1] > 2:
                ranges.append(str(nums[index - 1] + 1) + "->" + str(nums[index] - 1))
        return ranges
