class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = {}
        for str in strs:
            match = [0]*26
            for char in str:
                match[ord(char)-ord('a')]+=1
            match_tup = tuple(match)
            if match_tup in ans:
                ans[match_tup].append(str)
            else:
                ans[match_tup] = [str]
        return list(ans.values())

        