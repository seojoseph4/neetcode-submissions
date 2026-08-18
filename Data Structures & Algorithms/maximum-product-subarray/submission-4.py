class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        dp = [0] * len(nums)
        dpmin = [0]*len(nums)
        dp[0] = nums[0]
        dpmin[0] = nums[0]
        res = dp[0]

        for i in range(1, len(nums)):
            dp[i] = max(nums[i]*dp[i-1], nums[i],nums[i]*dpmin[i-1])
            dpmin[i] = min(nums[i]*dpmin[i-1],nums[i]*dp[i-1], nums[i])
            res = max(res, dp[i])
        
        print(dp)
        return res
            
        