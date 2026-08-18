class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = 0
        l = 0
        r = len(heights)-1
        while l < r:
            height = min(heights[r], heights[l])
            res = max(res, height*(r-l))
            if heights[r] >= heights[l]:
                l+=1
            else:
                r-=1
        return res