class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)
        for u,v, w in times:
            adj[u].append((v,w))
        
        minhp = [(0,k)]
        dist = {}

        while minhp:
            d, node = heapq.heappop(minhp)
            if node in dist:
                continue
            dist[node] = d
            for nei,w in adj[node]:
                if nei in dist:
                    continue
                heapq.heappush(minhp, (d+w, nei))
        return -1 if len(dist) != n else max(dist.values())
            
