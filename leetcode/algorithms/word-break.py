'''
Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, determine if s can be segmented into a space-separated sequence of one or more dictionary words.

Note:

The same word in the dictionary may be reused multiple times in the segmentation.
You may assume the dictionary does not contain duplicate words.
Example 1:

Input: s = "leetcode", wordDict = ["leet", "code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".
Example 2:

Input: s = "applepenapple", wordDict = ["apple", "pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
             Note that you are allowed to reuse a dictionary word.
Example 3:

Input: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
Output: false
'''


class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        subwords = {}
        for word in wordDict:
            for end in range(1, len(word) + 1):
                subwords[word[0:end]] = subwords.get(word[0:end], False)
            subwords[word] = True

        seen = set()
        stack = [(0, "")]
        while stack:
            item = stack.pop()
            if item in seen:
                continue
            seen.add(item)
            index, prefix = item
            if index < len(s):
                next_prefix = prefix + s[index]
                if next_prefix in subwords:
                    stack.append((index + 1, next_prefix))
                    if subwords[next_prefix]:
                        stack.append((index + 1, ""))
            elif prefix == "":
                return True
        return False
