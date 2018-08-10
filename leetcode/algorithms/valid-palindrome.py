'''
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Note: For the purpose of this problem, we define empty string as valid palindrome.

Example 1:

Input: "A man, a plan, a canal: Panama"
Output: true
Example 2:

Input: "race a car"
Output: false
'''


class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        candidate = (s or "").lower()
        left = 0
        right = len(candidate) - 1

        while left <= right:
            if not candidate[left].isalnum():
                left += 1
            elif not candidate[right].isalnum():
                right -= 1
            elif candidate[left] != candidate[right]:
                return False
            else:
                left += 1
                right -= 1

        return True
