class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        q = deque()
        visited = set()
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 0:
                    q.append([row,col])
                    visited.add((row,col))

        dist = 0
        def addland(r,c):
            if r<0 or r>=len(grid) or c < 0 or c >=len(grid[0]) or (r,c) in visited or grid[r][c] == -1:
                return
            visited.add((r,c))
            q.append([r,c])
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = dist   
                addland(r+1, c)
                addland(r-1, c)
                addland(r, c+1)
                addland(r,c-1)
            dist+=1      

        