class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        if len(nums1) < len(nums2):
            A = nums1
            B = nums2
        else:
            A = nums2
            B = nums1

        total_length = len(A) + len(B)
        half = total_length // 2

        l = 0
        r = len(A) - 1

        while True:
            m = (l + r) // 2
            m2 = half - m - 2

            Aleft = A[m] if m >= 0 else float("-inf")
            Bleft = B[m2] if m2 >= 0 else float("-inf")

            Aright = A[m + 1] if m + 1 < len(A) else float("inf")
            Bright = B[m2 + 1] if m2 + 1 < len(B) else float("inf")

            if Aleft <= Bright and Bleft <= Aright:

                if total_length % 2:
                    return min(Aright, Bright)

                else:
                    return (
                        max(Aleft, Bleft) +
                        min(Aright, Bright)
                    ) / 2

            elif Aleft > Bright:
                r = m - 1

            else:
                l = m + 1