class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        
        hp = []
        res = {}

        intervals.sort(key=lambda x:x[0])
        i = 0
        for q in sorted(queries):
            while i < len(intervals) and intervals[i][0] <= q:
                heapq.heappush(hp, (intervals[i][1]-intervals[i][0]+1,i))
                i+=1
            # print(hp)
            while hp and intervals[hp[0][1]][1] < q:
                heapq.heappop(hp)
            
            res[q] = hp[0][0] if hp else -1
        
        tres = []
        for q in queries:
            tres.append(res[q])
        return tres


