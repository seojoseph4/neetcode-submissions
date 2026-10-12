class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        curr = []
        candidates.sort()

        def dfs(i, runsum):
            if runsum == target:
                res.append(curr[:])
                return
            if runsum > target:
                return
            for j in range(i, len(candidates)):
                if j > i and candidates[j] == candidates[j-1]:
                    continue
                curr.append(candidates[j])
                dfs(j+1,runsum+candidates[j])
                curr.pop()
        

        dfs(0,0)
        return res