
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        visited = set()

        def dfs(row, col, region):
            # out of bounds = not surrounded
            if row < 0 or col < 0 or row >= len(board) or col >= len(board[0]):
                return False
            # if it's X, that's a wall = fine
            if board[row][col] == 'X':
                return True
            # skip if already visited
            if (row, col) in visited:
                return True

            visited.add((row, col))
            region.append((row, col))  # record cell in current region

            # check all 4 directions
            up = dfs(row - 1, col, region)
            down = dfs(row + 1, col, region)
            left = dfs(row, col - 1, region)
            right = dfs(row, col + 1, region)

            # region is surrounded only if all 4 sides return True
            return up and down and left and right

        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == 'O' and (r, c) not in visited:
                    region = []
                    if dfs(r, c, region):
                        for (x, y) in region:
                            board[x][y] = 'X'


            