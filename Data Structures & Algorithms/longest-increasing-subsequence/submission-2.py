class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [0]*len(nums)
        dp[0] = 1
        res = dp[0]

        for i in range(1, len(nums)):
            dp[i] = 1
            for j in range(i-1,-1,-1):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i],1+ dp[j])
            res = max(res, dp[i])
        return res
        



        