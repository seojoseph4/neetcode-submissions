class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = defaultdict(list)
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
        

        seen = set()
        def dfs(curr):
            seen.add(curr)
            for nei in adj[curr]:
                if nei in seen:
                    continue
                dfs(nei)

        res = 0
        for i in range(n):
            if i not in seen:
                dfs(i)
                res+=1
        return res