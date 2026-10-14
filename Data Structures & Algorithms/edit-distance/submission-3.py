class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
        memo = {}
        def helper(i,j):
            if i == len(word1):
                return len(word2) - j
            if j == len(word2):
                return len(word1) - i
            
            if (i,j) in memo:
                return memo[(i,j)]

            if word1[i] == word2[j]:
                res = helper(i+1,j+1)
            else:
                #insert
                res = 1+ helper(i,j+1)
                #delete
                res = min(1+ helper(i+1,j), res)
                #replace
                res = min(1+helper(i+1,j+1), res)
            memo[(i,j)] = res
            return res
        
        return helper(0,0)