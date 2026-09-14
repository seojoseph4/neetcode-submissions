"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key = lambda x: x.end)
        lastEnd = intervals[0].end if len(intervals) > 0 else 0
        for i in range(1, len(intervals)):
            start= intervals[i].start
            end = intervals[i].end
            if start < lastEnd:
                return False
            lastEnd = end
        
        return True
