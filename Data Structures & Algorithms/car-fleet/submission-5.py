class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        res = 0
        
        #O(n)
        combined = [(p,s) for p, s in zip(position, speed)]
        #O(nlogn)
        combined.sort(reverse = True)

        last = None
        for p, s in combined:
            #time it takes = (target - position) / speed
            duration = (target - p) / s
            if not last or (last and duration > last):
                res+=1
                last = duration
            
        return res