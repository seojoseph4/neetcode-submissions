class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = nums[0]
        runmax = 0

        for n in nums:
            runmax = max(n, runmax+n)
            res = max(res, runmax)
        
        return res