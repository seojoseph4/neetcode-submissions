class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        # visited = set()
        count = 0
        res = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    count+=1
                if grid[row][col] == 2:
                    q.append((row, col))
        def addq(r, c):
            nonlocal count
            if r < 0 or c < 0 or r >=len(grid) or c >=len(grid[0]):
                return
            if grid[r][c] == 0:
                return
            if grid[r][c] == 1:
                count-=1
                grid[r][c] = 2
                q.append((r,c))
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                addq(r,c+1)
                addq(r, c-1)
                addq(r+1,c)
                addq(r-1,c)
            res+=1
        if count == 0:
            return max(0,res-1)
        else:
            return -1
