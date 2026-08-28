class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def pcheck(l,r):
            #inclusive
            while l < r:
                if s[l] != s[r]:
                    return False
                l+=1
                r-=1
            return True


        res = []
        curr = []
        def bt(i):
            if i == len(s):
                res.append(curr[:])
                return
            
            for j in range(i, len(s)):
                if pcheck(i, j) == False:
                    continue
                curr.append(s[i:j+1])
                bt(j+1)
                curr.pop()
        bt(0)
        return res