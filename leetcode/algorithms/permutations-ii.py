'''
Given a collection of numbers that might contain duplicates, return all possible unique permutations.

Example:

Input: [1,1,2]
Output:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]
'''


class Solution:
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        permutes = []
        stack = [([], nums)]
        while stack:
            locked, rack = stack.pop()
            if not rack:
                permutes.append(locked)
                continue
            for index in range(len(rack)):
                if index > 0 and rack[index] == rack[index - 1]:
                    continue
                stack.append((locked + [rack[index]], rack[:index] + rack[index + 1:]))
        return permutes
