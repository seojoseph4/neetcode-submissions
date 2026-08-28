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
        def bt(l,r):
            if r == len(s):
                res.append(curr[:])
                return
            
            for j in range(r, len(s)):
                if pcheck(l, j) == False:
                    continue
                curr.append(s[l:j+1])
                bt(j+1, j+1)
                curr.pop()
        bt(0,0)
        return res