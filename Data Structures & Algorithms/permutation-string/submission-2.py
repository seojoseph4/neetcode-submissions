class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        hm1 = defaultdict(int)
        for s in s1:
            hm1[s] +=1
        
        l = 0
        r = 0

        hm2 = defaultdict(int)
        while r < len(s2):
            hm2[s2[r]]+=1
            if (r-l+1) > len(s1):
                hm2[s2[l]]-=1
                if hm2[s2[l]] == 0:
                    del hm2[s2[l]]
                l+=1
            # print(hm1, hm2)
            if hm1 == hm2:
                return True
            r+=1
        return False
        
        
    
