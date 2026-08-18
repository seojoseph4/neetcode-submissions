class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # dp = [0] * len(nums)
        # dpmin = [0]*len(nums)
        # dp[0] = nums[0]
        # dpmin[0] = nums[0]
        # res = dp[0]
        currMax=nums[0]
        currMin=nums[0]
        res = currMax

        for i in range(1, len(nums)):
            prevMax = currMax
            prevMin = currMin
            currMax = max(nums[i], nums[i]*prevMax, nums[i]*prevMin)
            currMin = min(nums[i], nums[i]*prevMax, nums[i]*prevMin)
            res = max(res, currMax)
        
        # print(dp)
        return res
            
        