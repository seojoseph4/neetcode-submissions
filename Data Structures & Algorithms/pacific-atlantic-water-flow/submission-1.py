class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pset = set()
        aset = set()
        
        rows = len(heights)
        cols = len(heights[0])
        seen = set()
        def dfs(r,c, ocean):
            if r < 0 or c < 0 or r== rows or c == cols or (r,c) in seen:
                return
            currh = heights[r][c]
            seen.add((r,c))
            ocean.add((r,c))
            if r+1 < rows and heights[r+1][c] >= currh:
                dfs(r+1,c, ocean)
            if r-1 >= 0 and heights[r-1][c] >= currh:
                dfs(r-1,c, ocean)
            if c+1 < cols and heights[r][c+1] >= currh:
                dfs(r, c+1, ocean)
            if c-1 >=0 and heights[r][c-1] >= currh:
                dfs(r,c-1,ocean)
            

        #pacific check
        for i in range(rows):
            dfs(i, 0, pset)
        for j in range(cols):
            dfs(0,j,pset)

        seen = set()


        #atlantic check
        for i in range(rows):
            dfs(i, cols-1, aset)
        for j in range(cols):
            dfs(rows-1,j,aset)


        return list(pset & aset)