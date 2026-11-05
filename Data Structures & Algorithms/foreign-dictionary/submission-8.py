class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = {c: set() for w in words for c in w}
        
        for i in range(len(words)-1):
            first = words[i]
            second = words[i+1]
            minlen = min(len(first),len(second))
            if len(first) > len(second) and first[:minlen] == second[:minlen]:
                return ""
            for j in range(minlen):
                if first[j] != second[j]:
                    adj[first[j]].add(second[j])
                    break

        seen = set()
        seeing=set()
        res = []
        def dfs(node):
            if node in seen:
                return True
            if node in seeing:
                return False
            
            seeing.add(node)
            for nei in adj[node]:
                if dfs(nei) == False:
                    return False
            seeing.remove(node)
            seen.add(node)
            res.append(node)
            return True
        
        for ch in adj.keys():
            if dfs(ch) == False:
                return ""

        return "".join(res[::-1])
