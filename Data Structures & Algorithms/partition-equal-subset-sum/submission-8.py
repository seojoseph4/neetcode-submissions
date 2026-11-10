class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total%2 != 0:
            return False
        
        target = total // 2
        memo = {}
        def helper(i,currsum):
            if currsum == target:
                return True
            if i>= len(nums):
                return False
            if (i,currsum) in memo:
                return memo[(i,currsum)]
            
            memo[(i,currsum)] = helper(i+1,currsum) or helper(i+1, currsum+nums[i])
            return memo[(i,currsum)]

        return helper(0,0)             
