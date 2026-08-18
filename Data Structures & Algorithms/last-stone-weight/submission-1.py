class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-stone for stone in stones]
        heapq.heapify(stones)
        while len(stones) >1:
            first = -heapq.heappop(stones)
            second = -heapq.heappop(stones)
            smash = first - second
            if smash !=0:
                heapq.heappush(stones,-smash)
        if len(stones) == 1:
            return -heapq.heappop(stones)
        else:
            return 0
        