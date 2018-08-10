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
        results = set()
        for left in range(len(nums) - 2):
            middle = left + 1
            right = len(nums) - 1

            if left > 0 and nums[left - 1] == nums[middle]:
                continue

            while middle < right:
                candidate = (nums[left], nums[middle], nums[right])
                candidate_sum = sum(candidate)

                if candidate_sum == 0:
                    results.add(candidate)
                if candidate_sum > 0:
                    right -= 1
                else:
                    middle += 1

        return list(results)
