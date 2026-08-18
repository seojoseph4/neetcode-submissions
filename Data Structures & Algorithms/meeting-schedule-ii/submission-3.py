"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        start = []
        end = []
        res = 0
        for i in range(len(intervals)):
            start.append(intervals[i].start)
            end.append(intervals[i].end)
        start.sort()
        end.sort()
        # print(start)
        # print(end)
        s = 0
        e = 0
        curr = 0
        while s < len(start) and e < len(end):
            if start[s] < end[e]:
                curr+=1
                s+=1
                res = max(res, curr)
            else:
                curr-=1
                e+=1
        return res
        