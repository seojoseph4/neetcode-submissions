class Solution:
    def numDecodings(self, s: str) -> int:
        
        memo = {}
        def helper(i):
            if i >= len(s):
                return 1
            if i in memo:
                return memo[i]
            if s[i] == "0":
                return 0
            
            res = helper(i+1)

            if i + 1 <len(s) and "10"<=s[i:i+2] <="26":
                res+= helper(i+2)

            memo[i] = res
            return res
        
        return helper(0)
            
