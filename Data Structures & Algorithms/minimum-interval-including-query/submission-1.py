class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        hm = {}

        for start, end in intervals:
            curr = (end-start+1)
            for i in range(start, end+1):
                if i in hm:
                    hm[i] = min(hm[i], curr)
                else:
                    hm[i] = curr
            
        res = []
        for q in queries:
            if q in hm:
                res.append(hm[q])
            else:
                res.append(-1)
        return res

        