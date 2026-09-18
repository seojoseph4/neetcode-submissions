class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = 0
        for n in nums:
            total+=n
        if total%2:
            return False
        target = total/2

        memo = {}
        def helper(i, runsum):
            if i == len(nums):
                return False
            if runsum == target:
                return True
            if (i, runsum) in memo:
                return memo[(i, runsum)]
            res = helper(i+1, runsum) or helper(i+1, runsum+nums[i])
            memo[(i,runsum)] = res
            return res
        
        return helper(0, 0)
            
