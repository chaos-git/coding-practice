#!/bin/python

import heapq
import sys

# Could use insertion sort on an array since it's an online sort, however
# insertion is expensive at O(n^2). Instead, we'll use a min/max heap pair
# since insertion is O(logn) and read is O(1). A little more work to keep
# the heaps balanced, but that's okay.
class MedianTracker:
    def __init__(self):
        self.left_max_heap = [] # track left side of median
        self.right_min_heap = [] # track right side of median

    def add_item(self, item):
        if len(self.left_max_heap) + len(self.right_min_heap) < 2:
            heapq.heappush(self.left_max_heap, item * -1) # default to left, it'll get rebalanced anyway
        elif item >= self.left_max_heap[0] * -1:
            heapq.heappush(self.right_min_heap, item)
        elif item <= self.right_min_heap[0]:
            heapq.heappush(self.left_max_heap, item * -1)
        self.rebalance()
    
    def rebalance(self):
        (left_len, right_len) = (len(self.left_max_heap), len(self.right_min_heap))
        if left_len <= 1 and right_len <= 1 or abs(left_len - right_len) <= 1:
            return
        if left_len - right_len > 1:
            heapq.heappush(self.right_min_heap, heapq.heappop(self.left_max_heap) * -1)
        else:
            heapq.heappush(self.left_max_heap, heapq.heappop(self.right_min_heap) * -1)

    def get_median(self):
        if not len(self.left_max_heap) and not len(self.right_min_heap):
            return None
        if len(self.left_max_heap) > len(self.right_min_heap):
            return self.left_max_heap[0] * -1
        if len(self.left_max_heap) < len(self.right_min_heap):
            return self.right_min_heap[0]
        return ((self.left_max_heap[0] * -1) + self.right_min_heap[0]) / float(2)

median_tracker = MedianTracker()
for index in xrange(int(raw_input().strip())):
    median_tracker.add_item(int(raw_input().strip()))
    print str(float(median_tracker.get_median()))