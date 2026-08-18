from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        i = 0
        while i <len(nums):
            if nums[i] > 0:
                break
            l = i+1
            r = len(nums)-1
            while l < r:
                total = nums[l]+nums[r]+nums[i]
                if total > 0:
                    r-=1
                elif total < 0:
                    l+=1
                else:
                    res.append([nums[l],nums[r],nums[i]])
                    while l < r and nums[l] == nums[l+1]:
                        l+=1
                    while l < r and nums[r] == nums[r-1]:
                        r-=1
                    l+=1
                    r-=1
            while i < len(nums)-1 and nums[i] == nums[i+1]:
                i+=1
            i+=1
        return res
            
