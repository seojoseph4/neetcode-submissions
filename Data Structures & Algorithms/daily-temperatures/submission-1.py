class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0]*len(temperatures)
        stack = []
        stack.append((temperatures[0], 0))
        for index, temp in enumerate(temperatures):
            for i in range(len(stack)-1,-1,-1):
                # print(stack)
                currVal = stack[i][0]
                currInd = stack[i][1]
                if temp > currVal:
                    res[currInd] = index - currInd
                    stack.pop()
            stack.append((temp, index))
        return res
