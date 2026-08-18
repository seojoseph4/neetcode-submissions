class FreqStack:

    def __init__(self):
        self.hm = defaultdict(int)
        self.maxCnt = 0
        self.groups = {}

    def push(self, val: int) -> None:
        
        self.hm[val]+=1
        valCnt = self.hm[val]
        if valCnt > self.maxCnt:
            self.maxCnt = valCnt
            self.groups[valCnt] = []
        self.groups[valCnt].append(val)

    def pop(self) -> int:
        res = self.groups[self.maxCnt].pop()
        if not self.groups[self.maxCnt]:
            self.maxCnt -= 1
        self.hm[res] -=1
        return res

        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()