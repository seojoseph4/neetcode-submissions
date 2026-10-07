class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = nums[0]
        runsum = 0
        for i in range(len(nums)):
            runsum+=nums[i]
            res = max(res, runsum)
            if runsum <0:
                runsum = 0
        return res

