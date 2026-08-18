class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        p1=len(nums1)-len(nums2)-1
        p2=len(nums2)-1
        # print(nums1[p1])
        # print(nums2[p2])

        p3 = len(nums1)-1

        while p1 >= 0 and p2 >= 0:
            if nums1[p1] > nums2[p2]:
                nums1[p3] = nums1[p1]
                p1-=1
            else:
                nums1[p3] = nums2[p2]
                p2-=1 
            p3-=1
        
        while p2>=0:
            nums1[p3] = nums2[p2]
            p2-=1
            p3-=1
        

