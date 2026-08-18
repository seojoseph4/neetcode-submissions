class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        res = 0
        def dfs(i, currsum):
            nonlocal res
            if i == len(nums) and currsum == target:
                res+=1
                return True
            if i == len(nums):
                return False
            dfs(i+1, currsum+nums[i])
            dfs(i+1, currsum-nums[i])
        
        dfs(0, 0)
        return res