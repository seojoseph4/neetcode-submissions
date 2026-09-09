class Solution:
    def rob(self, nums: List[int]) -> int:
        def helper(n):
            memo ={}
            def dfs(i):
                if i >= len(n):
                    return 0
                if i in memo:
                    return memo[i]
                memo[i] = max(dfs(i+1), dfs(i+2) + n[i])
                return memo[i]
            return dfs(0)
        if len(nums) == 1:
            return nums[0]
        return max(helper(nums[1:]), helper(nums[:-1]))