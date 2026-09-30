class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        
        memo = {}
        def helper(i,j):
            if j >= len(p):
                return i == len(s)
            if (i,j) in memo:
                return memo[(i,j)]
            
            match = i < len(s) and (s[i] == p[j] or p[j] == ".")

            if j+1 < len(p) and p[j+1] == "*":
                memo[(i,j)] = helper(i, j+2) or (match and helper(i+1,j))

            elif match:
                memo[(i,j)] = helper(i+1,j+1)
            
            else:
                memo[(i,j)] = False
            return memo[(i,j)]

        return helper(0,0)
        