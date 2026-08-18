class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        mapping1 = {}
        mapping2 = {}
        
        for c in s1:
            mapping1[c] = 1 + mapping1.get(c, 0)
        
        for c in s2[:len(s1)]:
            mapping2[c] = 1 + mapping2.get(c, 0)
        
        need = len(mapping1)
        curr = 0
        
        for x in mapping1:
            if mapping1[x] == mapping2.get(x, 0):
                curr += 1
        
        if curr == need:
            return True
        
        l = 0
        for r in range(len(s1), len(s2)):
            in_char = s2[r]
            mapping2[in_char] = mapping2.get(in_char, 0) + 1
            if in_char in mapping1:
                if mapping2[in_char] == mapping1[in_char]:
                    curr += 1
                elif mapping2[in_char] - 1 == mapping1[in_char]:
                    curr -= 1
            
            out_char = s2[l]
            if out_char in mapping1:
                # check BEFORE updating
                if mapping2.get(out_char, 0) == mapping1[out_char]:
                    curr -= 1
                elif mapping2.get(out_char, 0) - 1 == mapping1[out_char]:
                    curr += 1
            
            mapping2[out_char] = mapping2.get(out_char, 0) - 1
            if mapping2[out_char] == 0:
                del mapping2[out_char]
            
            if curr == need:
                return True
            l += 1
        
        return False
