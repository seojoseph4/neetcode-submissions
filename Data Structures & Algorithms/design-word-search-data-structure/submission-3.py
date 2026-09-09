class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False


class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.end = True
        

    def search(self, word: str) -> bool:
        def dfs(i, curr):
            if i == len(word):
                return curr.end
            if word[i] in curr.children:
                curr = curr.children[word[i]]
                return dfs(i+1, curr)
            if word[i] == ".":
                for ch, child in curr.children.items():
                    if dfs(i+1, child):
                        return True
            return False
        return dfs(0, self.root)
            

        
