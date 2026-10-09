class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        combined = [(p,s) for p,s in zip(position, speed)]

        combined.sort(reverse=True)

        last = 0
        res = 0
        for p,s in combined:
            arrivaltime = (target-p) / s
            # print(arrivaltime)
            if arrivaltime <= last:
                continue
            else:
                last = arrivaltime
                res+=1
        
        return res