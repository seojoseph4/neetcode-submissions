class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mappings = {'2': ('a','b','c'),
        '3': ('d','e','f'),
        '4': ('g','h','i'),
        '5': ('j','k','l'),
        '6': ('m','n','o'),
        '7': ('p','q','r', 's'),
        '8': ('t','u','v'),
        '9': ('w','x','y', 'z')}

        res = []

        def dfs(i, sublist):
            if i == len(digits):
                if len(sublist) >0:
                    res.append(sublist)
                return
            for letter in mappings[digits[i]]:
                sublist+=letter
                dfs(i+1, sublist)
                sublist = sublist[:-1]
        dfs(0, "")

        return res
        