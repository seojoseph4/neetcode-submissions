class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()

        res = 0
        fresh = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    fresh+=1
                if grid[i][j] == 2:
                    q.append((i,j))
        seen = set()
        while q:
            for t in range(len(q)):
                r,c = q.popleft()
                if r == len(grid) or c == len(grid[0]) or r < 0 or c < 0 or grid[r][c] == 0 or (r,c) in seen:
                    continue
                if grid[r][c] == 1:
                    fresh-=1
                    seen.add((r,c))
                q.append((r+1,c))
                q.append((r-1, c))
                q.append((r, c+1))
                q.append((r,c-1))
            if fresh == 0:
                break
            res+=1
        if fresh == 0:
            return res
        else:
            return -1