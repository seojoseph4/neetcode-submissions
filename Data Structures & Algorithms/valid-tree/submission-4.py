class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = defaultdict(list)
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        seen = set()
        def helper(i, parent):
            if i in seen:
                return False
            seen.add(i)

            for nei in adj[i]:
                if nei == parent:
                    continue
                else:
                    if helper(nei, i) == False:
                        return False
            return True
        
        res = helper(0,-1)
        if len(seen) != n:
            return False
        else:
            return res