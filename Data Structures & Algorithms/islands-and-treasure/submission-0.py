class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        def dfs(r, c, dis):
            if r < 0 or c < 0 or r >=len(grid) or c >=len(grid[0]):
                return
            if grid[r][c] == -1:
                return
            if grid[r][c] != 0:
                if grid[r][c] < dis:
                    return
                grid[r][c] = min(dis, grid[r][c])
            
            dfs(r+1, c, dis+1)
            dfs(r-1, c, dis+1)
            dfs(r, c+1, dis+1)
            dfs(r, c-1, dis+1)

            return 
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 0:
                    dfs(row, col, 0)
         

        