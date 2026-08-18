class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        res = 0
        intervals.sort(key = lambda i : i[0])
        
        closestEnd = intervals[0][1]
        res = 0
        for start, end in intervals[1:]:
            if start < closestEnd:
                res+=1
                closestEnd = min(closestEnd, end)
            else:
                closestEnd = end
        
        return res
        