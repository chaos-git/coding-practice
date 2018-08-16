'''
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note:

The solution set must not contain duplicate triplets.

Example:

Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
'''


class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()

        # grab indexes of numbers
        seen = {}
        for index, number in enumerate(nums):
            seen[number] = seen.get(number, []) + [index]
                            
        results = set()
        for left in range(len(nums) - 2):
            for middle in range(left + 1, len(nums) - 1):
                if left > 0 and nums[left] == nums[left - 1]:
                    continue
                remainder = 0 - nums[left] - nums[middle]
                if remainder in seen and max(seen[remainder]) > middle:
                    results.add((nums[left], nums[middle], remainder))
        return list(results)