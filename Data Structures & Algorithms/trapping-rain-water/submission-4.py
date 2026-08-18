class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        lmax = 0
        rmax = 0
        walls = [[0,0] for _ in range(len(height))]
        res = 0

        for i in range(len(height)):
            walls[i][0] = lmax
            lmax = max(lmax, height[i])
        
        for j in range(len(height)-1,-1,-1):
            walls[j][1] = rmax
            rmax = max(rmax, height[j])

        for k in range(len(height)):

            res+=max(0,min(walls[k][0], walls[k][1]) - height[k])

        return res

