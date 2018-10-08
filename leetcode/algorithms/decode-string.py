'''
Given an encoded string, return it's decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; No extra white spaces, square brackets are well-formed, etc.

Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there won't be input like 3a or 2[4].

Examples:

s = "3[a]2[bc]", return "aaabcbc".
s = "3[a2[c]]", return "accaccacc".
s = "2[abc]3[cd]ef", return "abcabccdcdcdef".
'''


class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        qty_stack = []
        val_stack = []
        val_buffer = ''

        index = 0
        while index < len(s):
            if s[index].isdigit():
                start = index
                while s[index].isdigit():
                    index += 1
                qty_stack.append(int(s[start:index]))
                val_stack.append(val_buffer)
                val_buffer = ''

            if s[index] == ']':
                val_buffer = val_stack.pop() + (val_buffer * qty_stack.pop())
            elif s[index] != '[':
                val_buffer += s[index]

            index += 1
        return val_buffer
