class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pset = set()
        aset = set()
        
        rows = len(heights)
        cols = len(heights[0])
        def dfs(r,c, ocean, prev):
            if r < 0 or c < 0 or r== rows or c == cols or (r,c) in ocean or heights[r][c] <prev:
                return
            ocean.add((r,c))
            dfs(r + 1, c, ocean, heights[r][c])
            dfs(r - 1, c, ocean, heights[r][c])
            dfs(r, c + 1, ocean, heights[r][c])
            dfs(r, c - 1, ocean, heights[r][c])
            

        #pacific check
        for i in range(rows):
            dfs(i, 0, pset, heights[i][0])
            dfs(i, cols-1, aset, heights[i][cols-1])
        for j in range(cols):
            dfs(0,j,pset, heights[0][j])
            dfs(rows-1,j,aset, heights[rows-1][j])

        return list(list(coord) for coord in pset & aset)