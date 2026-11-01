class Solution:
    def jump(self, nums: List[int]) -> int:
        maxjump = 0
        currentwindow = 0
        res = 0
        for i in range(len(nums)-1):
            maxjump = max(maxjump, nums[i]+i)
            if i == currentwindow:
                res+=1
                currentwindow = maxjump
        
        return res