class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        p1 = 0
        p2 = 0
        hs = set()
        k = 0
        while p1 < len(nums):
            if nums[p1] not in hs:
                hs.add(nums[p1])
                #place the number
                nums[p2] = nums[p1]
                p2+=1
                p1+=1
            else:
                p1+=1

        return len(hs)


        