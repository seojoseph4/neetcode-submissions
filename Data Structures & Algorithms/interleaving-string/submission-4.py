class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:

        #decision to take a or b
        memo = {}
        def dfs(i, j, k):
            
            #Base Cases
            if k == len(s3) and i == len(s1) and j == len(s2):
                memo[(i,j,k)] = True
                return memo[(i,j,k)]
            if k == len(s3) and (i != len(s1) or j != len(s2)):
                memo[(i,j,k)] = False
                return memo[(i,j,k)]
            if (i,j,k) in memo:
                return memo[(i,j,k)]
            
            #Both matches, recurse both paths
            if i < len(s1) and s1[i] == s3[k] and j < len(s2) and s2[j] == s3[k]:
                memo[(i,j,k)] =  dfs(i+1, j, k+1) or dfs(i, j+1, k+1)
            #take from s1
            elif i < len(s1) and s1[i] == s3[k]:
                memo[(i,j,k)] = dfs(i+1, j, k+1)
            #take from s2
            elif j < len(s2) and s2[j] == s3[k]: 
                memo[(i,j,k)] =  dfs(i, j+1, k+1)
            else:
                memo[(i,j,k)] =  False

            return memo[(i,j,k)]
        
        return dfs(0, 0,0)
        
        