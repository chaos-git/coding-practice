#!/bin/python

import sys
import math

def kangaroo(x1, v1, x2, v2):
    if v1 - v2 == 0:
        return "YES" if x1 == x2 else "NO"
    jumps = (x2 - x1) / (v1 - v2)
    return "YES" if jumps > 0 and jumps % 1 == 0 else "NO"
    
x1, v1, x2, v2 = map(float, raw_input().strip().split(' '))
print kangaroo(x1, v1, x2, v2)