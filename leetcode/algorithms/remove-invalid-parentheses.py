'''
Remove the minimum number of invalid parentheses in order to make the input string valid. Return all possible results.

Note: The input string may contain letters other than the parentheses ( and ).

Example 1:

Input: "()())()"
Output: ["()()()", "(())()"]
Example 2:

Input: "(a)())()"
Output: ["(a)()()", "(a())()"]
Example 3:

Input: ")("
Output: [""]
'''


class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        iterations = set()
        max_skips = None
        results = set()
        stack = [(0, 0, 0, 0, "")]
        while stack:
            # have we see this set of arguments before?
            iteration = stack.pop()
            if iteration in iterations:
                continue
            iterations.add(iteration)

            # have we already found a solution with less skips?
            index, opens, closes, skips, prefix = iteration
            if max_skips is not None and skips > max_skips:
                continue

            # have we finished?
            if index == len(s):
                if opens == closes:
                    max_skips = max_skips or skips
                    results.add(prefix)
                continue

            # stack up the next iterations
            if s[index] == '(':
                stack.append((index + 1, opens, closes, skips + 1, prefix))  # skip
                stack.append((index + 1, opens + 1, closes, skips, prefix + '('))  # keep
            elif s[index] == ')':
                stack.append((index + 1, opens, closes, skips + 1, prefix))  # skip
                if opens > closes: # keep only if including is valid
                    stack.append((index + 1, opens, closes + 1, skips, prefix + ')'))  # keep
            else:
                stack.append((index + 1, opens, closes, skips, prefix + s[index]))  # can't skip

        return list(results)
