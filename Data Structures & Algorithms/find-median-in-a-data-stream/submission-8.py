class MedianFinder:

    def __init__(self):
        self.minheap = []
        self.maxheap = []

    def addNum(self, num: int) -> None:

        #first, check where the new element should go
        if not self.minheap:
            heapq.heappush(self.minheap, num)
            return
        if num > self.minheap[0]:
            heapq.heappush(self.minheap, num)
        else:
            heapq.heappush(self.maxheap, -1*num)
        
        #now balance out the heaps

        while abs(len(self.minheap) - len(self.maxheap)) > 1:
            if len(self.minheap) > len(self.maxheap):
                popped = heapq.heappop(self.minheap)
                heapq.heappush(self.maxheap, -1*popped)
            else:
                popped = heapq.heappop(self.maxheap)
                heapq.heappush(self.minheap, -1*popped)
        

        
    #maxheap -- minheap

    def findMedian(self) -> float:
        if len(self.maxheap) > len(self.minheap):
            return self.maxheap[0] * -1
        elif len(self.minheap) > len(self.maxheap):
            return self.minheap[0]
        else:
            return (self.minheap[0] + (-1 * self.maxheap[0])) /2 
        
        