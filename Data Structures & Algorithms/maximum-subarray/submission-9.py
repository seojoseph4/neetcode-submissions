class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ares = nums[0]
        res = 0
        for n in nums:
            res = max(res+n, n)
            ares = max(ares,res)
            # print(n, res, ares)
        return ares