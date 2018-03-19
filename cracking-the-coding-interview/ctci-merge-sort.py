#!/bin/python

# !IMPORTANT: must run as 'PyPy' otherwise a timeout will occur on 3 tests

import math
import sys

''' Uses stack instead of recursion because was hitting StackOverflow issues
'''
def find_merges(arr):
    merges = []
    splits = [(0, len(arr) - 1)]
    while len(splits):
        left, right = splits.pop()
        if right - left == 0:
            continue
        mid = (left + right) / 2
        splits.append((left, mid))
        splits.append((mid + 1, right))
        merges.append((left, mid, right))
    return merges

def process_merges(arr, merges):
    aux = [0] * len(arr)
    count = 0
    while len(merges):
        left, mid, right = merges.pop()
        aux[left:right+1] = arr[left:right+1] # O(nlogn)
        a = left
        l = left
        r = mid + 1
        while l <= mid or r <= right:
            if l > mid:
                arr[a] = aux[r]
                r += 1
            elif r > right:
                arr[a] = aux[l]
                l += 1
            elif aux[l] <= aux[r]:
                arr[a] = aux[l]
                l += 1
            else:
                arr[a] = aux[r]
                r += 1
                count += mid + 1 - l
            a += 1
    return count

if __name__ == "__main__":
    t = int(raw_input().strip())
    for a0 in xrange(t):
        n = int(raw_input().strip())
        arr = map(int, raw_input().strip().split(' '))
        print process_merges(arr, find_merges(arr))