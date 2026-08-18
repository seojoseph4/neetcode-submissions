class MedianFinder:

    def __init__(self):
        self.minhp = []
        self.maxhp = []
        self.size = 0

    def addNum(self, num: int) -> None:
        self.size +=1
        if not self.maxhp and not self.minhp:
            heapq.heappush(self.maxhp, -num)
            return
        if num < -self.maxhp[0]:
            heapq.heappush(self.maxhp, -num)
        else:
            heapq.heappush(self.minhp, num)
        
        #balance
        diff = len(self.minhp) - len(self.maxhp)
        if diff > 1 or diff < -1:
            if len(self.minhp) > len(self.maxhp):
                heapq.heappush(self.maxhp, -heapq.heappop(self.minhp))
            else:
                heapq.heappush(self.minhp, -heapq.heappop(self.maxhp))


    def findMedian(self) -> float:
        print("min", self.minhp)
        print("max",self.maxhp)
        print("brek")
        if self.size%2 == 0:
            return (self.minhp[0] + -self.maxhp[0]) / 2
        else:
            if len(self.minhp) > len(self.maxhp):
                return self.minhp[0]
            else:
                return -self.maxhp[0]
        
        