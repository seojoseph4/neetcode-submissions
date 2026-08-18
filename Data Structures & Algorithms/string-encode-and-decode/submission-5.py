class Solution:

    def encode(self, strs: List[str]) -> str:
        ans =""
        for st in strs:
            ans+=str(len(st))
            ans+="#"
            ans+=st
        return ans

    def decode(self, s: str) -> List[str]:
        ans=[]
        print(s)
        curr = 0
        while curr < len(s) - 1:
            j = curr
            while s[j] != "#":
                j+=1
            l = int(s[curr:j])
            curr = j+1
            j = j+1+l
            ans.append(s[curr:j])
            print(ans)
            curr = j
        return ans
            

