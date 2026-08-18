class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack =[]
        res = 0
        for i in range(len(heights)):
            start = i
            while stack and stack[-1][1] > heights[i]:
                index, height = stack.pop()
                area = (i-index) * height
                res = max(res, area)
                start = index
            stack.append((start, heights[i]))
        
        while stack:
            index, height = stack.pop()
            area = (len(heights)-index) * height
            res = max(res, area)

        return res
        