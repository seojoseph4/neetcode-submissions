class DSU:
    def __init__(self, n):
        self.par = [i for i in range(n)]
        self.rank = [0]* n
    def find(self,x):
        if self.par[x] != x:
            self.par[x] = self.find(self.par[x])
        return self.par[x]
    def union(self,x,y):
        px = self.find(x)
        py = self.find(y)
        if px == py:
            return False
        if self.rank[px] > self.rank[py]:
            px,py = py,px
        #py is greater
        self.par[px] = py
        if self.rank[px] == self.rank[py]:
            self.rank[py]+=1
        return True


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        dsu = DSU(n)
        edges = []
        for i in range(n):
            xi,yi = points[i]
            for j in range(i+1, n):
                xj, yj = points[j]
                edges.append((abs(xi-xj)+abs(yi-yj), i,j))
        edges.sort()

        total = used = 0
        for w, u, v in edges:
            if dsu.union(u,v):
                total +=w
                used+=1
                if used == n-1:
                    break
        return total

        