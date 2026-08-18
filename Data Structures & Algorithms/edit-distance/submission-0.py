class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # choices: insert the character to match, delete for potential match, replace character
        # states, index, current letter

        memo = {}

        def dfs(i, j):

            if i == len(word1):
                return len(word2) - j
            if j == len(word2):
                return len(word1) - i

            if word1[i] == word2[j]:
                memo[(i,j)] = dfs(i+1, j+1)

            else:
                #Try inserting the needed character
                insert = dfs(i, j+1)

                #Try deleting the current character
                delete = dfs(i+1, j)

                #Try replacing the character
                replace = dfs(i+1, j+1)
                memo[(i,j)] = min(insert, delete, replace) +1
            return memo[(i,j)]

        

        return dfs(0, 0)
        