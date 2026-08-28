class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        hm = {
            2: ["a","b","c"],
            3: ["d","e","f"],
            4: ["g","h", "i"],
            5: ["j", "k", "l"],
            6: ["m","n","o"],
            7: ["p","q","r","s"],
            8: ["t","u","v"],
            9: ["w","x","y","z"]
        }
        res = []
        curr = []
        def bt(i):
            if i == len(digits):
                res.append("".join(curr)) if curr else None
                return
            for ch in hm[int(digits[i])]:
                curr.append(ch)
                bt(i+1)
                curr.pop()
        bt(0)
        return res
            
