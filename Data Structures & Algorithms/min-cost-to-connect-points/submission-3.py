class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        res = 0
        seen = [0]*n
        dist = [float("inf")]*n

        dist[0] = 0
        for _ in range(n):
            u = -1
            for i in range(len(points)):
              if seen[i] == False and (u==-1 or dist[i] < dist[u]):
                u = i
            seen[u] = True
            res+=dist[u]

            for i in range(len(points)):
                dist[i] = min(dist[i], abs(points[i][0]-points[u][0]) + abs(points[i][1]-points[u][1]))
            

        return res

