class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        hp = [-s for s in stones]
        heapq.heapify(hp)

        while len(hp) > 1:
            x = -1 * heapq.heappop(hp)
            y= -1 * heapq.heappop(hp)
            if x == y:
                continue
            else:
                heapq.heappush(hp, -(x-y))
        
        if len(hp) ==1:
            return -1 * hp[0]
        else:
            return 0
