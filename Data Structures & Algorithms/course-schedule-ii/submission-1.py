class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        ad =defaultdict(list)

        for post, prereq in prerequisites:
            ad[post].append(prereq)
        
        seen = set()
        seeing = set()
        res = []
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
            res.append(currcourse)
            return True
        
        for n in range(numCourses):
            if n not in seen:
                if dfs(n) == False:
                    return []
        return res