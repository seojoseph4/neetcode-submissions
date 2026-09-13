class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        hm = defaultdict(list)
        for post, pre in prerequisites:
            hm[post].append(pre)
        
        seen = set()
        seeing = set()
        res= []
        def dfs(curr):
            if curr in seen:
                return True
            if curr in seeing:
                return False
            seeing.add(curr)
            if curr in hm:
                for pre in hm[curr]:
                    if not dfs(pre):
                        return False
            seeing.remove(curr)
            seen.add(curr)
            res.append(curr)
            return True
        for i in range(numCourses):
            if not dfs(i):
                return []
        return res
        
