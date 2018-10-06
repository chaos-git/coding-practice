'''
Given a list of non negative integers, arrange them such that they form the largest number.

Example 1:

Input: [10,2]
Output: "210"
Example 2:

Input: [3,30,34,5,9]
Output: "9534330"
'''


class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        def cust_sort(x, y):
            return 1 if x + y < y + x else -1
        result = ''.join(sorted(map(str, nums), cmp=cust_sort))
        return result if result and result[0] != '0' else '0'
