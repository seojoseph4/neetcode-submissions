class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x:x[0])
        res = 0
        last = intervals[0] if intervals else None
        for i in range(1, len(intervals)):
            s = intervals[i][0]
            e = intervals[i][1]
            if last[1] > s:
                res+=1
                last = [s, min(e,last[1])]
            else:
                last = [s,e]
        
        return res