class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        map = {}
        l = 0
        r = 0
        ma = 0
        curr = 0
        while r < len(s):
            if s[r] in map and map[s[r]] >= l:
                l = map[s[r]]+1
            map[s[r]] = r
            curr = r - l +1
            ma = max(curr, ma)
            r +=1
        return ma






        