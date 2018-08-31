'''

Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output: 321
Example 2:

Input: -123
Output: -321
Example 3:

Input: 120
Output: 21
Note:
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.
'''


class Solution(object):
    pos32 = 2**31 - 1

    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        result = 0
        tmp, neg = abs(x), 1 if x > 0 else -1
        while tmp != 0:
            result = (result * 10) + (tmp % 10)
            tmp /= 10
        return result * neg * (result < self.pos32)
