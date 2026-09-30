class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        memo={}
        def helper(i,j):
            if j == len(t):
                return 1
            if i == len(s):
                return 0
            
            if (i,j) in memo:
                return memo[(i,j)]
            res = 0
            if s[i] == t[j]:
                res += helper(i+1,j+1)
            res+=helper(i+1,j)


            memo[(i,j)] = res
            return res
        return helper(0,0)
        