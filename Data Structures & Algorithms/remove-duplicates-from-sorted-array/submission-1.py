class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        p1 = 1
        for r in range(1, len(nums)):
            if nums[r] != nums[r-1]:
                nums[p1] = nums[r]
                p1+=1

        return p1


        