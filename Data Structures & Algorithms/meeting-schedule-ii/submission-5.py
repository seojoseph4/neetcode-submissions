"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        starts = []
        ends = []
        for i in intervals:
            starts.append(i.start)
            ends.append(i.end)

        starts.sort()
        ends.sort()

        ps = 0
        pe = 0

        res = 0
        curr = 0
        while ps < len(starts):
            if starts[ps] < ends[pe]:
                curr+=1
                ps+=1
                res = max(res, curr)
            else:
                pe+=1
                curr-=1
        return res

        