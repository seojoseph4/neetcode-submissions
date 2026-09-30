class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        memo={}
        def helper(i,j):
            if (i,j) in memo:
                return memo[(i,j)]
            res = 1
            for r,c in [(0,1),(0,-1),(1,0),(-1,0)]:
                nr = i+r
                nc = j+c
                if nr< 0 or nc <0 or nr == len(matrix) or nc == len(matrix[0]):
                    continue
                else:
                    if matrix[nr][nc] > matrix[i][j]:
                        res = max(res,helper(nr,nc)+1)
            
            memo[(i,j)] = res
            return res
        res = 0
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                res = max(res,helper(r,c))
        return res