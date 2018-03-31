#!/bin/python

import sys

def lonely_integer(arr):
    seen = {}
    for element in arr:
        seen[element] = seen.get(element, 0) + 1
        if seen[element] == 2:
            del seen[element]
    return seen.keys()[0]

n = int(raw_input().strip())
arr = map(int, raw_input().strip().split(' '))
print lonely_integer(arr)