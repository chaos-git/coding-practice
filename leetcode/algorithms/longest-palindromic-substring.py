'''
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: "cbbd"
Output: "bb"
'''


class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) <= 1:
            return s

        maxp = ""
        for index in range(len(s) - 1):
            oddp = self.get_palindrome_length(s, index, index)
            if len(oddp) > len(maxp):
                maxp = oddp

            evenp = self.get_palindrome_length(s, index, index + 1)
            if len(evenp) > len(maxp):
                maxp = evenp

        return maxp

    def get_palindrome_length(self, s, left, right):
        if s[left] != s[right]:
            return ""

        while left - 1 >= 0 and right + 1 < len(s) and s[left - 1] == s[right + 1]:
            left -= 1
            right += 1

        return s[left:right+1]
