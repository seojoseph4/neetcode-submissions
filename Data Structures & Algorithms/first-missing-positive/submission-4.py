class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        
        #first loop to get rid of all negatives
        for i in range(len(nums)):
            if nums[i] <= 0:
                nums[i] = len(nums)+1
        
        #second loop to makr all the numbers
        for i in range(len(nums)):

            if 1<=abs(nums[i]) <= len(nums):
                if nums[abs(nums[i])-1] >0:
                    nums[abs(nums[i])-1] *= -1
        
        
        for i in range(len(nums)):
            if nums[i] > 0:
                return i+1
        return len(nums)+1
        

        

