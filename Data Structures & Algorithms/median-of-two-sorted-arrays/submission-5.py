class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        if len(nums1) < len(nums2):
            A = nums1
            B = nums2
        else:
            A = nums2
            B = nums1

        total_length = len(A)+len(B)
        half = total_length // 2
        #left | right (right has more on odd cases)

        l = 0
        r = len(A)-1
        while True:
            mA = (l+r) //2
            #number of elements on left for A = (mA+1)
            # A + B = half
            # B = half - mA-1
            # mB = half - mA - 1 - 1
            mB = half - mA - 2

            #get the boundaries
            leftA = A[mA] if mA >= 0 else float("-inf")
            rightA = A[mA+1] if mA+1 < len(A) else float("inf")
            leftB = B[mB] if mB >= 0 else float("-inf")
            rightB = B[mB+1] if mB+1 < len(B) else float("inf")

            if leftA <= rightB and leftB <= rightA:
                #odd
                if total_length %2:
                    return min(rightA, rightB)
                #even
                else:
                    return (min(rightA, rightB) + max(leftA, leftB)) / 2
            elif leftA > rightB:
                r = mA-1
            else:
                l = mA+1


