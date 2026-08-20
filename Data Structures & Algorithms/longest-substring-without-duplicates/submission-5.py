class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        r = 0
        hm = {}
        res = 0

        while r <len(s):
            if s[r] in hm and hm[s[r]] >= l:
                l = hm[s[r]]+1
            res = max(res, (r-l)+1)
            hm[s[r]] = r
            r+=1
        return res






        