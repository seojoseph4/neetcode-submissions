class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        rows = len(grid)
        cols = len(grid[0])
        minhp = [(grid[0][0],0,0)]
        seen = set()

        while minhp:
            d, r,c = heapq.heappop(minhp)
            
            if r == rows-1 and c == cols-1:
                return d
            
            if (r,c) in seen:
                continue
            seen.add((r,c))
            for dx, dy in directions:
                nr = dx+r
                nc = dy+c
                if nr < 0 or nc < 0 or nr >= rows or nc >= cols:
                    continue
                heapq.heappush(minhp, (max(d,grid[nr][nc]),nr,nc))
