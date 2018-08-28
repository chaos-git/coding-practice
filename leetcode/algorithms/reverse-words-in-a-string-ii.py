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
        index = 0
        while index < len(string):
            next_start, next_end = self.__get_next_word_boundary(string, index)
            self.__reverse(string, next_start, next_end)
            index = next_end + 1
        self.__reverse(string, 0, len(string) - 1)

    def __get_next_word_boundary(self, string, start_index):
        start, end = start_index, start_index
        while end < len(string) - 1 and string[end + 1] != ' ':
            if string[start] == ' ':
                start += 1
            end += 1
        return (start, end)

    def __reverse(self, string, start, end):
        while start < end:
            string[start], string[end] = string[end], string[start]
            start, end = start + 1, end - 1
