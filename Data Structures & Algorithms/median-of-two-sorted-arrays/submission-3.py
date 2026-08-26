class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        #brute force would be to just merge the two arrays and iterate to find it
        #but faster way, key idea is that median has half elements to each side
        # so we can use one of the arrays binary search for a partition, verify that the partition is correct, if not continue the search, etc

        
        if len(nums1) < len(nums2):
            A = nums1
            B = nums2
        else:
            A = nums2
            B = nums1
        
        l, r = 0, len(A)-1
        total = len(A) + len(B)
        half = total //2
        #round down the half

        while True:
            m = (l+r)//2
            # index 3 --> 4 elements
            #if half is 6 elemnts
            m2 = half - m-2

            leftA = A[m] if m >= 0 else float("-inf")
            rightA = A[m+1] if m+1 < len(A) else float("inf")
            leftB = B[m2] if m2 >= 0 else float("-inf")
            rightB = B[m2+1] if m2+1 < len(B) else float("inf")

            if leftA <= rightB and leftB <= rightA:
                if total %2:
                    #odd
                    return min(rightA, rightB)
                else:
                    #even
                    return (min(rightA, rightB) + max(leftA, leftB)) / 2
            elif leftA > rightB:
                r = m-1
            else:
                l = m+1