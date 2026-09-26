class Solution:
    def getSum(self, a: int, b: int) -> int:
        MASK = 0xFFFFFFFF

        while b & MASK:
            carry = (a&b) << 1
            a = a^ b
            b = carry
        
        a&= MASK
        MAX_INT = 0x7FFFFFFF
        return a if a <= MAX_INT else a - 2**32

        