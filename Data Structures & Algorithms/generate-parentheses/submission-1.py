class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        curr = []

        def bt(closes, opens):
            if closes > opens:
                return
            if opens > n or closes > n:
                return
            if opens == n and closes == n:
                res.append("".join(curr))
                return
            curr.append("(")
            bt(closes, opens+1)
            curr.pop()
            curr.append(")")
            bt(closes+1, opens)
            curr.pop()
        bt(0,0)
        return res

            