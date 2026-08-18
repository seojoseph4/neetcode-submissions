class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0]*len(temperatures)

        for i in range(len(temperatures)):
            curr = (temperatures[i], i)
            while stack and stack[-1][0] < curr[0]:
                res[stack[-1][1]] = (i-stack[-1][1])
                stack.pop()
            stack.append(curr)
        return res

