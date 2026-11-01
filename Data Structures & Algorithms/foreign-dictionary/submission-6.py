class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = {c: set() for w in words for c in w}
        for i in range(len(words)-1):
            one = words[i]
            two = words[i+1]
            minLen = min(len(one), len(two))
            if len(one) > len(two) and one[:minLen] == two[:minLen]:
                return ""
            for j in range(minLen):
                if one[j] != two[j]:
                    adj[one[j]].add(two[j])
                    break
        
        seen = set()
        seeing = set()
        res= []
        def dfs(curr):
            if curr in seen:
                return True
            if curr in seeing:
                return False
            seeing.add(curr)
            for pre in adj[curr]:
                if not dfs(pre):
                    return False
            seeing.remove(curr)
            seen.add(curr)
            res.append(curr)
            return True
        for char in adj:
            if not dfs(char):
                return ""
        return "".join(reversed(res))