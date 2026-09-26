class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x < 0 else 1
        x = abs(x)

        res = 0

        while x:
            res = (res*10) + x%10
            x = x//10
        MAX_INT = 2**31 -1
        MIN_INT = -2**31
        res= res*sign
        return res if res <= MAX_INT and res >=MIN_INT else 0