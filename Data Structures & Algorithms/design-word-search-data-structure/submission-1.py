class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for ch in word:
            if ch not in curr.children:
                curr.children[ch] = TrieNode()
            curr = curr.children[ch]
        curr.end = True

    def search(self, word: str) -> bool:
        def helper(i, curr):
            if i == len(word):
                if curr.end:
                    return True
                else:
                    return False
            if word[i] == ".":
                for ch in curr.children.values():
                    if helper(i+1, ch):
                        return True
                return False
            if word[i] not in curr.children:
                return False
            curr = curr.children[word[i]]
            return helper(i+1, curr)

        return helper(0, self.root)

        
