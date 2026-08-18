class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        mapping1 = defaultdict(int)
        mapping2 = defaultdict(int)
        
        for c in s1:
            mapping1[c]+=1
        

        l = 0
        for r in range(len(s2)):
            mapping2[s2[r]]+=1
            if (r-l+1) > len(s1):
                mapping2[s2[l]]-=1
                if mapping2[s2[l]] == 0:
                    del mapping2[s2[l]]
                l+=1

            if mapping2 == mapping1:
                return True
        
        if mapping2 == mapping1:
            return True
        return False
        
        
    
