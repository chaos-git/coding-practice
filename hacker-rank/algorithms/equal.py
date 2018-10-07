'''
Christy is interning at HackerRank. One day she has to distribute some chocolates to her colleagues. She is biased towards her friends and plans to give them more than the others. One of the program managers hears of this and tells her to make sure everyone gets the same number.

To make things difficult, she must equalize the number of chocolates in a series of operations. For each operation, she can give  chocolates to all but one colleague. Everyone who gets chocolate in a round receives the same number of pieces.

For example, assume the starting distribution is . She can give  bars to the first two and the distribution will be . On the next round, she gives the same two  bars each, and everyone has the same number: .

Given a starting distribution, calculate the minimum number of operations needed so that every colleague has the same number of chocolates.    

Function Description

Complete the equal function in the editor below. It should return an integer that reperesents the minimum number of operations required.

equal has the following parameter(s):

arr: an array of integers to equalize
Input Format

The first line contains an integer , the number of test cases.

Each test case has  lines.    
- The first line contains an integer , the number of colleagues.    
- The second line contains  space-separated integers denoting the number of chocolates each colleague has.

Constraints

    
    
Number of initial chocolates each colleague has <    

Output Format

Print the minimum number of operations needed for each test case, one to a line.

Sample Input

1
4
2 2 3 7
Sample Output

2
Explanation

Start with    
Add  to all but the 3rd element    
Add  to all but the 4th element    

Two operations were required.

Sample Input 1

1
3
10 7 12
Sample Output 1

3
Explanation 1

Start with    
Add  to the first two elements    
Add  to the last two elements    
Add  to the last two elements    

Three operations were required.
'''


#!/bin/python

import math
import os
import random
import re
import sys

# Complete the equal function below.
DIST_QUANTITIES = [1, 2, 5]

# Complete the equal function below.
def equal(arr):
    # compute deltas
    min_chocs = min(arr)
    deltas = [chocs - min_chocs for chocs in arr]

    # compute number of operations to get to each delta
    ops = [0] * (max(deltas) + max(DIST_QUANTITIES))
    for i in range(len(ops)):
        for dist_qty in DIST_QUANTITIES:
            if i + dist_qty < len(ops):
                ops[i + dist_qty] = min(ops[i] + 1, ops[i + dist_qty] or ops[i] + 1)

    # add operations
    results = [0] * max(DIST_QUANTITIES)
    for offset in range(len(results)):
        for delta in deltas:
            results[offset] += ops[delta + offset]

    return min(results)
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(raw_input())

    for t_itr in xrange(t):
        n = int(raw_input())

        arr = map(int, raw_input().rstrip().split())

        result = equal(arr)

        fptr.write(str(result) + '\n')

    fptr.close()
