'''
Given an input string , reverse the string word by word.

Example:

Input:  ["t","h","e"," ","s","k","y"," ","i","s"," ","b","l","u","e"]
Output: ["b","l","u","e"," ","i","s"," ","s","k","y"," ","t","h","e"]
Note:

A word is defined as a sequence of non-space characters.
The input string does not contain leading or trailing spaces.
The words are always separated by a single space.
Follow up: Could you do it in-place without allocating extra space?
'''


class Solution(object):
    def reverseWords(self, string):
        """
        :type str: List[str]
        :rtype: void Do not return anything, modify str in-place instead.
        """
        start = 0
        for index in range(len(string) + 1):
            if index == len(string) or string[index] == ' ':
                self.__reverse(string, start, index - 1)
                start = index + 1
        self.__reverse(string, 0, len(string) - 1)

    def __reverse(self, string, start, end):
        while start < end:
            string[start], string[end] = string[end], string[start]
            start, end = start + 1, end - 1
