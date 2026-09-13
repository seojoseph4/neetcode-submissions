class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # build adjacency array
        hm = defaultdict(list)
        for post, pre in prerequisites:
            hm[post].append(pre)
        
        seen = set()
        seeing = set()
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
            return True
        print(hm)
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True
