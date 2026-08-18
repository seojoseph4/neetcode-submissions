class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #if graph has a cycle
        graph = defaultdict(list)
        for c1, c2 in prerequisites:
            graph[c2].append(c1)
        
        visited = set()
        def dfs(node):
            if node in visited:
                return False
            
            visited.add(node)
            for nei in graph[node]:
                if not dfs(nei):
                    return False
            visited.remove(node)
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False
        return True
            

            

        
        