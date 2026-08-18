class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        for c1, c2 in prerequisites:
            graph[c1].append(c2)
        res = []
        visited = set()
        cycle = set()
        def dfs(node):
            if node in cycle:
                return False
            if node in visited:
                return True

            cycle.add(node)
            for nei in graph[node]:
                if dfs(nei) == False:
                    return False

            cycle.remove(node)
            visited.add(node)
            res.append(node)
            return 

        for i in range(numCourses):
            if dfs(i) == False:
                return []
            
        return res