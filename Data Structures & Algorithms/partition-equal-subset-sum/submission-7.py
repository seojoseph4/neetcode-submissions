class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        
        if total % 2:
            return False
        target = total/2

        memo = {}
        def helper(i, runsum):
            if runsum == target:
                return True
            if i == len(nums):
                return False
            if (i, runsum) in memo:
                return memo[(i,runsum)]
            
            res = helper(i+1, runsum+nums[i]) or helper(i+1, runsum)
            memo[(i,runsum)] = res
            return res
        
        return helper(0,0)