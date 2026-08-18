class Solution:
    def canJump(self, nums: List[int]) -> bool:
        dp = [False]*(len(nums))

        dp[-1] = True

        for i in range(len(nums)-2, -1, -1):
            for j in range(1,nums[i]+1):
                if dp[i+j] >= len(dp) or dp[i+j] == True:
                    dp[i] = True
                    break
        print(dp)
        return dp[0]
        