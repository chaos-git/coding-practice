'''
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
'''


class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        results = []
        stack = [(0, 0, "")]
        while stack:
            opens, closes, string = stack.pop()
            if opens == n and closes == n:
                results.append(string)
                continue

            if opens > closes:
                stack.append((opens, closes + 1, string + ")"))
            if opens < n:
                stack.append((opens + 1, closes, string + "("))
        return results
