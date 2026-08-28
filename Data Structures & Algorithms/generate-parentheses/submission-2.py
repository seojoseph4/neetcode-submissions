class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        curr = []

        def bt(closes, opens):
            if opens == n and closes == n:
                res.append("".join(curr))
                return
            if opens < n:
                curr.append("(")
                bt(closes, opens+1)
                curr.pop()
            if closes < opens:
                curr.append(")")
                bt(closes+1, opens)
                curr.pop()
        bt(0,0)
        return res

            