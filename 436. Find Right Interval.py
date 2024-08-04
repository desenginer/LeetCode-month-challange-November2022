#https://leetcode.com/problems/find-right-interval
'''
You are given an array of intervals, where intervals[i] = [starti, endi] and each starti is unique.

The right interval for an interval i is an interval j such that startj >= endi and startj is minimized. Note that i may equal j.

Return an array of right interval indices for each interval i. If no right interval exists for interval i, then put -1 at index i.
'''


class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        start_points = {}
        for i, interval in enumerate(intervals):
            start_points[interval[0]] = i

        sorted_intervals = sorted(intervals, key=lambda x: x[0])
        result = [-1] * len(intervals)
        for i, interval in enumerate(intervals):
            index = bisect_left(sorted_intervals, [interval[1], -float('inf')])
            if index != len(intervals):
                result[i] = start_points[sorted_intervals[index][0]]

        return result