'''
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
Note:

All given inputs are in lowercase letters a-z.
'''


class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""

        prefix = ""
        while True:
            index = len(prefix)
            current_char = None
            for string in strs:
                if index > len(string) - 1:
                    return prefix
                if current_char is None:
                    current_char = string[index]
                elif string[index] != current_char:
                    return prefix
            prefix += current_char
        return prefix
