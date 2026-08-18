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
            num = ""
            print(s[curr])
            while s[curr] != "#":
                num+=s[curr]
                curr+=1
            curr+=1
            temp =""
            for i in range(int(num)):
                temp+=s[curr]
                curr+=1
            ans.append(temp)
            print(temp)
        return ans
            

