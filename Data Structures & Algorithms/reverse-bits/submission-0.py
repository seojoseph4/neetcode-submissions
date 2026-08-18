class Solution:
    def reverseBits(self, n: int) -> int:
        curr = 31
        res = 0
        while n >0:
            bit = n & 1
            res += (2**curr)*bit
            n = n>>1
            curr-=1
        return res