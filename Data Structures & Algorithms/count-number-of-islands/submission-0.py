class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0

        def dfs(row, col):
            if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]):
                return False
            if grid[row][col] == "1":
                grid[row][col] = "0"
                dfs(row+1, col)
                dfs(row-1, col)
                dfs(row, col+1)
                dfs(row, col-1)
                return True
            else:
                return False
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if dfs(i, j):
                    res+=1
        return res
            

        