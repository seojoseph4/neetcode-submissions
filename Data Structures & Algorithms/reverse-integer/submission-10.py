class Solution:
    def reverse(self, x: int) -> int:
        res = 0
        sign = -1 if x < 0 else 1
        x = abs(x)
        while x:
            res = (res*10) + (x%10)
            x = x//10
        
        max_int = 2**31 -1
        min_int = -2**31

        if res < min_int or res > max_int:
            return 0
        return res* sign