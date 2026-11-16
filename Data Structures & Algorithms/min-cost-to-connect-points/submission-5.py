class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        dist = [float("inf")]*n
        seen = set()
        
        dist[0] = 0
        res = 0

        for _ in range(n):
            u = -1
            for i in range(n):
                if i not in seen and (u == -1 or dist[i] < dist[u]):
                    u = i
            seen.add(u)
            res+=dist[u]

            for j in range(n):
                manh = abs(points[u][0]-points[j][0]) + abs(points[u][1]-points[j][1])
                dist[j] = min(dist[j], manh)
        
        return res