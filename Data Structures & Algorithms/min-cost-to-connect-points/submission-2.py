class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        res = 0
        seen = [0]*n
        dist = [float("inf")]*n

        dist[0] = 0
        for _ in range(n):
            u = -1
            for i in range(n):
                if seen[i] == False and (u==-1 or dist[i] < dist[u]):
                    u = i
            seen[u] = True
            res+=dist[u]
            
            ux, uy = points[u]
            for v in range(n):
                if not seen[v]:
                    d = abs(ux - points[v][0]) + abs(uy - points[v][1])
                    if d < dist[v]:
                        dist[v] = d
        return res

