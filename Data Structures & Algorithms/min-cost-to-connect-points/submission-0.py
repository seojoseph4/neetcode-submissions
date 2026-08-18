class DSU:
    def __init__(self, n):
        self.parent = list(range(n+1))
        self.rank = [1] * (n+1)
    def find(self, node):
        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]

    def union(self, u, v):
        pu = self.find(u)
        pv = self.find(v)
        if pu == pv:
            return False
        if self.rank[pu] > self.rank[pv]:
            self.rank[pu]+=self.rank[pv]
            self.parent[pv] = pu
        else:
            self.rank[pv]+=self.rank[pu]
            self.parent[pu] = pv
        return True


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        dsu = DSU(len(points))
        graph = []
        for i in range(len(points)):
            x1, y1 = points[i]
            for j in range(i+1, len(points)):
                x2, y2 = points[j]
                manhattan = abs(x1-x2) + abs(y1-y2)
                graph.append((manhattan, i, j))
        
        graph.sort()
        res = 0
        for dist, u, v in graph:
            if dsu.union(u,v):
                res+=dist

        return res


        print(graph)

        