'''
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

Example 1:

Input: "()"
Output: true
Example 2:

Input: "()[]{}"
Output: true
Example 3:

Input: "(]"
Output: false
Example 4:

Input: "([)]"
Output: false
Example 5:

Input: "{[]}"
Output: true
'''


class Solution(object):
    open_to_close = {'{': '}', '[': ']', '(': ')'}

    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        for char in s:
            if char in self.open_to_close.keys():
                stack.append(char)
            elif not stack:
                return False
            else:
                last_open = stack.pop()
                if char != self.open_to_close[last_open]:
                    return False

        return len(stack) == 0
