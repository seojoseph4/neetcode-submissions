class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        memo = {}

        nums = [1] + nums +[1]

        def helper(l,r):
            if l > r:
                return 0
            if (l,r) in memo:
                return memo[(l,r)]
            
            res = 0
            for i in range(l,r+1):
                curr = nums[l-1] * nums[r+1] * nums[i]
                curr+= helper(l,i-1) + helper(i+1,r)
                res = max(res, curr)
            
            memo[(l,r)] =res
            return res
        
        return helper(1,len(nums)-2)