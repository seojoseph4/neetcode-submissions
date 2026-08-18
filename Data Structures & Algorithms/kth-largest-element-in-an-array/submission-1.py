class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def partition(l,r):
            pivotI = r
            i = l
            for j in range(l,r):
                if nums[j] > nums[pivotI]:
                    #swap with i
                    temp = nums[j]
                    nums[j] = nums[i]
                    nums[i] = temp
                    i+=1
            temp = nums[i]
            nums[i] = nums[pivotI]
            nums[pivotI] = temp
            return i

        l, r = 0, len(nums)-1
        k-=1
        while l <=r:
            p = partition(l, r)
            if p== k:
                return nums[k]
            elif p < k:
                l = p+1
            else:
                r = p-1
