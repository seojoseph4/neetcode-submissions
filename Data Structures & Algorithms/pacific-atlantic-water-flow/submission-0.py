class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        res = []
        pacific = set()
        atlantic = set()

        def dfs(row, col, prev, seen):
            if (row, col) in seen:
                return
            if row < 0 or col < 0 or row >= len(heights) or col >= len(heights[0]):
                return
            if heights[row][col] < prev:
                return
            seen.add((row,col))
            dfs(row+1, col, heights[row][col], seen)
            dfs(row-1, col,heights[row][col], seen)
            dfs(row, col+1, heights[row][col], seen)
            dfs(row, col-1, heights[row][col], seen)

        for r in range(len(heights)):
            dfs(r, 0, heights[r][0], pacific)
            dfs(r, len(heights[0])-1, heights[r][len(heights[0])-1],atlantic)
        for c in range(len(heights[0])):
            dfs(0,c, heights[0][c], pacific)
            dfs(len(heights)-1, c, heights[len(heights)-1][c], atlantic)
        print(pacific)
        print(atlantic)
        for j in pacific:
            if j in atlantic:
                res.append([j[0],j[1]])
        return res




