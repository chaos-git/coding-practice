'''
Given an input string, reverse the string word by word.

Example:

Input: "the sky is blue",
Output: "blue is sky the".
Note:

A word is defined as a sequence of non-space characters.
Input string may contain leading or trailing spaces. However, your reversed string should not contain leading or trailing spaces.
You need to reduce multiple spaces between two words to a single space in the reversed string.
Follow up: For C programmers, try to solve it in-place in O(1) space.
'''


class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        words = []
        start = 0
        while start < len(s):
            if s[start] == ' ':
                start += 1
                continue
            end = self.__find_end(s, start)
            words.append(s[start:end+1][::-1])
            start = end + 1
        return " ".join(words)[::-1]

    def __find_end(self, s, start):
        last = start
        while last < len(s) - 1 and s[last + 1] != ' ':
            last += 1
        return last
