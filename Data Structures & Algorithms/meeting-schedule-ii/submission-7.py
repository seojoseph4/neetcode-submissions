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
        sp = 0
        ep = 0
        res = 0
        count = 0
        while sp < len(starts) and ep < len(ends):
            if starts[sp] < ends[ep]:
                sp+=1
                count+=1
            else:
                ep +=1
                count-=1
            res = max(res, count)
        return res
        

        return res