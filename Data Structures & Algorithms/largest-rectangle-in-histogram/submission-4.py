class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        # (startindex, height)
        res = 0

        for i in range(len(heights)):
            s = i
            while stack and stack[-1][1] > heights[i]:
                start, h = stack.pop()
                res = max(res, (i-start)*h)
                s = start
            stack.append((s, heights[i]))
        # print(stack)
        while stack:
            start, h = stack.pop()
            res = max(res, (len(heights)-start)*h)
        
        return res
