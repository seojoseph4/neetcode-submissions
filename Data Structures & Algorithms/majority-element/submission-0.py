class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majority = None
        count = 0
        for n in nums:
            if count == 0:
                majority = n
            if n == majority:
                count+=1
            else:
                count-=1
        return majority