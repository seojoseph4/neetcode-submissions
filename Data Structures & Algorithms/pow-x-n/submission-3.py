class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if x == 0:
            return 0
        negative = True if n < 0 else False
        n = abs(n)
        def helper(x,n):
            if n == 0:
                return 1
            if n == 1:
                return x
            
            if n % 2 == 0:
                return helper(x*x,n//2)
            else:
                return helper(x*x, n//2) * x
        
        return 1/helper(x,n) if negative else helper(x,n)
