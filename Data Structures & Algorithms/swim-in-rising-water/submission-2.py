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
            for dx,dy in directions:
                nx,ny = r+dx, c+dy
                if nx < 0 or ny < 0 or nx >= rows or ny >= cols or (nx,ny) in seen:
                    continue 
                seen.add((nx,ny))
                heapq.heappush(minhp, (max(d,grid[nx][ny]),nx,ny))
