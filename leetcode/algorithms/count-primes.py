'''
Count the number of prime numbers less than a non-negative number, n.

Example:

Input: 10
Output: 4
Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
'''


class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2:
            return 0

        primes = [0, 0] + ([1] * (n - 2))
        for multiplicand in range(2, int(n ** 0.5) + 1):
            if primes[multiplicand]:
                for product in range(multiplicand * multiplicand, n, multiplicand):
                    primes[product] = 0

        return sum(primes)
