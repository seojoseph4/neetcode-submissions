class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        p1 = 0
        p2 = len(nums)-1
        k%= len(nums)

        while p1 < p2:
            nums[p1], nums[p2] = nums[p2], nums[p1]
            p1+=1
            p2-=1
        
        p1 = 0
        p2 = k-1

        while p1 < p2:
            nums[p1], nums[p2] = nums[p2], nums[p1]
            p1+=1
            p2-=1

        p1 = k
        p2 = len(nums)-1

        while p1 < p2:
            nums[p1], nums[p2] = nums[p2], nums[p1]
            p1+=1
            p2-=1



        


        