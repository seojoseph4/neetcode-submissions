class Solution:
    def myPow(self, x: float, n: int) -> float:
        def helper(x, n):
            if n == 0:
                return 1
            if n == 1:
                return x
            res = helper(x, n//2)
            res = res * res
            if n %2 != 0:
                return x*res
            else:
                return res
        if x == 0:
            return 0
        neg = False
        if n== 0:
            return 1.0
        if n < 0:
            neg = True
        res  = helper(x,abs(n))
        if neg:
            return 1/res
        else:
            return res