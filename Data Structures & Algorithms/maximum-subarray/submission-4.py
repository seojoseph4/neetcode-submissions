class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = runsum = nums[0]
        for n in nums[1:]:
            runsum = max(n, runsum + n)   # extend, or start fresh at n
            res = max(res, runsum)
        return res

