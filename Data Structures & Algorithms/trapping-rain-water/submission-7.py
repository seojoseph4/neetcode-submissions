class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0

        l, r = 0, len(height)-1

        lmax = height[l]
        rmax = height[r]

        while l <= r:

            if lmax < rmax:
                res+=max(0,(lmax-height[l]))
                l+=1
                lmax = max(lmax, height[l])
            else:
                res+=max(0, (rmax-height[r]))
                r-=1
                rmax = max(rmax, height[r])
        return res
