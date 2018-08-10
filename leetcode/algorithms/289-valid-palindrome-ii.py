'''
Given a non-empty string s, you may delete at most one character. Judge whether you can make it a palindrome.

Example 1:
Input: "aba"
Output: True
Example 2:
Input: "abca"
Output: True
Explanation: You could delete the character 'c'.
Note:
The string will only contain lowercase characters a-z. The maximum length of the string is 50000.
'''


class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        deletion_limit = 1
        alt_queue = [(0, len(s) - 1, 0)]  # left index, right index, deletion count
        while alt_queue:
            (left, right, deletes) = alt_queue.pop()
            if left > right:
                return True
            if s[left] == s[right]:
                alt_queue.append((left + 1, right - 1, deletes))
            elif deletes < deletion_limit:
                alt_queue.append((left + 1, right, deletes + 1))
                alt_queue.append((left, right - 1, deletes + 1))
        return False
