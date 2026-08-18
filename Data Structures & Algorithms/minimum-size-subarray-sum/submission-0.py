class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l =0
        res = float("inf")
        cumsum = 0
        for r in range(len(nums)):
            cumsum+=nums[r]
            while cumsum >=target:
                res = min(res, r-l+1)
                cumsum-=nums[l]
                l+=1
        
        if res == float("inf"):
            return 0
        else:
            return res
                    
        