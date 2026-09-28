class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        memo = {}
        def helper(i,j):
            if i == len(text1) or j == len(text2):
                return 0
            if (i,j) in memo:
                return memo[(i,j)]
            
            #when matching advance both, then decision is which one to advance when no match
            
            if text1[i] == text2[j]:
                res= 1 + helper(i+1,j+1)
            
            else:
                res= max(helper(i+1,j), helper(i, j+1))
            
            memo[(i,j)] = res
            return res
        
        return helper(0,0)