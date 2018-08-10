'''
Given two binary strings, return their sum (also a binary string).

The input strings are both non-empty and contains only characters 1 or 0.

Example 1:

Input: a = "11", b = "1"
Output: "100"
Example 2:

Input: a = "1010", b = "1011"
Output: "10101"
'''


class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        num_a = self.binary_string_to_number(a)
        num_b = self.binary_string_to_number(b)

        return self.number_to_binary_string(num_a + num_b)

    def binary_string_to_number(self, binary_string):
        number = 0
        for bit in binary_string:
            number <<= 1
            number |= (bit == '1')
        return number

    def number_to_binary_string(self, number):
        string = ''
        while True:
            string = ('1' if number & 1 else '0') + string
            number >>= 1
            if not number:
                return string
