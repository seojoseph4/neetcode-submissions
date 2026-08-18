class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n-1:
            return False

        parent = [i for i in range(n)]
        rank = [0]*n
        def find(n):
            if n!= parent[n]:
                parent[n] = find(parent[n])
            return parent[n]
        def union(n1, n2):
            p1, p2 = find(n1), find(n2)
            if p1 == p2:
                return False
            if rank[p1] > rank[p2]:
                parent[p2] = p1
                rank[p1]+=rank[p2]
            else:
                parent[p1] = p2
                rank[p2]+=rank[p1]
            return True

        res = n
        for n1, n2 in edges:
            if not union(n1,n2):
                return False
            else:
                res-=1
        return res==1
        