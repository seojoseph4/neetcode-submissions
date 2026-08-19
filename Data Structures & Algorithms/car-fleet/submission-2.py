class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        time = {}
        
        for i in range(len(position)):
            currtime = (target - position[i]) / speed[i]
            time[position[i]] = currtime

        position.sort(reverse=True)
        # print(time)
        # print(position)
        stack = []
        res = 0
        for p in position:
            if stack and time[stack[-1]] >= time[p]:
                continue
            else:
                stack.append(p)

        return len(stack)