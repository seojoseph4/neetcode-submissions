class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:

        graph = defaultdict(list)
        for one, two in edges:
            graph[one].append(two)
            graph[two].append(one)

        visited = defaultdict()
        cycle = set()
        cycleStart = -1
        n = len(edges)
        def dfs(i, past):
            nonlocal cycleStart
            if i in visited:
                if visited[i] == True:
                    cycleStart = i
                    return True
            visited[i] = True
            for nei in graph[i]:
                if nei == past:
                    continue
                if dfs(nei, i):
                    if cycleStart != -1:
                        cycle.add(i)
                    if i == cycleStart:
                        cycleStart = -1
                    return True
            return False
        dfs(1,-1)
        for u, v in reversed(edges):
            if u in cycle and v in cycle:
                return [u, v]
        return []
            