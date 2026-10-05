class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        memo = {}
        def helper(l,r):
            if l > r:
                return 0
            
            if (l,r) in memo:
                return memo[(l,r)]
            
            memo[(l,r)] = 0
            for i in range(l,r+1):
                res = nums[l-1] * nums[r+1] * nums[i]
                res+=helper(l,i-1) + helper(i+1,r)
                memo[(l,r)] = max(memo[(l,r)],res)
            
            return memo[(l,r)]
        
        return helper(1,len(nums)-2)

