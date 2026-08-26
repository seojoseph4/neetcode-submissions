class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        pack = [(p,s) for p,s in zip(position,speed)]
        
        # time = (target - position[i]) / speed[i]

        pack.sort(reverse=True)
        stack = []
        for p,s in pack:
            time = (target - p) / s
            if stack and stack[-1] >= time:
                continue
            else:
                stack.append(time)
        
        return len(stack)

