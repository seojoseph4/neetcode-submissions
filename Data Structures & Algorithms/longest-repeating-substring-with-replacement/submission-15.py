class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, r = 0, 0

        res = 0

        maxF = 0
        hm = defaultdict(int)
        while r < len(s):
            hm[s[r]]+=1
            maxF = max(maxF, hm[s[r]])

            while (r-l+1) - maxF > k:
                hm[s[l]]-=1
                if hm[s[l]] == 0:
                    del hm[s[l]]
                l+=1
            res = max(res, (r-l+1))
            r+=1
        return res