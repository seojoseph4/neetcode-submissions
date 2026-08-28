class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        curr = []
        candidates.sort()

        def bt(index, runsum):
            if runsum == target:
                res.append(curr.copy())
                return
            
            for j in range(index, len(candidates)):
                if j > index and candidates[j-1] == candidates[j]:
                    continue
                if runsum + candidates[j] > target:
                    return
                curr.append(candidates[j])
                bt(j+1, runsum+candidates[j])
                curr.pop()

        bt(0, 0)
        return res
        