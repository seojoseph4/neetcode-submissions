class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x < 0 else 1
        x = abs(x)
        res = 0
        while x:
            res = (res*10) + (x%10)
            x = x//10
        
        max_int = 2**31 - 1
        min_int = -2**31
        res = res* sign
        if res > max_int or res < min_int:
            return 0
        else:
            return res