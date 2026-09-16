class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = defaultdict(list)
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
        

        seeing = set()
        def dfs(curr, par):
            if curr in seeing:
                return False
            seeing.add(curr)
            for nei in adj[curr]:
                if nei == par:
                    continue
                if not dfs(nei, curr):
                    return False
            return True
        
        return dfs(0,-1) and len(seeing) == n