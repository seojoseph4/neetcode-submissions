class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        temp = n
        for i in range(n):
            temp = temp^i
            temp = temp^nums[i]
        
        return temp
        

        