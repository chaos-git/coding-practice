'''
Convert a non-negative integer to its english words representation. Given input is guaranteed to be less than 231 - 1.

Example 1:

Input: 123
Output: "One Hundred Twenty Three"
Example 2:

Input: 12345
Output: "Twelve Thousand Three Hundred Forty Five"
Example 3:

Input: 1234567
Output: "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"
Example 4:

Input: 1234567891
Output: "One Billion Two Hundred Thirty Four Million Five Hundred Sixty Seven Thousand Eight Hundred Ninety One"
'''


class Solution(object):
    def __init__(self):
        singles = ['One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']
        teens = ['Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen']
        tens = ['Ten', 'Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety']
        self.words = {index + 1: word for index, word in enumerate(singles)}
        self.words.update({index + 11: word for index, word in enumerate(teens)})
        self.words.update({(index + 1) * 10: word for index, word in enumerate(tens)})
        self.signifier = [None, 'Thousand', 'Million', 'Billion']

    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        if not num:
            return 'Zero'

        digit_groups = self.__to_digit_groups(num)
        result = []
        for groupid, group in enumerate(digit_groups):
            if self.signifier[groupid] and sum(group) > 0:
                result.append(self.signifier[groupid])
            for digitid, digit in enumerate(group):
                if digit == 0:
                    continue
                if digitid == 0:
                    result.append(self.words[digit])
                elif digitid == 2:
                    result.append('Hundred')
                    result.append(self.words[digit])
                elif digitid == 1 and digit == 1 and group[digitid - 1] != 0:
                    result.pop()
                    result.append(self.words[group[digitid - 1] + 10])
                else:
                    result.append(self.words[digit * 10])
        return " ".join(result[::-1])

    def __to_digit_groups(self, number):
        groups, digits = [], []
        while number != 0:
            digits.append(number % 10)
            number /= 10
        group = []
        for digit in digits:
            group.append(digit)
            if len(group) == 3:
                groups.append(group)
                group = []
        if group:
            groups.append(group)
        return groups
