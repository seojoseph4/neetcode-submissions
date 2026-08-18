class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowd = defaultdict(set)
        cold = defaultdict(set)
        squd = defaultdict(set)
        for row in range(len(board)):
            for col in range(len(board[row])):
                if board[row][col] == ".":
                    continue
                if (board[row][col] in rowd[row]) or (board[row][col] in cold[col]) or (board[row][col] in squd[(row//3, col//3)]):
                    return False

                rowd[row].add(board[row][col])
                cold[col].add(board[row][col])
                squd[(row//3,col//3)].add(board[row][col])
        return True

