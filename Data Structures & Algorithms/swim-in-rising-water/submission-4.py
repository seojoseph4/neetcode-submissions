class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        
        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        rows = len(grid)
        cols = len(grid[0])
        minheap = [(grid[0][0],0,0)]
        seen = set()
        while minheap:
            d,r,c = heapq.heappop(minheap)
            if r == rows-1 and c == cols-1:
                return d
            if (r,c) in seen:
                continue
            seen.add((r,c))
            for dx,dy in directions:
                nx = dx+r
                ny = dy+c
                if nx <0 or ny <0 or nx == rows or ny == cols:
                    continue
                heapq.heappush(minheap, (max(d,grid[nx][ny]), nx,ny))
        
