class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = nums[0]
        added = nums[0]
        for i in range(1,len(nums)):
            added = max(added+nums[i], nums[i])
            res = max(added, res)
        return res

            
        

        