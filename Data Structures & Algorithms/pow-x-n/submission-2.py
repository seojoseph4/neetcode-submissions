class Solution:
    def myPow(self, x: float, n: int) -> float:
        sign = -1 if n < 0 else 1
        n = abs(n)

        def helper(number,times):
            if times == 0:
                return 1
            if number == 0:
                return 0
            res = helper(number*number, times//2)
            if times % 2 == 1:
                return number * res
            else:
                return res
            

        if sign == -1:
            return 1/helper(x,n)
        return helper(x,n)