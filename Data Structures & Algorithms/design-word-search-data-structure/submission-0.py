class Node:
    def __init__(self):
        self.children = {}
        self.end = False
class WordDictionary:
    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = Node()
            curr = curr.children[c]
        curr.end = True        

    def search(self, word: str) -> bool:
        def dfs(j, root):
            curr = root
            for c in range(j, len(word)):
                if word[c] != '.':
                    if word[c] not in curr.children:
                        return False
                    curr = curr.children[word[c]]
                else:
                    for chil in curr.children.values():
                        if dfs(c+1,chil):
                            return True
                    return False
            return curr.end
        return dfs(0,self.root)

        
