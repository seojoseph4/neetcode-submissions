class Solution:
    def rob(self, nums: List[int]) -> int:
        res = 0


        def helper(l):
            memo = {}
            def dp(i):
                if i >= len(l):
                    return 0
                if i in memo:
                    return memo[i]
                
                temp = max(dp(i+2)+l[i], dp(i+1))
                memo[i] = temp
                return memo[i]
            return dp(0)
        if len(nums) == 1:
            return nums[0]
        return max(helper(nums[1:]) , helper(nums[:len(nums)-1]))
                
