class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        tickets.sort(reverse=True)
        adj = defaultdict(list)
        for fro, to in tickets:
            adj[fro].append(to)
        print(adj)
        res = []
        def dfs(node):
            
            while adj[node]:
                dfs(adj[node].pop())
            
            res.append(node)
        dfs("JFK")
        return res[::-1]
