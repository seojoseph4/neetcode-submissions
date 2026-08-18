class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        res = n

        parent = [i for i in range(n)]
        rank = [0]*n


        def find(n):
            if n != parent[n]:
                parent[n] = find(parent[n])
            return parent[n]
        def union(n1, n2):
            p1, p2 = find(n1), find(n2)
            if p1 == p2:
                return False
            if rank[p1] > rank[p2]:
                parent[p2] = p1
                rank[p1] += rank[p2]
            else:
                parent[p1] = p2
                rank[p2] += rank[p1]
            return True
                
        for n1, n2 in edges:
            if union(n1,n2):
                res-=1
        return res
         