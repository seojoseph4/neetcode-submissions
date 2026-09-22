class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        res = 0

        for i in range(len(heights)):
            indextopush = i
            while stack and stack[-1][0] > heights[i]:
                h, i2 = stack.pop()
                currarea = (i-i2) * h
                res = max(res, currarea)
                indextopush = i2
            stack.append([heights[i], indextopush])
        
        while stack:
            h, i2 = stack.pop()
            currarea = (len(heights)-i2) * h
            res = max(res, currarea)
            indextopush = i2


        return res