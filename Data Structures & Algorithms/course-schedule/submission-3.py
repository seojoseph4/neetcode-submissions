class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # build adjacency array
        ad =defaultdict(list)

        for post, prereq in prerequisites:
            ad[post].append(prereq)
        
        seen = set()
        seeing = set()
        def dfs(currcourse):
            seen.add(currcourse)
            seeing.add(currcourse)
            for nei in ad[currcourse]:
                if nei in seeing:
                    return False
                if nei in seen:
                    continue
                
                if dfs(nei) == False:
                    return False
            seeing.remove(currcourse)
            return True
        
        for n in range(numCourses):
            if n not in seen:
                if dfs(n) == False:
                    return False
        return True
