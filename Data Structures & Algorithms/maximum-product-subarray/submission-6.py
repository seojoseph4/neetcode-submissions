class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        #decision to take or not take
        res= nums[0]
        currMin = 1
        currMax = 1
        
        for n in nums:
            temp = n * currMax
            currMax = max(n*currMin, n*currMax, n)
            currMin = min(temp, n*currMin, n)
            res = max(res, currMax)
        return res
