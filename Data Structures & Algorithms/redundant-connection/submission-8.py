class DSU:
    def __init__(self,n):
        self.par = [i for i in range(n)]
        self.rank = [0]*n
    
    def find(self, x):
        if self.par[x] != x:
            self.par[x] = self.find(self.par[x])
        return self.par[x]

    def union(self,x,y):
        px =self.find(x)
        py = self.find(y)
        if px == py:
            return False
        
        if self.rank[px] < self.rank[py]:
            px, py = py, px
        #keep y as smaller one

        self.par[py] = px
        if self.rank[px] == self.rank[py]:
            self.rank[px]+=1
        return True

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        dsu = DSU(n+1)

        for u,v in edges:
            if not dsu.union(u,v):
                return [u,v]
        
        