class DSU:
    def __init__(self, n):
        self.par = [i for i in range(n)]
        self.rank = [0]*n
    
    def find(self,x):
        if x != self.par[x]:
            self.par[x] = self.find(self.par[x])
        return self.par[x]
    
    def union(self,x,y):
        fx = self.find(x)
        fy = self.find(y)
        if fx == fy:
            return False
        
        if self.rank[fx] < self.rank[fy]:
            fx,fy = fx,fy
        self.par[fy] = fx
        if self.rank[fx]==self.rank[fy]:
            self.rank[fx]+=1


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        dsu = DSU(len(edges)+1)

        for u,v in edges:
            if dsu.union(u,v) == False:
                return [u,v]
        


