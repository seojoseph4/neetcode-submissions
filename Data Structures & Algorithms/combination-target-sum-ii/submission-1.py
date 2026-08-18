class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res =[]
        candidates.sort()
        def dfs(i,curr, subset):
            if curr == target:
                res.append(subset.copy())
                return
            for j in range(i, len(candidates)):
                if j > i and candidates[j] == candidates[j-1]:
                    continue
                if curr > target:
                    return
                subset.append(candidates[j])
                dfs(j+1, curr+candidates[j],subset )
                subset.pop()

        dfs(0,0, [])
        return res