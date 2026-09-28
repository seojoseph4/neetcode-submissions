class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        memo = {}
        def helper(i, runsum):
            if i == len(nums):
                if runsum == target:
                    return 1
                else:
                    return 0

            if (i, runsum) in memo:
                return memo[(i, runsum)]
            
            sub = helper(i+1, runsum-nums[i])
            add = helper(i+1, runsum+nums[i])

            memo[(i, runsum)] = add+sub
            return memo[(i, runsum)]
        
        return helper(0,0)