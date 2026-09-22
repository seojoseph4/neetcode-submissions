class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        total = len(nums1) + len(nums2)
        target = total //2

        if len(nums1) < len(nums2):
            l1 = nums1
            l2 = nums2
        else:
            l1 = nums2
            l2 = nums1
        
        l = 0
        r = len(l1)-1

        while True:
            mid1 = (l+r) //2
            mid2 = target - (mid1+1) -1

            left1 = l1[mid1] if mid1 >= 0 else float("-inf")
            right1 = l1[mid1+1] if mid1+1 < len(l1) else float("inf")
            left2 = l2[mid2] if mid2 >= 0 else float("-inf")
            right2 = l2[mid2+1] if mid2+1 < len(l2) else float("inf")
            if left1 <= right2 and left2 <=right1:
                if total % 2:
                    return min(right2, right1)
                else:
                    return (min(right1,right2) + max(left1, left2)) / 2
            elif left1 > right2:
                r = mid1-1
            else:
                l = mid1+1
        
            
        