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

        starts.sort()
        ends.sort()

        sp, ep = 0,0

        res = 0
        curr = 0
        while sp < len(starts) and ep < len(ends):
            if starts[sp] < ends[ep]:
                curr+=1
                sp+=1
            else:
                curr-=1
                ep+=1
            res = max(res, curr)
        
        return res

