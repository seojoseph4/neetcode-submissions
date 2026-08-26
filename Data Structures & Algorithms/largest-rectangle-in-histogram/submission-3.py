class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # at each index, the largest one we can make we can find my expanding left and right until we reach one where the height is smaller

        #but O(n^2) 
        
        res = 0
        stack = []
        for i in range(len(heights)):
            index = i
            while stack and stack[-1][0] > heights[i]:
                h, start = stack.pop()
                res = max(res, (i-start)* h)
                index = start
            stack.append([heights[i], index])
        
        while stack:
            h, start = stack.pop()
            res = max(res, (len(heights)-start) * h)
        
        return res
