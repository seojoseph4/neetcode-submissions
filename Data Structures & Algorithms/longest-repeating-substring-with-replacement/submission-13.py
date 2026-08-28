class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #sliding window approach, keep expanding right pointer until not valid, if not valid, move left pointer until valid again

        l = 0
        r = 0
        maxf = 0
        res = 0
        counter = defaultdict(int)
        while r < len(s):
            # print("-")
            # print(l,r)
            # print(counter)
            counter[s[r]]+=1
            maxf = max(maxf, counter[s[r]])
            while (r-l+1) - maxf > k:
                counter[s[l]]-=1
                l+=1
                if counter[s[l]] == 0:
                    del counter[s[l]]
            res = max(res, (r-l+1))
            r+=1
        
        return res

                