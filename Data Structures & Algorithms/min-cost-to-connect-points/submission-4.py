class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        res = 0
        seen = [0]*n
        dist = {i:float("inf") for i in range(n)}
        dist[0] = 0
        for _ in range(n):
            u = -1
            for v in range(n):
                if seen[v] == False and (u==-1 or dist[v] < dist[u]) :
                    u = v
            
            seen[u] = True
            res +=dist[u]
            for i in range(n):
                x,y = points[i]
                if seen[i] == False:
                    dist[i] = min(dist[i], abs(x-points[u][0])+abs(y-points[u][1]))
        
        return res
