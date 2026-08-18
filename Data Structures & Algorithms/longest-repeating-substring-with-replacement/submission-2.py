class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        mapping = {}
        res = 0
        l = 0
        r = 0
        maxf = 0
        while r < len(s):
            if s[r] in mapping:
                mapping[s[r]] += 1
            else:
                mapping[s[r]] = 1
            maxf = max(mapping[s[r]], maxf)
            while l <r and ((r-l+1) - maxf) > k:
                mapping[s[l]] -=1
                l+=1
            res = max(res, (r-l+1))

            r+=1
        return res

        