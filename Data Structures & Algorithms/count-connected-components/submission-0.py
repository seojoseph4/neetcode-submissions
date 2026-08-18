class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        mapping = {}
        for i in range(n):
            mapping[i] = []
        for pair in edges:
            mapping[pair[0]].append(pair[1])
            mapping[pair[1]].append(pair[0])
        print(mapping) 
        res = 0

        seen = set()
        def dfs(curr):
            if curr in seen:
                return
            seen.add(curr)
            if mapping[curr] == []:
                return
            for nei in mapping[curr]:
                dfs(nei)
            mapping[curr] = []
            return

        for i in range(n):
            if i not in seen:
                dfs(i)
                res+=1
                print(seen)
                print(mapping)

        return res
         