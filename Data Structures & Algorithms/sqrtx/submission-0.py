class Solution:
    def mySqrt(self, x: int) -> int:
        l, r = 0,x

        res = 0
        while l <=r:
            m = (l+r)//2
            if m*m > x:
                r = m-1
            if m*m <= x:
                l = m+1
                res = max(res, m)
        
        return res

            
        