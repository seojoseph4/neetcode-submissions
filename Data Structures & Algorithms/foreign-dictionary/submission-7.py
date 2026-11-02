class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = {c: set() for w in words for c in w}
        
        for i in range(len(words)-1):
            one = words[i]
            two = words[i+1]
            minlen = min(len(one), len(two))
            if len(one) > len(two) and one[:minlen] == two[:minlen]:
                return ""
            for j in range(minlen):
                if one[j]!=two[j]:
                    adj[one[j]].add(two[j])
                    break

        seen = set()
        seeing = set()
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
                