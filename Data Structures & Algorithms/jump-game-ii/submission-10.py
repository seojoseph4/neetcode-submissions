class Solution:
    def jump(self, nums: List[int]) -> int:
        maxjump = 0
        res = 0
        runningwindow = 0
        for i in range(len(nums)-1):
            n = nums[i]
            runningwindow = max(runningwindow, i+n)
            if i == maxjump:
                res+=1
                maxjump = runningwindow
                
            
        
        return res