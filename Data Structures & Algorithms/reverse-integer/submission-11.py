class Solution:
    def reverse(self, x: int) -> int:
        max_int = 2**31 -1
        min_int = -2**31

        sign = -1 if x < 0 else 1

        x = abs(x)
        res = 0
        while x:
            digit = x % 10
            res = (res*10) + digit
            x = x//10
        
        res = res * sign
        if res > max_int or res < min_int:
            return 0
        else:
            return res