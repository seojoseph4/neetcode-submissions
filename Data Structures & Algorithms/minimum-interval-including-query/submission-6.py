class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort(key = lambda x:x[0])

        hp = []
        res= {}
        i = 0
        for q in sorted(queries):
            while i < len(intervals) and intervals[i][0] <= q:
                l,r = intervals[i]
                heapq.heappush(hp,((r-l+1),l,r))
                i+=1
            
            while hp and hp[0][2] < q:
                heapq.heappop(hp)
            
            res[q] = hp[0][0] if len(hp) > 0 else -1

        
        return [res[q] for q in queries]
