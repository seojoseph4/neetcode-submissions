class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        memo = {}

        def helper(i, j):
            if i == m or j ==n:
                return 0
            if i == m-1 and j == n-1:
                return 1
            
            if (i,j) in memo:
                return memo[(i,j)]

            res = helper(i+1, j) + helper(i, j+1)
            memo[(i,j)] = res
            return res
        
        return helper(0,0)
