class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        res = 0
        memo = {}
        def dfs(i, currsum):
            if i == len(nums) and currsum == target:
                return 1
            if i == len(nums):
                return 0
            if (i, currsum) in memo:
                return memo[(i, currsum)]
            ways= dfs(i+1, currsum+nums[i]) + dfs(i+1, currsum-nums[i])
            memo[(i, currsum)] = ways
            return ways
        
        return dfs(0, 0)
