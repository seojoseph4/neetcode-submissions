"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        starts = [i.start for i in intervals]
        ends = [i.end for i in intervals]
        res = curr = 0
        i = j= 0
        starts.sort()
        ends.sort()
        while i < len(starts) and j < len(ends):
            if starts[i] < ends[j]:
                curr+=1
                i+=1
                res = max(res, curr)
            else:
                curr-=1
                j+=1
        return res
        