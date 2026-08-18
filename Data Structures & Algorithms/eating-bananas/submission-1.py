import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)

        k = r

        while l <=r:
            m = (l+r)//2
            currhours = 0
            for p in piles:
                currhours += math.ceil(p/m)

            if currhours <= h:
                r = m-1
                k = min(k, m)
            else:
                l = m+1
        return k



