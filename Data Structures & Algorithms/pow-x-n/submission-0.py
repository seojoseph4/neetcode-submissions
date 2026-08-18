class Solution:
    def myPow(self, x: float, n: int) -> float:
        res = 1.0
        neg = False
        if n== 0:
            return res
        if n < 0:
            neg = True
        n = abs(n)

        for i in range(n):
            res *= x

        if neg:
            res = 1/res
        
        return res