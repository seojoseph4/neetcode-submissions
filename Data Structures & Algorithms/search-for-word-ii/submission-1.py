class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False

    def addWord(self, word):
        curr = self
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.isWord = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for w in words:
            root.addWord(w)

        res = set()
        visit = set()


        def dfs(i, j, node, word):
            if i < 0 or j < 0 or i >= len(board) or j >=len(board[0]):
                return
            if board[i][j] not in node.children:
                return
            if (i,j) in visit:
                return
            visit.add((i,j))
            
            
            node = node.children[board[i][j]]
            word +=board[i][j]
            if node.isWord:
                res.add(word)
            dfs(i-1, j, node, word)
            dfs(i, j-1, node, word)
            dfs(i+1, j, node, word)
            dfs(i, j+1, node, word)

            visit.remove((i,j))
            
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                dfs(i, j, root, "")
        return list(res)
        