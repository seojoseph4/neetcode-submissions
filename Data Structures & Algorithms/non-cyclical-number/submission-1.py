class Solution:
    def isHappy(self, n: int) -> bool:
        hs = set()
        def helper(num):
            if num == 1:
                return True
            if num in hs:
                return False
            hs.add(num)
            res = 0
            while num:
                digit = num% 10
                res += digit * digit
                num = num//10
            return helper(res)
        
        return helper(n)
        