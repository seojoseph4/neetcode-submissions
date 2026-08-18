class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        lmax = [0]*len(height)
        rmax = [0]*len(height)

        currmax = 0
        for i in range(len(height)):
            lmax[i] = currmax
            currmax = max(currmax, height[i])
        currmax = 0
        for i in range(len(height)-1, -1, -1):
            rmax[i] = currmax
            currmax = max(currmax, height[i])
        
        res = 0
        for i in range(len(height)):
            curr = min(lmax[i], rmax[i]) - height[i]
            if curr > 0:
                res+=curr
        return res
