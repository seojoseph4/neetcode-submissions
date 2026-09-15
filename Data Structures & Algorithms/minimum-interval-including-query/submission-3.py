class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()
        minhp = []
        res = {}
        i = 0
        for q in sorted(queries):
            while i< len(intervals) and intervals[i][0] <= q:
                l,r = intervals[i]
                heapq.heappush(minhp, (r-l+1, r))
                i+=1
            while minhp and minhp[0][1] < q:
                heapq.heappop(minhp)
            res[q] = minhp[0][0] if minhp else -1

        return [res[q] for q in queries]