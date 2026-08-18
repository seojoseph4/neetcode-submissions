class StockSpanner:

    def __init__(self):
        self.s = []

    def next(self, price: int) -> int:
        self.s.append(price)
        res = 0
        for i in range(len(self.s)-1,-1,-1):
            if self.s[i] <= price:
                res+=1
            else:
                break
        return res
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)