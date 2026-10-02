class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        target = len(nums)-k 
        def quick(l,r):
            pivotVal = nums[r]
            p = l

            for i in range(l,r):
                if nums[i] < pivotVal:
                    nums[i], nums[p] = nums[p], nums[i]
                    p+=1
            
            nums[r], nums[p] = nums[p], nums[r]
            if p == target:
                return nums[p]
            elif p > target:
                return quick(l,p-1)
            else:
                return quick(p+1,r)
            
        return quick(0,len(nums)-1)

        