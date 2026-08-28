class TrieNode():
    def __init__(self):
        self.children = {}
        self.end = False
class Trie():
    def __init__(self):
        self.root = TrieNode()

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        t = Trie()
        curr = t.root
        for word in words:
            curr = t.root
            for c in word:
                if c not in curr.children:
                    curr.children[c] = TrieNode()
                curr = curr.children[c]
            curr.end = True
        rows = len(board)
        cols = len(board[0])

        res= set()
        word = []
        def bt(r, c, node):
            if r < 0 or c < 0 or r >= rows or c >= cols or board[r][c] not in node.children or board[r][c] == ".":
                return
            curr = board[r][c]
            word.append(curr)
            board[r][c] ="."
            node = node.children[curr]
            if node.end:
                res.add("".join(word))
            bt(r+1,c, node)
            bt(r-1,c, node)
            bt(r,c+1, node)
            bt(r,c-1, node)
            board[r][c] = curr
            word.pop()
        for r in range(rows):
            for c in range(cols):
                bt(r,c,t.root)
        
        return list(res)

            
        