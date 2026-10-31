class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)
        for source, target, cost in times:
            adj[source].append((target, cost))

        minheap = [(0,k)]
        dist = {}

        while minheap:
            cost, node = heapq.heappop(minheap)
            if node in dist:
                continue
            dist[node] = cost
            for nei, cost2 in adj[node]:
                heapq.heappush(minheap, (cost+cost2, nei))
        
        if len(dist) != n:
            return -1
        else:
            return max(dist.values())

