class Solution:
    def reverse(self, x: int) -> int:
        negative = False
        if x < 0:
            negative = True
        x = abs(x)
        digit = 0 
        res = 0
        place = 10
        while x > 0:
            digit = x %10
            x = x // 10
            res = res*place + digit
            # print(x)
            # print("place", place)
            # print(res)
        if negative:
            res = -res
        if  res> 2147483647 or res < -2147483648:
            return 0
        return res
