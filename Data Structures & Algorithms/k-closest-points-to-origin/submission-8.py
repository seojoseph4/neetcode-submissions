class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        hp =[]

        for x,y in points:
            dist = -(x*x + y*y)
            heapq.heappush(hp, [dist, x, y])
            if len(hp) > k:
                heapq.heappop(hp)

        return [[x,y] for _, x, y in hp]