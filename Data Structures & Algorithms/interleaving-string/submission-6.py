class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        
        memo = {}
        def helper(i,j):
            if i + j == len(s3):
                if i == len(s1) and j == len(s2):
                    return True
                return False
            
            if (i,j) in memo:
                return memo[(i,j)]
            
            res = False
            if i < len(s1):
                if s1[i] == s3[i+j]:
                    res= res or  helper(i+1,j)
            
            if j < len(s2):
                if s2[j] == s3[i+j]:
                    res = res or helper(i,j+1)
            memo[(i,j)] = res
            return res
        
        return helper(0,0)