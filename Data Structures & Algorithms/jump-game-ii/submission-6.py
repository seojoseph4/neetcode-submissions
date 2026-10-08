class Solution:
    def jump(self, nums: List[int]) -> int:
        currentWindow = 0
        nextWindow = 0
        jumps = 0
        for i in range(len(nums)-1):
            nextWindow = max(nextWindow,i+nums[i])
            if i == currentWindow:
                currentWindow = nextWindow
                jumps+=1
            

        return jumps