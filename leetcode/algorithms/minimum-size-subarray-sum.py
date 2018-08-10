'''
Given an array of n positive integers and a positive integer s, find the minimal length of a contiguous subarray of which the sum ≥ s. If there isn't one, return 0 instead.

Example: 

Input: s = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: the subarray [4,3] has the minimal length under the problem constraint.
Follow up:
If you have figured out the O(n) solution, try coding another solution of which the time complexity is O(n log n). 
'''


class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        left = 0
        right = 0
        subsum = nums[left]

        min_length = 0
        while left < len(nums):
            # update min_length
            if subsum >= s:
                length = right - left + 1
                min_length = min(length, min_length or length)

            # move left pointer
            if subsum >= s:  # if subsum is too big, shrink from the left
                subsum -= nums[left]
                left += 1
                if left <= right:  # when moving left pointer, only move right if left passes right
                    continue

            # move right pointer
            if right >= len(nums) - 1:
                break
            right += 1
            subsum += nums[right]

        return min_length
