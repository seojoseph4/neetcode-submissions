"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key = lambda i:i.start)
        mh = []
        res = 0

        for interval in intervals:
            while mh and mh[0] <= interval.start:
                heapq.heappop(mh)
            heapq.heappush(mh, interval.end)
            res = max(len(mh), res)
            

        return res
        