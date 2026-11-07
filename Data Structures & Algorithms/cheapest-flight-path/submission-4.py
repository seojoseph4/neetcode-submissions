class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = defaultdict(list)
        for fr, to, price in flights:
            adj[fr].append((to,price))
        
        dist = {}
        minheap = [(0,0,src)] #cost, stops, node

        while minheap:
            cost, stop, node = heapq.heappop(minheap)
            if node == dst:
                return cost
            if stop > k:
                continue
            if node in dist and dist[node] <= stop:
                continue

            dist[node] = stop
            for nei, c in adj[node]:
                heapq.heappush(minheap, (cost+c, stop+1, nei))
        
        return -1