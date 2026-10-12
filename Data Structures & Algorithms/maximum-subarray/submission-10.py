class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = float("-inf")
        runmax = float("-inf")

        for n in nums:
            runmax = max(runmax+n, n)
            res = max(runmax, res)
        
        return res