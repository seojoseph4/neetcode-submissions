class Solution:
    def jump(self, nums: List[int]) -> int:
        res = 0
        currwindow = 0
        maxJump = 0

        for i in range(len(nums)-1):
            maxJump = max(maxJump, i+nums[i])

            if i == currwindow:
                res+=1
                currwindow = maxJump
            
                
        return res