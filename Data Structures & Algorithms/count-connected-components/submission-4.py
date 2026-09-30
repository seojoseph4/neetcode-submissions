class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = defaultdict(list)
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
        

        seen = set()
        def dfs(curr, parent):
            if curr in seen:
                return 
            seen.add(curr)
            for nei in adj[curr]:
                dfs(nei, curr)

        res = 0
        for i in range(n):
            if i not in seen:
                dfs(i,-1)
                res+=1
        return res