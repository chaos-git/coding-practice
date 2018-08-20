'''
Given an input string (s) and a pattern (p), implement regular expression matching with support for '.' and '*'.

'.' Matches any single character.
'*' Matches zero or more of the preceding element.
The matching should cover the entire input string (not partial).

Note:

s could be empty and contains only lowercase letters a-z.
p could be empty and contains only lowercase letters a-z, and characters like . or *.
Example 1:

Input:
s = "aa"
p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".
Example 2:

Input:
s = "aa"
p = "a*"
Output: true
Explanation: '*' means zero or more of the precedeng element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".
Example 3:

Input:
s = "ab"
p = ".*"
Output: true
Explanation: ".*" means "zero or more (*) of any character (.)".
Example 4:

Input:
s = "aab"
p = "c*a*b"
Output: true
Explanation: c can be repeated 0 times, a can be repeated 1 time. Therefore it matches "aab".
Example 5:

Input:
s = "mississippi"
p = "mis*is*p*."
Output: false
'''


class Solution(object):
    def compress(self, pattern):
        index = 0
        while index < len(pattern) - 1:
            current, current_wild = pattern[index], pattern[index + 1] == '*'
            nxt, nxt_wild = pattern[index + 2:index + 3], pattern[index + 3:index + 4] == '*'
            if current_wild and nxt_wild and (current == '.' or current == nxt):
                pattern = pattern[:index+2] + pattern[index + 4:]
            else:
                index += 1
        return pattern


    def isMatch(self, string, pattern):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        pattern = self.compress(pattern)
        stack = [(0, 0)]
        while stack:
            sindex, pindex = stack.pop()

            # short circuits
            if sindex == len(string) and pindex == len(pattern):
                return True
            if sindex > len(string) or pindex > len(pattern):
                continue

            # advances
            s, p = string[sindex:sindex+1], pattern[pindex:pindex+1]
            if pattern[pindex + 1:pindex + 2] == '*':
                if s == p or p == '.':
                    stack.append((sindex + 1, pindex))
                    stack.append((sindex + 1, pindex + 2))
                stack.append((sindex, pindex + 2))
            elif s == p or p == '.':
                stack.append((sindex + 1, pindex + 1))
        return False
