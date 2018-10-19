'''
Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms required.

Example 1:

Input: [[0, 30],[5, 10],[15, 20]]
Output: 2
Example 2:

Input: [[7,10],[2,4]]
Output: 1
'''

# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        if not intervals:
            return 0

        milestones = []
        for interval in intervals:
            milestones.append((interval.start,  1))
            milestones.append((interval.end  , -1))

        count = 0
        max_count = 0
        for time, delta in sorted(milestones):
            count += delta
            max_count = max(count, max_count)

        return max_count
