from typing import List

class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []
        for word in strs:
            l = str(len(word))
            res.append(l)
            res.append("#")
            for ch in word:
                res.append(ch)
        print(''.join(res))
        return ''.join(res)
    def decode(self, s: str) -> List[str]:
        res = []
        currnum = ""
        i = 0
        while i < len(s):
            # print(s[i])
            if s[i] == "#":
                currnum = int(currnum)
                currval = s[i+1: i+currnum+1]
                i+=int(currnum)
                currnum = ""
                res.append(currval)
                # print(currval)
                # print(i)
            else:
                # print(currnum)
                currnum+= s[i]
            i+=1
        
        return res 
        
