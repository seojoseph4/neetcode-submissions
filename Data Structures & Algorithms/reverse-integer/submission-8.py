class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x < 0 else 1

        res = 0
        x = abs(x)
        while x:
            res = (res * 10) + (x%10)
            x = x//10
        
        max_int = 2**31 -1
        min_int = -2**31+1
        if res > max_int or res < min_int:
            return 0
        return res * sign