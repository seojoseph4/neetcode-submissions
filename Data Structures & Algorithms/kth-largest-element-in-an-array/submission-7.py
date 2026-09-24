class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        target = len(nums)-k

        def quick(l,r):
            pivot = nums[r]
            p = l

            for i in range(l,r):
                if nums[i] < pivot:
                    nums[i], nums[p] = nums[p], nums[i]
                    p+=1

            nums[p], nums[r] = nums[r], nums[p]
            if p == target:
                return nums[p]
            elif p < target:
                return quick(p+1,r)
            else:
                return quick(l,p-1)
        return quick(0, len(nums)-1)
        