class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxjump = 0
        for i, n in enumerate(nums):
            if i > maxjump:
                return False
            maxjump = max(maxjump, i+n)
        
        return True