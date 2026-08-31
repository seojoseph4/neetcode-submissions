class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False
class Trie:
    def __init__(self):
        self.root = TrieNode()

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        t = Trie()
        for word in words:
            curr = t.root
            for c in word:
                if c not in curr.children:
                    curr.children[c] = TrieNode()
                curr = curr.children[c]
            curr.end = True
        #n= len(words) m = largest word length so --> n*m time complexity
        res = set()
        curr = []
        rows = len(board)
        cols = len(board[0])
        seen = set()
        def dfs(r,c, node):
            if node.end == True:
                res.add("".join(curr))
            if r<0 or c <0 or r==rows or c==cols or (r,c) in seen:
                return
            if board[r][c] in node.children:
                curr.append(board[r][c])
                seen.add((r,c))
                dfs(r+1,c, node.children[board[r][c]])
                dfs(r-1,c, node.children[board[r][c]])
                dfs(r, c+1, node.children[board[r][c]])
                dfs(r,c-1, node.children[board[r][c]])
                curr.pop()
                seen.remove((r,c))
        
        for r in range(rows):
            for c in range(cols):
                dfs(r,c, t.root)
        
        return list(res)
                

