class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []

        i = 0
        while i < len(intervals) and intervals[i][1] < newInterval[0]:
            res.append(intervals[i])
            i+=1
        
        merged = newInterval
        while i < len(intervals) and intervals[i][0] <= newInterval[1]:
            merged[0] = min(merged[0],intervals[i][0])
            merged[1] = max(merged[1],intervals[i][1])
            i+=1
        res.append(merged)

        while i < len(intervals):
            res.append(intervals[i])
            i+=1
        
        return res
