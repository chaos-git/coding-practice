'''
Given an input string (s) and a pattern (p), implement wildcard pattern matching with support for '?' and '*'.

'?' Matches any single character.
'*' Matches any sequence of characters (including the empty sequence).
The matching should cover the entire input string (not partial).

Note:

s could be empty and contains only lowercase letters a-z.
p could be empty and contains only lowercase letters a-z, and characters like ? or *.

Example 1:
Input:
s = "aa"
p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".

Example 2:
Input:
s = "aa"
p = "*"
Output: true
Explanation: '*' matches any sequence.

Example 3:
Input:
s = "cb"
p = "?a"
Output: false
Explanation: '?' matches 'c', but the second letter is 'a', which does not match 'b'.

Example 4:
Input:
s = "adceb"
p = "*a*b"
Output: true
Explanation: The first '*' matches the empty sequence, while the second '*' matches the substring "dce".

Example 5:
Input:
s = "acdcb"
p = "a*c?b"
Output: false
'''

class Solution:
    def isMatch(self, string, pattern):
        visited = {}
        queue = [(0,0)]
        while len(queue):
            (sindex, pindex) = queue.pop()
            if (sindex, pindex) in visited: 
                continue # skip: we've seen this before, or if we're at the end of the pattern
            visited[(sindex, pindex)] = True
            if sindex == len(string) and pindex == len(pattern):
                return True # if we consumed both strings at the same time, success!
            if pindex == len(pattern):
                continue # if we finished pattern, then must give up on this one
            if sindex < len(string) and (pattern[pindex] is '?' or pattern[pindex] == string[sindex]):
                queue.append((sindex + 1, pindex + 1)) # next sindex/pindex when single character matches
            if pattern[pindex] is '*':
                queue.append((sindex, pindex + 1)) # for any wildcard, must try next pattern
                if sindex != len(string): # but if wildcard isn't when string ended, then extra possibilities!
                    queue.append((sindex + 1, pindex + 1))
                    queue.append((sindex + 1, pindex))
        return False
