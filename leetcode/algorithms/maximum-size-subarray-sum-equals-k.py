'''
Given an array nums and a target value k, find the maximum length of a subarray that sums to k. If there isn't one, return 0 instead.

Note:
The sum of the entire nums array is guaranteed to fit within the 32-bit signed integer range.

Example 1:

Input: nums = [1, -1, 5, -2, 3], k = 3
Output: 4 
Explanation: The subarray [1, -1, 5, -2] sums to 3 and is the longest.
Example 2:

Input: nums = [-2, -1, 2, 1], k = 1
Output: 2 
Explanation: The subarray [-1, 2] sums to 1 and is the longest.
Follow Up:
Can you do it in O(n) time?
'''


class Solution(object):
    def maxSubArrayLen(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        seen = {}
        max_length = 0
        running_sum = 0

        for index in range(len(nums)):
            running_sum += nums[index]
            if running_sum not in seen:
                seen[running_sum] = index
            if running_sum == k:
                max_length = index + 1
            if (running_sum - k) in seen:
                max_length = max(index - seen[running_sum - k], max_length)

        return max_length
