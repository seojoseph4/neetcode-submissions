class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        l = 0
        r = len(height)-1
        lmax = height[l]
        rmax = height[r]
        res = 0

        while l < r:
            if lmax <= rmax:
                #means left is guaranteed lower
                l+=1
                
                res+=max(0,lmax-height[l])
                lmax = max(lmax, height[l])
            else:
                r-=1
                res+=max(0,rmax-height[r])
                rmax = max(rmax, height[r])

        return res

