class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x: x[0])
        res=[intervals[0]]

        for i in range(1, len(intervals)):
            s = intervals[i][0]
            e = intervals[i][1]
            if res[-1][1] >= s:
                s1, e1 = res.pop()
                res.append([s1, max(e, e1)])
            else:
                res.append([s,e])
        
        return res