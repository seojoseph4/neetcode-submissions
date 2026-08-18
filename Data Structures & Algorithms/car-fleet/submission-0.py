class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        formatted = []
        stack = []
        for i in range(len(position)):
            formatted.append((position[i], speed[i]))
        
        formatted.sort(key=lambda x: x[0], reverse = True)
        for pos, spd in formatted:
            time= (target - pos) / spd
            if not stack or time > stack[-1]:
                stack.append(time)
            
        return len(stack)

                

                
        print(formatted)