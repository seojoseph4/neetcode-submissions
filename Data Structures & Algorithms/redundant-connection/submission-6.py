class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0]*n
    def find(self, x):
        if self.parent[x] !=x:
            self.parent[x]=self.find(self.parent[x])
        return self.parent[x]
    def union(self, x,y):
        rootX, rootY = self.find(x), self.find(y)
        if rootX == rootY:
            return False
        if self.rank[rootX] < self.rank[rootY]:
            self.parent[rootX] = rootY
            self.rank[rootY] += self.rank[rootX]
        else:
            self.parent[rootY] = rootX
            self.rank[rootX] += self.rank[rootY]

        return True
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        dsu = DSU(n+1)
        for u,v in edges:
            if not dsu.union(u,v):
                return [u,v]
        return []