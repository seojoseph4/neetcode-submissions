class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        graph = {}
        for word in words:
            for c in word:
                graph[c] = []
        for i in range(0,len(words)-1):
            first = words[i]
            second = words[i+1]
            # print(first, second)
            j = 0
            while j < len(first) and j < len(second):
                if first[j] != second[j]:
                    graph[first[j]].append(second[j])
                    break
                j+=1
            if j == len(second) and len(first) > len(second):
                return ""

            
            
        visited = {}
        res = []
        def dfs(char):
            if char in visited:
                return visited[char]
            visited[char] = True
            for nei in graph[char]:
                if dfs(nei):
                    return True
            visited[char] = False
            res.append(char)
            return False

        for char in graph:
            if dfs(char):
                return ""
        res.reverse()

        return "".join(res)

                    
                

        