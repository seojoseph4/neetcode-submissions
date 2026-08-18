class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        mapping = {}
        for i in range(n):
            mapping[i] = []
        
        for pair in edges:
            mapping[pair[0]].append(pair[1])
            mapping[pair[1]].append(pair[0])
        
        seen = set()
        def dfs(index, par):
            if index in seen:
                return False
            seen.add(index)
            if mapping[index] == []:
                return True

            
            for nei in mapping[index]:
                if nei == par:
                    continue
                if not dfs(nei, index):
                    return False
            mapping[index] = []
            return True


        if not dfs(i,-1):
            return False

        return len(seen) == n
        