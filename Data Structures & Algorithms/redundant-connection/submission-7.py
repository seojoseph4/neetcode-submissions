class DSU:
    def __init__(self,n):
        self.par = [i for i in range(n)]
        self.rank = [0]*n

    def find(self,x):
        if x != self.par[x]:
            self.par[x] = self.find(self.par[x])
        return self.par[x]
    def union(self,x,y):
        px, py = self.find(x), self.find(y)
        if px==py:
            return False
        if self.rank[px] > self.rank[py]:
            px,py = py,px
        self.par[px] = py
        if self.rank[px] == self.rank[py]:
            self.rank[py]+=1
        return True
        
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        d = DSU(n+1)

        for u, v in edges:
            if not d.union(u,v):
                return [u,v]