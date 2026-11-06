class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        
        intervals.sort(key = lambda x:x[0])


        hp = []
        hm = {}
        i = 0

        for q in sorted(queries):
            while i < len(intervals) and intervals[i][0] <= q:
                heapq.heappush(hp, [(intervals[i][1]-intervals[i][0]+1), intervals[i][1]])
                i+=1
            
            while hp and hp[0][1] < q:
                heapq.heappop(hp)

            hm[q] = hp[0][0] if hp else -1
        res = []
        for q in queries:
            res.append(hm[q])
        return res