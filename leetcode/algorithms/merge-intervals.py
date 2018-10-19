'''
 Merge Intervals
  Go to Discuss
Given a collection of intervals, merge all overlapping intervals.

Example 1:

Input: [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
Example 2:

Input: [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considerred overlapping.
'''


# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def merge(self, intervals_in):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if not intervals_in:
            return []

        result = []
        intervals = sorted(intervals_in, key=lambda i: i.start, reverse=True)
        last = None
        while intervals:
            interval = intervals.pop()
            if not last:
                last = interval
                continue
            if interval.start <= last.end:  # merge them
                last.end = max(last.end, interval.end)
            else:
                result.append(last)
                last = interval
        return result + [last]
