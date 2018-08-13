'''
Given a collection of distinct integers, return all possible permutations.

Example:

Input: [1,2,3]
Output:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
'''


class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        perms = []
        stack = [([], nums)]
        while stack:
            locked, rack = stack.pop()
            if not rack:
                perms.append(locked)
                continue
            for index in range(len(rack)):
                stack.append((locked + [rack[index]], rack[:index] + rack[index + 1:]))
        return perms
