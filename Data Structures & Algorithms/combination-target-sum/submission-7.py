class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        curr = []
        nums.sort()
        def dfs(i,runsum):
            if runsum > target:
                return
            if runsum == target:
                res.append(curr[:])
                return
            if i == len(nums):
                return
            
            for j in range(i,len(nums)):
                curr.append(nums[j])
                dfs(j,runsum+nums[j])
                curr.pop()
        dfs(0,0)
        return res

