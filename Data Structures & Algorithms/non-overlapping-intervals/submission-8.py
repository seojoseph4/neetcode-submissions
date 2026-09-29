class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x:x[0])

        lastEnd = intervals[0][1]
        res = 0
        for i in range(1, len(intervals)):
            s = intervals[i][0]
            e = intervals[i][1]
            if s < lastEnd:
                res+=1
                lastEnd = min(e, lastEnd)
            else:
                lastEnd = e
        
        return res