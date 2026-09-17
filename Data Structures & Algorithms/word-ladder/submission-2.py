class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        hm = defaultdict(set)
        for word in wordList:
            for i in range(len(word)):
                temp = word[:i] + "*" + word[i+1:]
                hm[temp].add(word)
        
        # print(hm)
        q = deque()
        q.append(beginWord)
        seen = set()
        seen.add(beginWord)
        res= 1
        while q:
            for _ in range(len(q)):
                word = q.popleft()
                for i in range(len(word)):
                    temp = word[:i] + "*" + word[i+1:]
                    for nei in hm[temp]:
                        if nei in seen:
                            continue
                        if nei == endWord:
                            return res + 1
                        q.append(nei)
                        seen.add(nei)
            res+=1
        return 0
                    


