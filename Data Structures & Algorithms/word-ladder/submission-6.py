class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        adj = defaultdict(list)
        for word in wordList:
            for c in range(len(word)):
                key = word[:c] + "*" + word[c+1:]
                adj[key].append(word)

        q = deque()
        q.append(beginWord)
        res = 1
        seen = set()
        seen.add(beginWord)
        while q:
            for _ in range(len(q)):
                popped = q.popleft()
                if popped == endWord:
                    return res
                for c in range(len(popped)):
                    key = popped[:c] + "*" + popped[c+1:]
                    for word in adj[key]:

                        if word!= popped and word not in seen:
                            q.append(word)
                            seen.add(word)

            res+=1

        return 0

        