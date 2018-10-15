'''
Given a string S, check if the letters can be rearranged so that two characters that are adjacent to each other are not the same.

If possible, output any possible result.  If not possible, return the empty string.

Example 1:

Input: S = "aab"
Output: "aba"
Example 2:

Input: S = "aaab"
Output: ""
Note:

S will consist of lowercase letters and have length in range [1, 500].
'''


class Solution(object):
    def reorganizeString(self, S):
        """
        :type S: str
        :rtype: str
        """
        counts = {}
        for char in S:
            counts[char] = counts.get(char, 0) + 1
        chars = sorted(counts.keys(), key=lambda char: counts[char], reverse=True)

        if counts[chars[0]] > (len(S) + 1) // 2:
            return ""

        char_index = 0
        result_index = 0
        result = [''] * len(S)
        while char_index < len(chars):
            char = chars[char_index]
            counts[char] -= 1
            if counts[char] < 0:
                char_index += 1
                continue
            result[result_index] = char
            result_index += 2
            if result_index >= len(S):
                result_index = 1
        return "".join(result)

