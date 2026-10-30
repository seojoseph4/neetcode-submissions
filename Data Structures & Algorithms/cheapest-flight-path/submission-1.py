class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = defaultdict(list)
        for fr, to, price, in flights:
            adj[fr].append((to,price))
        
        minheap = []
        minheap.append([0,0,src])
        dist = {}
        while minheap:
            cost, edges, node = heapq.heappop(minheap)
            if node == dst:
                return cost
            if edges > k:
                continue
            if node in dist and dist[node]<=edges:
                continue
            dist[node] = edges
            for nei, price in adj[node]:
                heapq.heappush(minheap, (cost + price, edges + 1, nei))
        
        return -1
