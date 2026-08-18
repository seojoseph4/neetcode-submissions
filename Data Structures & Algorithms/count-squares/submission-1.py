class CountSquares:
    def __init__(self):
        self.ptsCount = defaultdict(int)

    def add(self, point: List[int]) -> None:
        self.ptsCount[tuple(point)] += 1

    def count(self, point: List[int]) -> int:
        res = 0
        px, py = point
        for (x, y), cnt in self.ptsCount.items():
            if abs(py - y) != abs(px - x) or x == px or y == py:
                continue
            res += cnt * self.ptsCount.get((x, py), 0) * self.ptsCount.get((px, y), 0)
        return res



            
        
